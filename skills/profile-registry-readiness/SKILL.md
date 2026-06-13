---
name: profile-registry-readiness
description: Check whether a Hermes profile distribution is ready for public registry submission.
version: 1.0.0
author: Volcanic
license: MIT
---

# Profile Registry Readiness

## Checklist

- Clear one-sentence purpose.
- README has install, run, update, examples, toolset rationale, and privacy/safety notes.
- SOUL/persona is concise and aligned with the stated job.
- `config.yaml` uses non-secret defaults and minimal toolsets.
- `distribution.yaml` includes name, version, description, author, license, Hermes requirement, env requirements, and owned files.
- `.env.EXAMPLE` contains empty placeholders only.
- `cron/README.md` explicitly states whether any cron jobs are enabled.
- No secrets, auth state, sessions, memories, logs, wallets, or private local state.
- Fresh-clone scanner passes.
- Install smoke test passes.

## Output Template

- Verdict:
- Score:
- Blocking fixes:
- Optional polish:
- Registry fields:
  - Repo URL:
  - Tags:
  - Category:
