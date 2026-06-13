---
name: profile-scaffolding
description: Scaffold clean Hermes profile distributions with README, SOUL, config, metadata, safety notes, and validation steps.
version: 1.0.0
author: Volcanic
license: MIT
---

# Profile Scaffolding

## When to Use

Use when turning an agent idea into a public or shareable Hermes profile distribution.

## Workflow

1. Define the profile's narrow job in one sentence.
2. Pick a neutral name and public-safe description.
3. Choose the minimum toolsets needed.
4. Draft core files:
   - `README.md`
   - `SOUL.md`
   - `config.yaml`
   - `distribution.yaml`
   - `profile.yaml`
   - `.env.EXAMPLE`
   - `cron/README.md`
   - optional `skills/`, `scripts/`, `templates/`
5. Add safety notes and toolset rationale.
6. Add `.gitignore` that blocks secrets/runtime state while allowing intentional scanner files.
7. Validate from a fresh clone before publishing.

## Quality Bar

A good public profile is understandable, installable, scoped, safe, and humble. It should not require the user to trust hidden state.
