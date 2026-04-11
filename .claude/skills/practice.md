---
name: practice
description: Start tutor-guided LeetCode practice on a specific problem
user_invocable: true
---

Start a practice session following the "模式二：練習模式（Practice）" flow defined in CLAUDE.md.

The user's argument is the problem they want to work on: $ARGUMENTS

If no problem is specified, ask the user which problem they'd like to practice.

Begin by pulling the latest neetcode-submissions, then check if the user has solved this problem before. If so, mention it and ask if they want to try a different approach or re-solve from scratch.
