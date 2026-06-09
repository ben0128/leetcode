# Google SWE 考古題題單

> 來源：LeetCode Discuss 2024-2026 firsthand 面經、Blind、Reddit、一畝三分地、snehasishroy/liquidslr 頻率資料（2026-05 snapshot）、LeetCode Company Tags、NeetCode Roadmap、Grind 75
> 更新日期：2026-06-08（workflow：6 源並行掃描 → 3 鏡頭對抗驗證 → 對照合成）
> 頻率標記：🔥🔥🔥 = 極高頻 / 🔥🔥 = 高頻 / 🔥 = 常見
>
> ⚠️ 策展注意（2026-06-08 驗證結論）：Discuss 6185127「2024 合集」是無日期 title index（混 2018-2024）；krishnadey `google_6months.csv` 是 2020 快照。**只**出現在這兩處的題目不構成「近期高頻」證據——未來更新時別被這類來源灌水。

---

## 📈 2024-2026 面試趨勢（2026-06-08，dated firsthand 面經驗證）

- **偽裝變體 > 原題**：onsite 題目包成現實故事（咖啡店選址 = multi-source BFS、F1 輪胎策略 = DP、cloud snapshot 刪除 = topo sort、10 秒 log 去重 = stream/window）。考的就是穿透故事做 pattern matching。
- **Follow-up 驅動**：一題基底 + 2-3 個遞進 follow-up（記憶體清理、O(n²)→O(n)、duplicates、rotation）；評的是**優化軌跡和對 hint 的反應**，不是第一版能跑。
- **Code quality 是明確 reject 理由**：2025-06 一位 L4 三題全對仍被 hold——「整坨塞一個 function、不模組化、可讀性差」。Bar = production-ready、every corner case、主動 walk through code；correct-but-slow → Lean Hire 也可能沉掉整個 loop。
- **Graph 是 table stakes**：multi-source BFS、Kahn's topo sort、Dijkstra 變體、connected components 幾乎每個 2024-2026 L4/L5 loop 都出現（但 arrays/strings 仍是最大桶 ~35%，graph ~25%——別偏科）。
- **Interval / line-sweep 反覆出現**：Range Module / My Calendar / Employee Free Time / Merge Intervals 一族，特別愛追問 **duplicates 和樣例沒給的 edge cases**。
- **String parsing / 遞迴運算式求值**仍是 phone screen 主力題型（45 分鐘、自選語言，評乾淨遞迴 + edge cases）。
- **Binary-search-on-answer（max-min/min-max）是上升 pattern**：#875、#410 出現在近 30 天頻率窗口。
- **L4 loop 形態**：~3 coding + 1 Googlyness，**L4 無 system design**（L5 才有）；每輪有效 coding ~37 分鐘；部分 loop 出現純數學/機率輪；Googlyness 有實際權重。
- **≥1 in-person round 回歸**（反 AI 作弊；Pichai 2025-02 town hall + 多家媒體確認）。2026 H2 起部分美國團隊試點 **AI-assisted code comprehension 輪**（用 Gemini 讀/debug/優化 codebase，評 prompt 與驗證能力）——firsthand 證據還薄，但過渡期兩種形式都要準備。

---

## 1. Array / Hashing

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 1 | Two Sum | E | 🔥🔥🔥 |
| 42 | Trapping Rain Water | H | 🔥🔥🔥 |
| 56 | Merge Intervals | M | 🔥🔥🔥 |
| 253 | Meeting Rooms II | M | 🔥🔥🔥 |
| 380 | Insert Delete GetRandom O(1) | M | 🔥🔥🔥 |
| 560 | Subarray Sum Equals K | M | 🔥🔥🔥 |
| 1146 | Snapshot Array | M | 🔥🔥🔥 |
| 41 | First Missing Positive | H | 🔥🔥 |
| 48 | Rotate Image | M | 🔥🔥 |
| 49 | Group Anagrams | M | 🔥🔥 |
| 54 | Spiral Matrix | M | 🔥🔥 |
| 57 | Insert Interval | M | 🔥🔥 |
| 128 | Longest Consecutive Sequence | M | 🔥🔥 |
| 238 | Product of Array Except Self | M | 🔥🔥 |
| 271 | Encode and Decode Strings | M | 🔥🔥 |
| 299 | Bulls and Cows | M | 🔥🔥 |
| 359 | Logger Rate Limiter | E | 🔥🔥 |
| 621 | Task Scheduler | M | 🔥🔥 |
| 904 | Fruit Into Baskets | M | 🔥🔥 |
| 939 | Minimum Area Rectangle | M | 🔥🔥 |

## 2. String

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 3 | Longest Substring Without Repeating Characters | M | 🔥🔥🔥 |
| 68 | Text Justification | H | 🔥🔥🔥 |
| 76 | Minimum Window Substring | H | 🔥🔥🔥 |
| 394 | Decode String | M | 🔥🔥🔥 |
| 844 | Backspace String Compare | E | 🔥🔥🔥 |
| 681 | Next Closest Time | M | 🔥（2018-2020 高頻，近年少見） |
| 809 | Expressive Words | M | 🔥（2018-2020 高頻，近年少見） |
| 929 | Unique Email Addresses | E | 🔥（太簡單，L4 不太會考） |
| 5 | Longest Palindromic Substring | M | 🔥🔥 |
| 10 | Regular Expression Matching | H | 🔥🔥 |
| 17 | Letter Combinations of a Phone Number | M | 🔥🔥 |
| 20 | Valid Parentheses | E | 🔥🔥 |
| 22 | Generate Parentheses | M | 🔥🔥 |
| 159 | Longest Substring with At Most Two Distinct Characters | M | 🔥🔥 |
| 340 | Longest Substring with At Most K Distinct Characters | M | 🔥🔥 |
| 443 | String Compression | M | 🔥🔥 |
| 468 | Validate IP Address | M | 🔥🔥 |
| 678 | Valid Parenthesis String | M | 🔥🔥 |
| 727 | Minimum Window Subsequence | H | 🔥🔥 |
| 1153 | String Transforms Into Another String | H | 🔥（2020 快照高頻，2025-26 未見） |

## 3. Two Pointers / Sliding Window

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 15 | 3Sum | M | 🔥🔥🔥 |
| 239 | Sliding Window Maximum | H | 🔥🔥🔥 |
| 283 | Move Zeroes | E | 🔥🔥🔥 |
| 11 | Container With Most Water | M | 🔥🔥🔥 |
| 209 | Minimum Size Subarray Sum | M | 🔥🔥 |
| 424 | Longest Repeating Character Replacement | M | 🔥🔥 |
| 567 | Permutation in String | M | 🔥🔥 |
| 713 | Subarray Product Less Than K | M | 🔥🔥 |
| 826 | Most Profit Assigning Work | M | 🔥🔥 |
| 986 | Interval List Intersections | M | 🔥🔥 |

## 4. Binary Search

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 4 | Median of Two Sorted Arrays | H | 🔥🔥🔥 |
| 33 | Search in Rotated Sorted Array | M | 🔥🔥🔥 |
| 162 | Find Peak Element | M | 🔥🔥🔥 |
| 528 | Random Pick with Weight | M | 🔥🔥🔥 |
| 34 | Find First and Last Position of Element in Sorted Array | M | 🔥🔥 |
| 153 | Find Minimum in Rotated Sorted Array | M | 🔥🔥 |
| 278 | First Bad Version | E | 🔥🔥 |
| 410 | Split Array Largest Sum | H | 🔥🔥 |
| 658 | Find K Closest Elements | M | 🔥🔥 |
| 702 | Search in a Sorted Array of Unknown Size | M | 🔥🔥 |
| 875 | Koko Eating Bananas | M | 🔥🔥 |
| 981 | Time Based Key-Value Store | M | 🔥🔥 |
| 1011 | Capacity to Ship Packages Within D Days | M | 🔥🔥 |
| 1060 | Missing Element in Sorted Array | M | 🔥🔥 |

## 5. Linked List

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 23 | Merge k Sorted Lists | H | 🔥🔥🔥 |
| 146 | LRU Cache | M | 🔥🔥🔥 |
| 2 | Add Two Numbers | M | 🔥🔥 |
| 21 | Merge Two Sorted Lists | E | 🔥🔥 |
| 25 | Reverse Nodes in k-Group | H | 🔥🔥 |
| 138 | Copy List with Random Pointer | M | 🔥🔥 |
| 141 | Linked List Cycle | E | 🔥🔥 |
| 206 | Reverse Linked List | E | 🔥🔥 |
| 460 | LFU Cache | H | 🔥🔥 |

## 6. Stack / Monotonic Stack

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 227 | Basic Calculator II | M | 🔥🔥🔥 |
| 341 | Flatten Nested List Iterator | M | 🔥🔥🔥 |
| 394 | Decode String | M | 🔥🔥🔥 |
| 84 | Largest Rectangle in Histogram | H | 🔥🔥 |
| 224 | Basic Calculator | H | 🔥🔥 |
| 316 | Remove Duplicate Letters | M | 🔥🔥 |
| 388 | Longest Absolute File Path | M | 🔥🔥 |
| 636 | Exclusive Time of Functions | M | 🔥🔥 |
| 739 | Daily Temperatures | M | 🔥🔥 |
| 895 | Maximum Frequency Stack | H | 🔥🔥 |

## 7. Tree (Binary Tree / BST)

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 98 | Validate Binary Search Tree | M | 🔥🔥🔥 |
| 124 | Binary Tree Maximum Path Sum | H | 🔥🔥🔥 |
| 236 | Lowest Common Ancestor of a Binary Tree | M | 🔥🔥🔥 |
| 297 | Serialize and Deserialize Binary Tree | H | 🔥🔥🔥 |
| 543 | Diameter of Binary Tree | E | 🔥🔥🔥 |
| 938 | Range Sum of BST | E | 🔥🔥🔥 |
| 951 | Flip Equivalent Binary Trees | M | 🔥🔥🔥 |
| 94 | Binary Tree Inorder Traversal | E | 🔥🔥 |
| 101 | Symmetric Tree | E | 🔥🔥 |
| 105 | Construct BT from Preorder and Inorder | M | 🔥🔥 |
| 114 | Flatten Binary Tree to Linked List | M | 🔥🔥 |
| 199 | Binary Tree Right Side View | M | 🔥🔥 |
| 222 | Count Complete Tree Nodes | M | 🔥🔥 |
| 230 | Kth Smallest Element in a BST | M | 🔥🔥 |
| 235 | Lowest Common Ancestor of a BST | M | 🔥🔥 |
| 270 | Closest Binary Search Tree Value | E | 🔥🔥 |
| 366 | Find Leaves of Binary Tree | M | 🔥🔥 |
| 652 | Find Duplicate Subtrees | M | 🔥🔥 |
| 863 | All Nodes Distance K in Binary Tree | M | 🔥🔥🔥 |

## 8. Heap / Priority Queue

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 253 | Meeting Rooms II | M | 🔥🔥🔥 |
| 295 | Find Median from Data Stream | H | 🔥🔥🔥 |
| 973 | K Closest Points to Origin | M | 🔥🔥🔥 |
| 215 | Kth Largest Element in an Array | M | 🔥🔥 |
| 347 | Top K Frequent Elements | M | 🔥🔥 |
| 373 | Find K Pairs with Smallest Sums | M | 🔥🔥 |
| 621 | Task Scheduler | M | 🔥🔥 |
| 767 | Reorganize String | M | 🔥🔥 |
| 1094 | Car Pooling | M | 🔥🔥 |
| 759 | Employee Free Time | H | 🔥🔥（interval-merge 族，2025 onsite 主題） |

## 9. Graph (BFS / DFS / Topological Sort)

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 127 | Word Ladder | H | 🔥🔥🔥 |
| 200 | Number of Islands | M | 🔥🔥🔥 |
| 207 | Course Schedule | M | 🔥🔥🔥 |
| 210 | Course Schedule II | M | 🔥🔥🔥（2025 firsthand：Kahn's topo+BFS；topo 是最穩定出現的 graph core） |
| 269 | Alien Dictionary | H | 🔥🔥🔥 |
| 329 | Longest Increasing Path in a Matrix | H | 🔥🔥🔥 |
| 399 | Evaluate Division | M | 🔥🔥🔥 |
| 721 | Accounts Merge | M | 🔥🔥🔥 |
| 863 | All Nodes Distance K in Binary Tree | M | 🔥🔥🔥 |
| 994 | Rotting Oranges | M | 🔥🔥🔥 |
| 778 | Swim in Rising Water | H | 🔥🔥🔥（2025 兩份 firsthand 變體：6701617、6846591） |
| 133 | Clone Graph | M | 🔥🔥 |
| 310 | Minimum Height Trees | M | 🔥🔥 |
| 332 | Reconstruct Itinerary | H | 🔥🔥 |
| 417 | Pacific Atlantic Water Flow | M | 🔥🔥 |
| 490 | The Maze | M | 🔥🔥 |
| 694 | Number of Distinct Islands | M | 🔥🔥 |
| 743 | Network Delay Time | M | 🔥🔥 |
| 785 | Is Graph Bipartite? | M | 🔥🔥 |
| 787 | Cheapest Flights Within K Stops | M | 🔥🔥 |
| 815 | Bus Routes | H | 🔥🔥 |
| 1091 | Shortest Path in Binary Matrix | M | 🔥🔥 |
| 2115 | Find All Possible Recipes from Given Supplies | M | 🔥🔥（disguised topo-sort 變體的代表原型） |

## 10. Union Find

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 721 | Accounts Merge | M | 🔥🔥🔥 |
| 128 | Longest Consecutive Sequence | M | 🔥🔥 |
| 261 | Graph Valid Tree | M | 🔥🔥 |
| 323 | Number of Connected Components | M | 🔥🔥 |
| 547 | Number of Provinces | M | 🔥🔥 |
| 684 | Redundant Connection | M | 🔥🔥 |
| 947 | Most Stones Removed with Same Row or Column | M | 🔥🔥 |
| 1135 | Connecting Cities With Minimum Cost | M | 🔥🔥 |

## 11. Dynamic Programming

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 72 | Edit Distance | M | 🔥🔥🔥 |
| 139 | Word Break | M | 🔥🔥🔥 |
| 300 | Longest Increasing Subsequence | M | 🔥🔥🔥 |
| 322 | Coin Change | M | 🔥🔥🔥 |
| 1235 | Maximum Profit in Job Scheduling | H | 🔥🔥🔥 |
| 5 | Longest Palindromic Substring | M | 🔥🔥 |
| 10 | Regular Expression Matching | H | 🔥🔥 |
| 44 | Wildcard Matching | H | 🔥🔥 |
| 53 | Maximum Subarray | M | 🔥🔥 |
| 64 | Minimum Path Sum | M | 🔥🔥 |
| 91 | Decode Ways | M | 🔥🔥 |
| 97 | Interleaving String | M | 🔥🔥 |
| 140 | Word Break II | H | 🔥🔥 |
| 152 | Maximum Product Subarray | M | 🔥🔥 |
| 312 | Burst Balloons | H | 🔥🔥 |
| 416 | Partition Equal Subset Sum | M | 🔥🔥 |
| 472 | Concatenated Words | H | 🔥🔥 |
| 518 | Coin Change II | M | 🔥🔥 |
| 688 | Knight Probability in Chessboard | M | 🔥🔥 |
| 1143 | Longest Common Subsequence | M | 🔥🔥 |
| 354 | Russian Doll Envelopes | H | 🔥（2024 L4 onsite 變體 box-stacking + rotation follow-up） |

## 12. Backtracking

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 79 | Word Search | M | 🔥🔥🔥 |
| 17 | Letter Combinations of a Phone Number | M | 🔥🔥 |
| 22 | Generate Parentheses | M | 🔥🔥 |
| 39 | Combination Sum | M | 🔥🔥 |
| 46 | Permutations | M | 🔥🔥 |
| 51 | N-Queens | H | 🔥🔥 |
| 78 | Subsets | M | 🔥🔥 |
| 93 | Restore IP Addresses | M | 🔥🔥 |
| 131 | Palindrome Partitioning | M | 🔥🔥 |
| 212 | Word Search II | H | 🔥🔥 |

## 13. Trie

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 208 | Implement Trie (Prefix Tree) | M | 🔥🔥🔥 |
| 642 | Design Search Autocomplete System | H | 🔥（2020 快照高頻，2025-26 窗口未見；Trie/Design 經典參考） |
| 211 | Design Add and Search Words Data Structure | M | 🔥🔥 |
| 212 | Word Search II | H | 🔥🔥 |
| 745 | Prefix and Suffix Search | H | 🔥🔥 |
| 1032 | Stream of Characters | H | 🔥🔥 |

## 14. Design

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 146 | LRU Cache | M | 🔥🔥🔥 |
| 295 | Find Median from Data Stream | H | 🔥🔥🔥 |
| 341 | Flatten Nested List Iterator | M | 🔥🔥🔥 |
| 380 | Insert Delete GetRandom O(1) | M | 🔥🔥🔥 |
| 588 | Design In-Memory File System | H | 🔥🔥🔥 |
| 642 | Design Search Autocomplete System | H | 🔥（2020 快照高頻，2025-26 窗口未見） |
| 1146 | Snapshot Array | M | 🔥🔥🔥 |
| 715 | Range Module | H | 🔥🔥（2025 兩份 firsthand：Mar onsite R2 + Oct Bangalore line-sweep） |
| 359 | Logger Rate Limiter | E | 🔥🔥 |
| 460 | LFU Cache | H | 🔥🔥 |
| 895 | Maximum Frequency Stack | H | 🔥🔥 |
| 1352 | Product of the Last K Numbers | M | 🔥🔥 |

## 15. Greedy

| # | 題目 | 難度 | 頻率 |
|---|------|------|------|
| 1235 | Maximum Profit in Job Scheduling | H | 🔥🔥🔥 |
| 45 | Jump Game II | M | 🔥🔥 |
| 134 | Gas Station | M | 🔥🔥 |
| 253 | Meeting Rooms II | M | 🔥🔥🔥 |
| 435 | Non-overlapping Intervals | M | 🔥🔥 |
| 452 | Minimum Number of Arrows to Burst Balloons | M | 🔥🔥 |
| 621 | Task Scheduler | M | 🔥🔥 |
| 763 | Partition Labels | M | 🔥🔥 |

---

## 🎯 最高優先未完成題目（🔥🔥🔥 且未做過）

> 已於 2026-06-08 重新驗證並對齊（6 源 workflow 掃描 + 3 鏡頭驗證；剔除已完成：#127 #162 #236 #394 #721 #863 #1235；#642 因降級移出；#210 新升 🔥🔥🔥 但已完成、#778 新進 🔥🔥🔥 但已在 NeetCode 做過）

| # | 題目 | 主題 | 難度 |
|---|------|------|------|
| 4 | Median of Two Sorted Arrays | Binary Search | H |
| 68 | Text Justification | String | H |
| 283 | Move Zeroes | Two Pointers | E |
| 341 | Flatten Nested List Iterator | Stack/Design | M |
| 380 | Insert Delete GetRandom O(1) | Design | M |
| 399 | Evaluate Division | Graph/UF | M |
| 528 | Random Pick with Weight | Binary Search | M |
| 588 | Design In-Memory File System | Design | H |
| 844 | Backspace String Compare | String/Stack | E |
| 938 | Range Sum of BST | Tree | E |
| 951 | Flip Equivalent Binary Trees | Tree | M |
| 1146 | Snapshot Array | Design | M |

> 次優先（本次新進 🔥🔥、未做過、貼合 2025-26 interval/topo 趨勢）：#715 Range Module、#759 Employee Free Time、#2115 Find All Possible Recipes
