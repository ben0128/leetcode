#!/usr/bin/env python3
"""SessionStart hook: surface today's due SR items from review/schedule.md.

A row in the Active table is due if column 8 (下次日期) is YYYY-MM-DD <= today.
Output JSON with systemMessage (shown to user) + additionalContext (injected to model).
"""
import os
import re
import sys
import json
import datetime

today = datetime.date.today().isoformat()
root = os.environ.get("CLAUDE_PROJECT_DIR", ".")
path = os.path.join(root, "review", "schedule.md")

if not os.path.exists(path):
    sys.exit(0)

due = []
in_active = False
with open(path, encoding="utf-8") as f:
    for line in f:
        if line.startswith("## Active"):
            in_active = True
            continue
        if in_active and line.startswith("## "):
            break
        if not in_active or not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 8 or not cols[0].isdigit():
            continue
        date_col = cols[7]
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date_col) and date_col <= today:
            due.append(f"  • #{cols[0]} {cols[1]} — due {date_col} (stage {cols[6]})")

if not due:
    sys.exit(0)

msg = f"📚 今日 SR due（{len(due)} 題，/practice 可挑這些做）:\n" + "\n".join(due)
print(json.dumps({
    "systemMessage": msg,
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": msg,
    },
}, ensure_ascii=False))
