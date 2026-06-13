# volcanic-profile-builder

Public-safe Hermes profile packaging assistant for scaffolding clean, installable, registry-ready Hermes profile distributions.

## Install

```bash
hermes profile install github.com/Freakazoid78tr/volcanic-profile-builder --name volcanic-profile-builder
```

## Run

```bash
hermes -p volcanic-profile-builder chat
```

One-shot example:

```bash
hermes -p volcanic-profile-builder chat -q "Help with the task this profile is designed for."
```

## Example tasks

- "Turn this agent idea into a clean Hermes profile repo layout."
- "Write a public-safe README, SOUL.md, config.yaml, and distribution.yaml for this profile."
- "Review this profile package before I submit it to Hermes Profiles."
- "Generate registry tags, category, and install instructions for my profile."

## Toolset rationale

This profile requests web access for public registry/docs research, terminal/file/code execution for scaffolding and validation, and skills for its bundled profile-building workflow. It does not request `all`, cron, messaging, wallet, or admin toolsets by default.

## Privacy note

Do not include private memories, session logs, API keys, auth files, internal business strategy, wallet data, or unreleased proprietary workflows in public profile packages.


## What is included

- `SOUL.md` — profile persona and operating principles.
- `config.yaml` — conservative non-secret Hermes defaults.
- `distribution.yaml` — installable profile distribution metadata.
- `profile.yaml` — short registry-facing profile metadata.
- `.env.EXAMPLE` — empty placeholder file; no secrets.
- `skills/` — bundled reusable workflows for this profile.
- `scripts/profile_secret_scan.py` — local scanner for common secrets/private state.
- `cron/README.md` — explicit note that no cron jobs are enabled by default.

## Validate before publishing

```bash
python3 scripts/profile_secret_scan.py .
hermes profile install github.com/Freakazoid78tr/volcanic-profile-builder --name volcanic-profile-builder-smoke -y
hermes profile show volcanic-profile-builder-smoke
hermes profile delete volcanic-profile-builder-smoke -y
```

## Branding/provenance

Published under the `Freakazoid78tr` GitHub account with `Volcanic` as the profile author/brand. This is a public-service profile, not a private Volcanic operating profile.

## License

MIT
