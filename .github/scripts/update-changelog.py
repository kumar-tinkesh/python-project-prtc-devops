#!/usr/bin/env python3
"""
Update changelog using Claude AI.
"""

import argparse
import json
import os
import sys
from datetime import datetime

from claude_client import ClaudeDocumentationClient, DocumentationRequest


def update_changelog(report: dict, changelog_path: str):
    """Update changelog with new changes."""
    
    features = report.get("affected_features", [])
    if not features:
        print("No features to add to changelog")
        return
    
    # Build context
    feature_list = [f"- {f['name']}: {', '.join(f['files'][:3])}" for f in features]
    
    context = {
        "changes": feature_list,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "version": "Unreleased"
    }
    
    request = DocumentationRequest(
        feature_id="changelog",
        feature_name="Project Changelog",
        doc_type="changelog",
        context=context,
        change_diff="\n".join(feature_list)
    )
    
    client = ClaudeDocumentationClient()
    
    try:
        response = client.generate_documentation(request)
        
        # Read existing changelog
        existing = ""
        if os.path.exists(changelog_path):
            with open(changelog_path) as f:
                existing = f.read()
        
        # Prepend new entries
        new_content = response.content + "\n\n" + existing
        
        with open(changelog_path, 'w') as f:
            f.write(new_content)
        
        print(f"✅ Updated: {changelog_path}")
        
    except Exception as e:
        print(f"❌ Failed to update changelog: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", required=True)
    parser.add_argument("--changelog", default="CHANGELOG.md")
    parser.add_argument("--config", default="docs/.ai-docs-config.yml")
    
    args = parser.parse_args()
    
    with open(args.report) as f:
        report = json.load(f)
    
    update_changelog(report, args.changelog)


if __name__ == "__main__":
    main()
