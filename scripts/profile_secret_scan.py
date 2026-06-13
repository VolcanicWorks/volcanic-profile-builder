#!/usr/bin/env python3
"""Small public-repo scanner for common secrets and private Hermes state."""
from __future__ import annotations
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
if not root.exists():
    print(f'Path does not exist: {root}', file=sys.stderr)
    sys.exit(2)

skip_dirs = {'.git', '.venv', 'venv', 'node_modules', '__pycache__', '.pytest_cache', '.mypy_cache'}
private_names = {
    '.env', 'auth.json', 'state.db', 'sessions.db', 'memory.db', 'memories.json',
    'wallet.json', 'keystore.json', 'credentials.json', 'token.json', 'cookies.txt',
}
private_parts = {'sessions', 'memories', 'logs', 'runtime', 'wallets', 'keystores', 'private'}
secret_patterns = [
    re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC |DSA |PGP )?PRIVATE KEY-----'),
    re.compile(r'(?i)(api[_-]?key|secret|token|password|mnemonic|private[_-]?key)\s*[:=]\s*["\']?[^"\'\s]{12,}'),
    re.compile(r'ghp_[A-Za-z0-9_]{20,}'),
    re.compile(r'github_pat_[A-Za-z0-9_]{20,}'),
    re.compile(r'sk-[A-Za-z0-9]{20,}'),
]
problems = []
for p in root.rglob('*'):
    rel = p.relative_to(root)
    if any(part in skip_dirs for part in rel.parts):
        continue
    lower_parts = {part.lower() for part in rel.parts}
    if p.name in private_names:
        problems.append(f'private filename present: {rel}')
    if lower_parts & private_parts:
        if not (p.is_file() and str(rel).lower().endswith('cron/readme.md')):
            problems.append(f'private/runtime path present: {rel}')
    if p.is_file():
        try:
            text = p.read_text(errors='ignore')
        except Exception:
            continue
        for pat in secret_patterns:
            if pat.search(text):
                if p.name.lower() in {'.env.example', '.env_example', '.env-example'}:
                    continue
                problems.append(f'possible secret pattern in: {rel}')
                break
if problems:
    print('Secret/private-state scan failed:')
    for item in sorted(set(problems)):
        print(f'- {item}')
    sys.exit(1)
print(f'Secret/private-state scan passed: {root}')
