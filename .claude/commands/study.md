---
name: study
description: Generate a 5-problem study plan based on weakness analysis
user_invocable: true
---

Generate a focused 5-problem study plan for Google SWE L4 prep.

Optional argument for topic focus: $ARGUMENTS

## Steps

1. **讀取歷史紀錄並校正熟練度表**
   - Read `./ANALYSIS.md` — 關注「主題熟練度總表」（量化等級）為主，「質性分析」僅供備註參考
   - Read all existing files in `./study/` to determine the next plan number and avoid repeating already-completed problems
   - Read `./review/schedule.md` Active table — identify items where `下次日期 ≤ 今天`（= due SR revisits）
   - Execute `git -C ../neetcode-submissions pull` to get latest submissions
   - **校正熟練度表**：若近期 `study/plan_*.md` 或 `review/schedule.md` 中有結果未反映到 ANALYSIS 熟練度表（題數未 +1、最近 2 題未更新、等級需重算），先修正該表再設計計畫

2. **快速複習（如果有之前的 notes）**
   - 掃描 `./notes/` 裡的筆記，挑 1-2 個跟本次計畫主題相關的「複習時問自己」問題抽問學生
   - 確認上次學的概念還記得，再開始新的計畫

3. **設計 5 題計畫**，遵守以下規則：

### Plan Design — 題目組成（5 題固定結構）
- **2 題 weak**：從 `ANALYSIS.md` 的「主題熟練度總表」中挑 `等級 ∈ {weak}` 的主題，再選具體題目
  - 若多個 weak 主題可選 → 優先選**最近計畫中沒出現過的**（配合 interleaving）
  - 具體題目優先從 `GOOGLE_QUESTIONS.md` 該主題分類下挑選（若無則 NeetCode / LeetCode pattern 常見題）
- **1 題 review (SR)**：從 `review/schedule.md` Active 表中選一個 due 的項目（`下次日期 ≤ 今天`）；有多項則取最早 due 的。複習題以**原題**出現，不換題（間隔重複的核心就是重做同一題）。若當天無 due 項目 → fallback：從 `study/` 歷史 ⚠️ 題目挑同主題變體題
- **1 題 Google 校準**：從 `GOOGLE_QUESTIONS.md` 挑一題未做過的 🔥🔥🔥，維持對當前 Google 題風的敏感度
- **1 題 wildcard**：優先挑 `等級 = gap` 的主題做新主題暖身；若所有 gap 主題本輪不適合（例如 Google 低頻的 Segment Tree / Math），改為 hard 挑戰

### Plan Design — 難度與去重
- **難度分布**：至少 3 題 medium、至少 1 題 hard
- **不重複**：不出 `study/` 中已做過的**同一題**；⚠️ 題目出同主題的**不同題**，不重做原題

### Plan Design — Interleaving（反 blocked practice）
研究證據：blocked practice（連續練同主題）會造成假熟練；interleaving 可提升 retention ~75%。
- 單份計畫內，**同主題不可連續出現 2 題**（強迫 pattern 切換）
- 連續 2 份計畫，**同主題佔比 ≤ 40%**（5 題中最多 2 題）— 檢查最新 1 份 `study/plan_*.md`

### Plan Design — weak vs 🔥🔥🔥 衝突處理
- 弱項 ∩ Google 高頻（DP/Graph/Heap/Union Find）→ 直接優先選，不衝突
- 弱項 ∩ Google 低頻（segment tree、math 等）→ 單主題歷史總量 cap 在 5 題，不追求完美
- 非弱項 🔥🔥🔥 → 靠上述「1 題 Google 校準」槽位吸收
- 最後衝刺階段（距面試 < 3 週）再把比例偏向 🔥🔥🔥（此階段規則之後會另外定義）

### If user specifies a topic
- 5 題中 3 題偏重該主題（取代 2 題 weak + 1 題 review 的部分）
- 仍需遵守 interleaving（同主題不連續）與難度分布

4. **輸出計畫**，格式如下：

```
## 讀書計畫 #{number} — {YYYY-MM-DD}
主題重點：{focus areas}

| # | 題目 | 難度 | 主題 | 為什麼選這題 |
|---|------|------|------|-------------|
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |

建議順序：先做 #{n}（暖身）→ #{n} → #{n} → #{n} → #{n}（挑戰）
預估總時間：{X} 小時
```

5. **存檔到 `study/plan_{nn}_{YYYY-MM-DD}.md`**
   - 包含計畫內容和進度追蹤表格（初始狀態全部為 `—`）
   - 編號接續 `study/` 資料夾中最大的編號

6. **問學生要從哪題開始**，然後以 `/practice` 助教模式引導該題：
   - Create the solution file using the template and naming convention from `/practice`
   - File location: `solutions/` (difficulty noted in the docstring)
   - Filename: `{number}_{snake_case_title}.py`
   - Follow the full practice flow (approach discussion → coding → optimize → teach back → follow-up → timing)
   - After solving, commit the solution file

7. **每完成一題，立即更新兩個檔案**：
   - `study/plan_{nn}_{YYYY-MM-DD}.md` 的進度欄位：
     - 結果：✅ = 獨立解出最優解 / ⚠️ = 需要提示或非最優 / ❌ = 無法解出
     - 花費時間（實際分鐘數）
     - 筆記（掙扎點或收穫）
   - `review/schedule.md` 依 Update Protocol 維護：
     - **新題**（不在 Active 中）：符合「排程納入規則」（⚠️/❌/Hard ✅/新主題 ✅）→ append 到 Active，階段=2d，下次日期=今天+2
     - **SR 複習題**（原本在 Active 中）：依本次結果（✅→進階段 / ⚠️→維持 / ❌→重置 2d）更新該列；若從 32d ✅ 通過 → 移到 Mastered 區塊

8. **全部 5 題完成後**，append 摘要到 `./ANALYSIS.md` 的「讀書計畫紀錄」section：

```
### Plan #{number} — {YYYY-MM-DD}
主題重點：{focus areas}

| # | 題目 | 結果 | 花費時間 | 筆記 |
|---|------|------|----------|------|
| 1 | ... | ✅/⚠️/❌ | ... | ... |
| 2 | ... | ... | ... | ... |

**整體觀察：** {patterns noticed, improvements, recurring issues}
**下次建議加強：** {topics to focus next}
```
