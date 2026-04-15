#!/usr/bin/env python3
"""
Feature Detection and Mapping System
Maps changed files to features using configuration rules.
"""

import argparse
import fnmatch
import glob
import json
import os
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set


def glob_match(path: str, pattern: str) -> bool:
    """Match path against glob pattern with ** support."""
    # Convert glob pattern to regex
    if '**' in pattern:
        # ** matches any number of directory levels
        # * matches anything except /
        # ? matches single char
        
        # Manual regex conversion to avoid over-escaping
        regex = ''
        i = 0
        while i < len(pattern):
            if pattern[i:i+2] == '**':
                regex += '.*'
                i += 2
            elif pattern[i] == '*':
                regex += '[^/]*'
                i += 1
            elif pattern[i] == '?':
                regex += '.'
                i += 1
            elif pattern[i] == '/':
                regex += '/'
                i += 1
            elif pattern[i] == '.':
                regex += r'\.'
                i += 1
            else:
                regex += re.escape(pattern[i])
                i += 1
        
        return bool(re.match('^' + regex + '$', path))
    else:
        # Use standard fnmatch for simple patterns
        return fnmatch.fnmatch(path, pattern)

import yaml


@dataclass
class Feature:
    id: str
    name: str
    description: str
    doc_path: str
    priority: str
    related_files: Set[str] = field(default_factory=set)


@dataclass
class FileChange:
    path: str
    change_type: str = "modified"
    diff_content: str = ""
    lines_added: int = 0
    lines_removed: int = 0


class FeatureMapper:
    def __init__(self, config_path: str = "docs/.ai-docs-config.yml"):
        self.config = self._load_config(config_path)
        self.features = self._load_features()
        self.pattern_map = self._build_pattern_map()
    
    def _load_config(self, path: str) -> dict:
        if not os.path.exists(path):
            return self._default_config()
        with open(path) as f:
            return yaml.safe_load(f) or self._default_config()
    
    def _default_config(self) -> dict:
        return {
            "feature_mapping": {"patterns": []},
            "features": {},
            "unmapped_files": {"strategy": "ignore", "min_changes_threshold": 3},
            "multi_feature_strategy": {"max_features_per_pr": 5, "semantic_grouping": True}
        }
    
    def _load_features(self) -> Dict[str, Feature]:
        features = {}
        for feat_id, feat_data in self.config.get("features", {}).items():
            features[feat_id] = Feature(
                id=feat_id,
                name=feat_data.get("name", feat_id),
                description=feat_data.get("description", ""),
                doc_path=feat_data.get("doc_path", f"docs/features/{feat_id}.md"),
                priority=feat_data.get("priority", "medium")
            )
        return features
    
    def _build_pattern_map(self) -> List[tuple]:
        patterns = []
        for mapping in self.config.get("feature_mapping", {}).get("patterns", []):
            pattern = mapping.get("pattern", "")
            feat_ids = mapping.get("features", [])
            if isinstance(feat_ids, str):
                feat_ids = [feat_ids]
            patterns.append((pattern, feat_ids))
        return patterns
    
    def map_files_to_features(self, changed_files: List[FileChange]) -> Dict[str, Set[str]]:
        feature_files = defaultdict(set)
        unmapped_files = []
        
        for file_change in changed_files:
            file_path = file_change.path
            mapped = False
            
            for pattern, feature_ids in self.pattern_map:
                if glob_match(file_path, pattern):
                    for feat_id in feature_ids:
                        if feat_id in self.features:
                            feature_files[feat_id].add(file_path)
                            self.features[feat_id].related_files.add(file_path)
                            mapped = True
            
            if not mapped:
                unmapped_files.append(file_change)
        
        # Handle unmapped files
        if unmapped_files:
            self._handle_unmapped_files(unmapped_files, feature_files)
        
        return dict(feature_files), unmapped_files
    
    def _handle_unmapped_files(self, unmapped: List[FileChange], feature_files: Dict):
        strategy = self.config.get("unmapped_files", {}).get("strategy", "ignore")
        
        if strategy == "ignore":
            return
        
        threshold = self.config.get("unmapped_files", {}).get("min_changes_threshold", 3)
        
        # Cluster by directory
        clusters = defaultdict(list)
        for f in unmapped:
            parts = Path(f.path).parts
            if len(parts) >= 2:
                cluster_key = f"{parts[0]}/{parts[1]}"
            else:
                cluster_key = parts[0] if parts else "root"
            clusters[cluster_key].append(f)
        
        # Suggest new features for large clusters
        for cluster_key, files in clusters.items():
            if len(files) >= threshold and strategy == "suggest_new_feature":
                suggested_id = f"suggested-{cluster_key.replace('/', '-').lower()}"
                feature_files[suggested_id] = {f.path for f in files}
                print(f"🆕 Suggested new feature: {cluster_key} ({len(files)} files)")
    
    def detect_multi_feature_pr(self, feature_files: Dict[str, Set[str]]) -> bool:
        max_features = self.config.get("multi_feature_strategy", {}).get("max_features_per_pr", 5)
        return len(feature_files) > max_features
    
    def generate_impact_report(self, feature_files: Dict[str, Set[str]], 
                              unmapped: List[FileChange],
                              changed_files: List[FileChange]) -> Dict:
        report = {
            "affected_features": [],
            "total_files_changed": len(changed_files),
            "unmapped_files": [f.path for f in unmapped],
            "multi_feature_pr": self.detect_multi_feature_pr(feature_files),
            "impact_summary": {}
        }
        
        for feat_id, files in feature_files.items():
            feature = self.features.get(feat_id)
            if feature:
                report["affected_features"].append({
                    "id": feat_id,
                    "name": feature.name,
                    "files": sorted(list(files)),
                    "priority": feature.priority,
                    "doc_path": feature.doc_path
                })
            else:
                report["affected_features"].append({
                    "id": feat_id,
                    "name": f"Unmapped: {feat_id}",
                    "files": sorted(list(files)),
                    "priority": "unknown",
                    "doc_path": None
                })
        
        return report


def main():
    parser = argparse.ArgumentParser(description="Detect features from changed files")
    parser.add_argument("--changed-files", required=True, help="File containing list of changed files")
    parser.add_argument("--output", required=True, help="Output JSON file")
    parser.add_argument("--config", default="docs/.ai-docs-config.yml", help="Configuration file path")
    
    args = parser.parse_args()
    
    # Read changed files
    changed_files = []
    if os.path.exists(args.changed_files):
        with open(args.changed_files) as f:
            for line in f:
                line = line.strip()
                if line:
                    changed_files.append(FileChange(path=line))
    
    # Run detection
    mapper = FeatureMapper(args.config)
    feature_files, unmapped = mapper.map_files_to_features(changed_files)
    
    # Generate report
    report = mapper.generate_impact_report(feature_files, unmapped, changed_files)
    
    # Write output
    with open(args.output, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"Feature detection complete. Report written to {args.output}")
    print(f"Features affected: {len(report['affected_features'])}")
    print(f"Unmapped files: {len(report['unmapped_files'])}")


if __name__ == "__main__":
    main()
