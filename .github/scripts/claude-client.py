#!/usr/bin/env python3
"""
Claude API Client for Documentation Generation
Handles API calls, prompt management, and response parsing.
"""

import argparse
import json
import os
import time
from dataclasses import dataclass
from typing import Dict, List, Optional

from anthropic import Anthropic


@dataclass
class DocumentationRequest:
    feature_id: str
    feature_name: str
    doc_type: str  # technical, user_guide, changelog, api
    context: Dict
    previous_content: Optional[str] = None
    change_diff: Optional[str] = None


@dataclass
class DocumentationResponse:
    content: str
    sections_updated: List[str]
    confidence_score: float


class ClaudeDocumentationClient:
    MODEL = "claude-3-5-sonnet-20241022"
    MAX_TOKENS = 4096
    TEMPERATURE = 0.3
    
    def __init__(self, api_key: Optional[str] = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
    
    def generate_documentation(self, request: DocumentationRequest) -> DocumentationResponse:
        prompt = self._build_prompt(request)
        
        response = self.client.messages.create(
            model=self.MODEL,
            max_tokens=self.MAX_TOKENS,
            temperature=self.TEMPERATURE,
            system=self._get_system_prompt(request.doc_type),
            messages=[{"role": "user", "content": prompt}]
        )
        
        content = response.content[0].text
        
        return DocumentationResponse(
            content=content,
            sections_updated=self._extract_sections(content),
            confidence_score=self._estimate_confidence(content)
        )
    
    def _build_prompt(self, request: DocumentationRequest) -> str:
        base_prompt = f"""# Documentation Update Request

## Feature Information
- Feature ID: {request.feature_id}
- Feature Name: {request.feature_name}
- Documentation Type: {request.doc_type}

## Context
{json.dumps(request.context, indent=2)}

"""
        
        if request.previous_content:
            base_prompt += f"""## Previous Documentation Content
```markdown
{request.previous_content[:10000]}
```

"""
        
        if request.change_diff:
            base_prompt += f"""## Code Changes Summary
Files changed: {request.change_diff[:5000]}

"""
        
        base_prompt += self._get_type_instructions(request.doc_type)
        return base_prompt
    
    def _get_system_prompt(self, doc_type: str) -> str:
        prompts = {
            "technical": """You are an expert technical writer specializing in Python project documentation.
Update technical documentation based on code changes. Maintain existing structure.
Use clear, precise language. Include code examples where relevant.""",
            
            "user_guide": """You are a user experience writer creating accessible documentation for Python learning projects.
Explain features to beginners. Use clear, jargon-free language. Include step-by-step instructions.""",
            
            "changelog": """You are a changelog writer following Keep a Changelog format.
Categorize changes: Added, Changed, Deprecated, Removed, Fixed, Security.
Be concise but informative.""",
            
            "api": """You are an API documentation specialist. Document endpoints, parameters, responses.
Include request/response examples. Follow REST API documentation best practices."""
        }
        return prompts.get(doc_type, prompts["technical"])
    
    def _get_type_instructions(self, doc_type: str) -> str:
        instructions = {
            "technical": """
## Instructions
Update the technical documentation with these changes. Return ONLY the updated markdown content.
Preserve existing content that wasn't changed. Format: Markdown""",
            
            "user_guide": """
## Instructions
Write or update the user guide section. Explain what changed in user-friendly terms.
Include practical examples. Return ONLY markdown content.""",
            
            "changelog": """
## Instructions
Generate changelog entries for the unreleased section following Keep a Changelog format.
Return only the changelog markdown section.""",
            
            "api": """
## Instructions
Document API changes. Include endpoints, methods, schemas, auth, errors.
Return in OpenAPI-compatible Markdown format."""
        }
        return instructions.get(doc_type, instructions["technical"])
    
    def _extract_sections(self, content: str) -> List[str]:
        import re
        sections = re.findall(r'^##+\s+(.+)$', content, re.MULTILINE)
        return sections[:10]
    
    def _estimate_confidence(self, content: str) -> float:
        score = 0.5
        if len(content) > 200:
            score += 0.1
        if '##' in content:
            score += 0.1
        if '```' in content:
            score += 0.1
        if '-' in content:
            score += 0.05
        if 'example' in content.lower():
            score += 0.05
        return min(score, 1.0)


def main():
    parser = argparse.ArgumentParser(description="Generate documentation with Claude")
    parser.add_argument("--request", required=True, help="JSON file containing documentation request")
    parser.add_argument("--output", required=True, help="Output file path")
    
    args = parser.parse_args()
    
    with open(args.request) as f:
        req_data = json.load(f)
    
    client = ClaudeDocumentationClient()
    request = DocumentationRequest(**req_data)
    
    response = client.generate_documentation(request)
    
    with open(args.output, 'w') as f:
        f.write(response.content)
    
    print(json.dumps({
        "confidence": response.confidence_score,
        "sections": response.sections_updated,
        "output_file": args.output
    }))


if __name__ == "__main__":
    main()
