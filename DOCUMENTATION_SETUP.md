# Automated Documentation Pipeline - Setup Guide

Complete setup instructions for the AI-powered documentation automation system.

## Overview

This pipeline automatically generates and deploys documentation when code changes are merged to the `main` branch.

**Architecture:**
```
Code PR → Feature Detection → AI Doc Generation → Docs Repo PR → GitHub Pages
```

## Prerequisites

1. GitHub repository with your Python projects
2. Anthropic API key (for Claude AI)
3. GitHub Personal Access Token (for cross-repo access)

## Setup Steps

### 1. Configure Repository Secrets

Go to **Settings → Secrets and variables → Actions** and add:

| Secret | Value | Required |
|--------|-------|----------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key | Yes |
| `DOCS_REPO_TOKEN` | GitHub PAT with `repo` scope | Yes |

**Create PAT:**
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with scopes: `repo`, `workflow`
3. Copy token and add as `DOCS_REPO_TOKEN` secret

### 2. Create Documentation Repository

Create a new repository for hosting documentation (e.g., `python-projects-docs`):

```bash
# Create new repo on GitHub, then:
git clone https://github.com/YOUR_USERNAME/python-projects-docs.git
cd python-projects-docs
```

Add these files to the docs repo:

**`mkdocs.yml`:**
```yaml
site_name: Python Projects Documentation
site_url: https://yourusername.github.io/python-projects-docs

nav:
  - Home: index.md
  - Features: features/
  - API Reference: api-reference/
  - Changelog: changelogs/

theme:
  name: material
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
    - scheme: slate
      primary: indigo
      accent: indigo

plugins:
  - search

markdown_extensions:
  - pymdownx.highlight
  - pymdownx.superfences
```

**`docs/index.md`:**
```markdown
# Python Projects Documentation

Welcome to the documentation for Python learning projects.
```

### 3. Update Configuration

Edit `docs/.ai-docs-config.yml` in your main repo:

```yaml
docs_sync:
  target_repo: "YOUR_USERNAME/python-projects-docs"  # Update this!
```

### 4. Install Dependencies (Local Testing)

```bash
pip install -r requirements-automation.txt
```

### 5. Test Locally

```bash
# Test feature detection
echo "weatherData/app.py" > changed_files.txt
python .github/scripts/feature-mapper.py \
  --changed-files changed_files.txt \
  --output report.json \
  --config docs/.ai-docs-config.yml

cat report.json
```

### 6. Enable GitHub Actions

The workflows are already in `.github/workflows/`. They will activate automatically on push to `main`.

### 7. Configure GitHub Pages (Docs Repo)

1. Go to docs repo → Settings → Pages
2. Source: GitHub Actions
3. Save

## Workflow Execution

The pipeline runs automatically when you push to `main`:

1. **01-detect-features.yml** - Analyzes changed files
2. **02-generate-docs.yml** - Calls Claude AI to generate docs
3. **03-sync-docs-repo.yml** - Creates PR in docs repo
4. **04-deploy-docs.yml** - Deploys to GitHub Pages (in docs repo)

## Manual Trigger

You can manually trigger workflows:

1. Go to **Actions** tab
2. Select workflow (e.g., "01 - Feature Detection")
3. Click **Run workflow**

## Customization

### Adding New Features

Edit `docs/.ai-docs-config.yml`:

```yaml
feature_mapping:
  patterns:
    - pattern: "**/my-new-project/**"
      features: ["my-new-feature"]

features:
  my-new-feature:
    name: "My New Feature"
    description: "Description here"
    doc_path: "docs/features/my-new-feature.md"
    priority: "medium"
```

### Modifying AI Prompts

Edit the prompt templates in `docs/.ai-docs-config.yml` under `ai.prompts`.

## Troubleshooting

### Workflow Fails

Check the Actions tab for error logs. Common issues:
- Missing secrets (`ANTHROPIC_API_KEY`, `DOCS_REPO_TOKEN`)
- Invalid YAML in configuration
- Rate limiting from Anthropic API

### No Documentation Generated

- Verify `.ai-docs-config.yml` has correct file patterns
- Check that changed files match patterns
- Ensure features are defined in configuration

### Cross-Repo Sync Fails

- Verify `DOCS_REPO_TOKEN` has `repo` scope
- Check that target repo exists and is accessible
- Ensure token hasn't expired

## File Structure

```
Python-Projects/
├── .github/
│   ├── workflows/
│   │   ├── 01-detect-features.yml
│   │   ├── 02-generate-docs.yml
│   │   ├── 03-sync-docs-repo.yml
│   │   └── 04-deploy-docs.yml
│   └── scripts/
│       ├── feature-mapper.py
│       ├── claude-client.py
│       ├── generate-tech-docs.py
│       ├── generate-user-guides.py
│       └── update-changelog.py
├── docs/
│   ├── .ai-docs-config.yml
│   └── README.md
├── CHANGELOG.md
├── requirements-automation.txt
└── DOCUMENTATION_SETUP.md (this file)
```

## Next Steps

1. ✅ Add secrets to GitHub
2. ✅ Create docs repository
3. ✅ Configure `docs/.ai-docs-config.yml`
4. ✅ Push to main branch to test
5. ✅ Verify docs site is deployed

## Support

For issues with:
- **Anthropic API**: Check [Anthropic docs](https://docs.anthropic.com)
- **GitHub Actions**: Check [GitHub docs](https://docs.github.com/actions)
- **MkDocs**: Check [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
