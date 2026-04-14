# Automated Documentation

This directory contains the configuration for the automated documentation pipeline.

## Structure

- `.ai-docs-config.yml` - Feature mapping configuration
- `generated/` - Auto-generated documentation (created by CI/CD)

## How It Works

1. **Code Changes** → Push to `main` branch triggers detection
2. **Feature Mapping** → `.ai-docs-config.yml` maps files to features
3. **AI Generation** → Claude generates/updates documentation
4. **Sync to Docs Repo** → Changes pushed to documentation repository
5. **Deployment** → Documentation site deployed to GitHub Pages

## Manual Trigger

You can manually trigger documentation generation:

```bash
# Run feature detection
python .github/scripts/feature-mapper.py \
  --changed-files changed_files.txt \
  --output report.json \
  --config docs/.ai-docs-config.yml
```

## Configuration

Edit `docs/.ai-docs-config.yml` to:
- Add new feature mappings
- Define feature descriptions
- Configure AI behavior
- Set sync targets

## Secrets Required

Configure these in GitHub repository settings:

- `ANTHROPIC_API_KEY` - API key for Claude AI
- `DOCS_REPO_TOKEN` - Personal Access Token for cross-repo access
