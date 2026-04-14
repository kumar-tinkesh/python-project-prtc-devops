#!/usr/bin/env python3
"""
Generate technical documentation using Claude AI.
Processes feature report and generates/updating technical docs.
"""

import argparse
import json
import os
import sys
from pathlib import Path

import yaml

sys.path.insert(0, os.path.dirname(__file__))
from claude_client import ClaudeDocumentationClient, DocumentationRequest


def load_config(config_path: str) -> dict:
    with open(config_path) as f:
        return yaml.safe_load(f)


def load_report(report_path: str) -> dict:
    with open(report_path) as f:
        return json.load(f)


def ensure_dir(path: str):
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def generate_feature_doc(feature: dict, config: dict, output_dir: str):
    """Generate technical documentation for a single feature."""
    
    feature_id = feature["id"]
    feature_name = feature["name"]
    files = feature.get("files", [])
    doc_path = feature.get("doc_path", f"docs/features/{feature_id}.md")
    
    # Prepare output path
    output_path = os.path.join(output_dir, "features", f"{feature_id}.md")
    ensure_dir(output_path)
    
    # Check for existing content
    previous_content = ""
    if os.path.exists(doc_path):
        with open(doc_path) as f:
            previous_content = f.read()
    
    # Build context
    context = {
        "files_changed": files,
        "priority": feature.get("priority", "medium"),
        "description": feature.get("description", ""),
        "project_type": "python-learning"
    }
    
    # Create request
    request = DocumentationRequest(
        feature_id=feature_id,
        feature_name=feature_name,
        doc_type="technical",
        context=context,
        previous_content=previous_content,
        change_diff=json.dumps(files)
    )
    
    # Generate with Claude
    client = ClaudeDocumentationClient()
    
    try:
        response = client.generate_documentation(request)
        
        with open(output_path, 'w') as f:
            f.write(response.content)
        
        print(f"✅ Generated: {output_path} (confidence: {response.confidence_score:.2f})")
        return True
        
    except Exception as e:
        print(f"❌ Failed to generate {feature_id}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Generate technical documentation")
    parser.add_argument("--report", required=True, help="Feature report JSON")
    parser.add_argument("--output", required=True, help="Output directory")
    parser.add_argument("--config", default="docs/.ai-docs-config.yml", help="Config file")
    
    args = parser.parse_args()
    
    report = load_report(args.report)
    config = load_config(args.config)
    
    # Create output directories
    os.makedirs(os.path.join(args.output, "features"), exist_ok=True)
    os.makedirs(os.path.join(args.output, "api"), exist_ok=True)
    
    # Generate docs for each affected feature
    generated = 0
    failed = 0
    
    for feature in report.get("affected_features", []):
        if generate_feature_doc(feature, config, args.output):
            generated += 1
        else:
            failed += 1
        
        # Rate limiting
        import time
        time.sleep(0.5)
    
    print(f"\nSummary: {generated} generated, {failed} failed")
    
    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
