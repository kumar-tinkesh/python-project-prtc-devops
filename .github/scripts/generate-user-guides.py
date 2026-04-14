#!/usr/bin/env python3
"""
Generate user guide documentation using Claude AI.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import yaml

sys.path.insert(0, os.path.dirname(__file__))
from claude_client import ClaudeDocumentationClient, DocumentationRequest


def generate_user_guide(feature: dict, config: dict, output_dir: str):
    """Generate user guide for a feature."""
    
    feature_id = feature["id"]
    feature_name = feature["name"]
    files = feature.get("files", [])
    
    output_path = os.path.join(output_dir, "user-guides", f"{feature_id}.md")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    context = {
        "feature_name": feature_name,
        "files": files,
        "description": feature.get("description", ""),
        "target_audience": "beginner"
    }
    
    request = DocumentationRequest(
        feature_id=feature_id,
        feature_name=feature_name,
        doc_type="user_guide",
        context=context,
        change_diff=json.dumps(files[:10])  # Limit files
    )
    
    client = ClaudeDocumentationClient()
    
    try:
        response = client.generate_documentation(request)
        
        with open(output_path, 'w') as f:
            f.write(response.content)
        
        print(f"✅ User guide: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Failed user guide {feature_id}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--config", default="docs/.ai-docs-config.yml")
    
    args = parser.parse_args()
    
    with open(args.report) as f:
        report = json.load(f)
    
    os.makedirs(os.path.join(args.output, "user-guides"), exist_ok=True)
    
    for feature in report.get("affected_features", []):
        if feature.get("priority") in ["high", "medium"]:
            generate_user_guide(feature, {}, args.output)
            time.sleep(0.5)
    
    print("\nUser guides generated.")


if __name__ == "__main__":
    main()
