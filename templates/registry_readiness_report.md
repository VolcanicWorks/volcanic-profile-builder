# Hermes Profile Registry Readiness Report

## Verdict

## Score

## What this profile does

## Files inspected

## Safety checks
- Secrets/private state:
- Toolsets:
- Cron/background behavior:
- MCP/external services:
- Installability:

## Blocking fixes

## Optional polish

## Registry submission fields
- Repo URL:
- Tags:
- Category:

## Verification commands

```bash
python3 scripts/profile_secret_scan.py .
hermes profile install github.com/OWNER/REPO --name REPO-smoke -y
hermes profile show REPO-smoke
hermes profile delete REPO-smoke -y
```
