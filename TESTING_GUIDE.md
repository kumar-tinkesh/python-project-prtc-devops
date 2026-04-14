# Testing the Documentation Automation Pipeline

Step-by-step instructions to test the complete flow from PR merge → documentation update.

## Table of Contents
1. [Local Testing (Before GitHub)](#local-testing)
2. [GitHub Actions Testing](#github-actions-testing)
3. [End-to-End Test](#end-to-end-test)
4. [Troubleshooting](#troubleshooting)

---

## Local Testing

Test scripts locally before pushing to GitHub.

### Step 1: Install Dependencies

```bash
cd /Users/macbook/Desktop/Python-Projects
pip install -r requirements-automation.txt
```

### Step 2: Test Feature Detection

Create a test file with changed files:

```bash
# Create test file list
cat > /tmp/test_changed_files.txt << 'EOF'
weatherData/app.py
weatherData/config.ini
weatherData/templates/index.html
EOF

# Run feature detection
python .github/scripts/feature-mapper.py \
  --changed-files /tmp/test_changed_files.txt \
  --output /tmp/test_report.json \
  --config docs/.ai-docs-config.yml

# View results
cat /tmp/test_report.json | jq .
```

**Expected Output:**
```json
{
  "affected_features": [
    {
      "id": "weather-app",
      "name": "Weather Dashboard App",
      "files": ["weatherData/app.py", "weatherData/config.ini", "weatherData/templates/index.html"],
      "priority": "medium",
      "doc_path": "docs/features/weather-app.md"
    },
    {
      "id": "flask-apps",
      "name": "Flask Applications Collection",
      "files": [...]
    }
  ],
  "total_files_changed": 3,
  "unmapped_files": [],
  "multi_feature_pr": false
}
```

### Step 3: Test AI Documentation Generation (Requires API Key)

```bash
# Set your Anthropic API key
export ANTHROPIC_API_KEY="sk-ant-..."

# Test with the report from Step 2
python .github/scripts/generate-tech-docs.py \
  --report /tmp/test_report.json \
  --output docs/generated \
  --config docs/.ai-docs-config.yml

# Check generated content
ls -la docs/generated/features/
cat docs/generated/features/weather-app.md
```

---

## GitHub Actions Testing

### Method 1: Manual Workflow Trigger (Recommended)

Test workflows without merging code:

1. **Go to GitHub → Actions → "01 - Feature Detection & Analysis"**

2. **Click "Run workflow" button**
   - Select branch: `main`
   - Test mode: `true` (optional)
   - Click "Run workflow"

3. **Check the results:**
   - Click on the workflow run
   - View logs for each step
   - Check the "Summary" section for the report

### Method 2: Create Test Branch & PR

Test the full merge flow:

```bash
# 1. Create a test branch
git checkout -b test/docs-automation

# 2. Make a small change to trigger detection
echo "# Test comment" >> weatherData/app.py

# 3. Commit and push
git add weatherData/app.py
git commit -m "test: Trigger docs automation for weather app"
git push origin test/docs-automation

# 4. Create PR on GitHub
# Go to GitHub → Pull requests → New PR
# Base: main, Compare: test/docs-automation
# Title: "TEST: Documentation automation"
# Click "Create pull request"

# 5. Merge the PR
# Click "Merge pull request"
# This triggers the automation!

# 6. Watch the automation run
# Go to Actions tab
# You'll see 3 workflows run sequentially:
# - 01-detect-features.yml
# - 02-generate-docs.yml  
# - 03-sync-docs-repo.yml
```

### Method 3: Test with Dummy File

Create a minimal change that won't affect your projects:

```bash
# Add a comment to trigger detection
git checkout main
git checkout -b test/minimal-change

# Just add a comment to a tracked file
echo "# Automated documentation test - $(date)" >> README.md

git add README.md
git commit -m "docs: Test automation pipeline"
git push origin test/minimal-change

# Create PR and merge
```

---

## End-to-End Test

Complete verification of the entire pipeline.

### Prerequisites Checklist

Before testing, verify:

- [ ] `ANTHROPIC_API_KEY` secret added to GitHub
- [ ] `DOCS_REPO_TOKEN` secret added to GitHub
- [ ] Docs repository exists (e.g., `python-projects-docs`)
- [ ] Docs repo has `mkdocs.yml` configured
- [ ] GitHub Pages enabled on docs repo

### Full Pipeline Test

```bash
# 1. Create test feature branch
git checkout -b feature/test-weather-update

# 2. Modify a project file (weather app example)
cat >> weatherData/app.py << 'EOF'

# NEW_FEATURE: Added temperature unit toggle
# This demonstrates a new feature for documentation testing
def toggle_unit():
    """Toggle between Celsius and Fahrenheit."""
    return "Feature added for doc automation test"
EOF

# 3. Commit with semantic message
git add weatherData/app.py
git commit -m "feat(weather): Add temperature unit toggle

- Added toggle_unit() function
- Supports Celsius and Fahrenheit
- Updated UI components"

git push origin feature/test-weather-update
```

4. **Create PR on GitHub:**
   - Go to your repo on GitHub
   - Click "Compare & pull request"
   - Title: `feat(weather): Add temperature unit toggle`
   - Description: "Testing documentation automation"
   - Create PR

5. **Merge the PR:**
   - Click "Merge pull request"
   - Confirm merge

6. **Monitor the pipeline:**
   - Go to Actions tab immediately
   - You'll see:
     
     **01 - Feature Detection (Running)**
     ```
     ✓ Checkout code
     ✓ Get changed files
     ✓ Run feature detection
     → Output: Detected 2 features: weather-app, flask-apps
     ```
     
     **02 - AI Documentation Generation (Queued)**
     ```
     → Waiting for 01 to complete
     ```
     
     **03 - Sync to Docs Repo (Queued)**
     ```
     → Waiting for 02 to complete
     ```

7. **Verify Results:**

   Check each workflow:
   
   - **01-detect-features:** Should show "2 features affected"
   - **02-generate-docs:** Should show "Generated: docs/generated/features/weather-app.md"
   - **03-sync-docs-repo:** Should show "PR created successfully"

8. **Check the Docs PR:**
   - Go to your docs repository
   - Click Pull requests
   - You should see: "docs: Automated update from python-projects"
   - Click the PR to review changes

9. **Merge Docs PR:**
   - Review the auto-generated documentation
   - Click "Merge pull request"
   - This triggers deployment to GitHub Pages

10. **Verify Live Documentation:**
    - Go to docs repo → Actions
    - Wait for "Deploy Documentation" to complete
    - Visit: `https://yourusername.github.io/python-projects-docs`
    - Check that weather-app documentation is updated

---

## Expected Timeline

| Stage | Duration | What Happens |
|-------|----------|--------------|
| 01-detect-features | 30 seconds | Maps changed files to features |
| 02-generate-docs | 30-60 seconds | Claude AI generates documentation |
| 03-sync-docs-repo | 20 seconds | Creates PR in docs repo |
| Manual Review | User decides | You review and merge the docs PR |
| Deploy to Pages | 1-2 minutes | GitHub Pages builds and deploys |

**Total Time:** ~5-10 minutes (plus your review time)

---

## Verification Commands

Check pipeline status from command line:

```bash
# Check recent workflow runs
gh run list --limit 5

# View specific workflow
gh run view <run-id>

# Check if docs PR was created
gh pr list --repo YOUR_USERNAME/python-projects-docs

# View docs PR
gh pr view <pr-number> --repo YOUR_USERNAME/python-projects-docs
```

---

## Troubleshooting

### Issue: Workflow Not Triggering

**Check:**
```bash
# Is the file in .ai-docs-config.yml patterns?
grep "weatherData" docs/.ai-docs-config.yml

# Is the workflow file valid?
gh workflow view "01 - Feature Detection & Analysis"
```

**Fix:**
- Ensure file paths in PR match the glob patterns
- Check Actions tab for any YAML syntax errors

### Issue: "ANTHROPIC_API_KEY not found"

**Check:**
```bash
# Verify secret exists (won't show value)
gh secret list
```

**Fix:**
1. Go to GitHub → Settings → Secrets → Actions
2. Add `ANTHROPIC_API_KEY` with your key
3. Re-run the workflow

### Issue: Docs Repo Sync Fails

**Check:**
```bash
# Verify token has repo access
curl -H "Authorization: token $DOCS_REPO_TOKEN" \
  https://api.github.com/user
```

**Fix:**
1. Create new PAT with `repo` and `workflow` scopes
2. Update `DOCS_REPO_TOKEN` secret
3. Ensure docs repo exists and is accessible

### Issue: No Features Detected

**Debug locally:**
```bash
python .github/scripts/feature-mapper.py \
  --changed-files <(echo "your/file/path.py") \
  --output /tmp/debug.json \
  --config docs/.ai-docs-config.yml

cat /tmp/debug.json
```

**Common fixes:**
- Add missing file patterns to `.ai-docs-config.yml`
- Ensure glob patterns match (e.g., `**/filename.py`)
- Check that features are defined in config

---

## Quick Test Checklist

Use this checklist when testing:

- [ ] Create test branch with code change
- [ ] Push to GitHub
- [ ] Create PR
- [ ] Merge PR to main
- [ ] Check Actions tab for running workflows
- [ ] Verify 01-detect-features completes successfully
- [ ] Verify 02-generate-docs creates documentation
- [ ] Verify 03-sync-docs-repo creates PR in docs repo
- [ ] Review and merge docs PR
- [ ] Verify GitHub Pages deployment
- [ ] Check live documentation site

---

## Next Steps After Testing

Once testing is successful:

1. **Clean up test branches:**
   ```bash
   git branch -D feature/test-weather-update
   git push origin --delete feature/test-weather-update
   ```

2. **Set up branch protection:**
   - Go to Settings → Branches
   - Protect `main`: require PR reviews
   - Protect docs repo `main`: require PR reviews

3. **Monitor ongoing:**
   - Watch first few real PRs closely
   - Check Actions tab regularly
   - Review AI-generated docs for accuracy

**You're ready to use the automation!**
