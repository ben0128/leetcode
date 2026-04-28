#!/usr/bin/env python3
"""Stop hook: warn if solutions/*.py changed but tracking files weren't.

Fires a systemMessage when git status shows dirty/new solutions/*.py
but review/schedule.md AND ANALYSIS.md are untouched.

Expected behavior: noisy during a practice session — each Stop prompts
"did you update tracking yet?" Silence yourself by updating the tracking
files, or disable the hook in .claude/settings.local.json if undesired.
"""
import os
import sys
import json
import subprocess

root = os.environ.get("CLAUDE_PROJECT_DIR", ".")

try:
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=5,
    )
except Exception:
    sys.exit(0)

if result.returncode != 0:
    sys.exit(0)

lines = [l for l in result.stdout.splitlines() if l.strip()]
# Porcelain format: first 2 chars = status, char 3 = space, rest = path
paths = [l[3:] for l in lines]

solutions_changed = any(
    p.startswith("solutions/") and p.endswith(".py") for p in paths
)
if not solutions_changed:
    sys.exit(0)

schedule_changed = any("review/schedule.md" in p for p in paths)
analysis_changed = any(p.endswith("ANALYSIS.md") for p in paths)

# Warn if EITHER tracking file is missing an update
if schedule_changed and analysis_changed:
    sys.exit(0)

missing = []
if not schedule_changed:
    missing.append("review/schedule.md")
if not analysis_changed:
    missing.append("ANALYSIS.md")

msg = f"⚠️ solutions/ 有變動但 {' 和 '.join(missing)} 未更新 — 記得跑進度追蹤（/practice 完題步驟 8 / schedule.md Update Protocol）"
print(json.dumps({"systemMessage": msg}, ensure_ascii=False))
