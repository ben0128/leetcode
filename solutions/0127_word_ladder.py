"""
LeetCode 127. Word Ladder
Difficulty: Hard
Tags: Graph, BFS, Hash Table
URL: https://leetcode.com/problems/word-ladder/

Problem:
    A transformation sequence from word `beginWord` to word `endWord` using a dictionary
    `wordList` is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
      1. Every adjacent pair of words differs by a single letter.
      2. Every si (for 1 <= i <= k) is in wordList. Note that beginWord does not need to be in wordList.
      3. sk == endWord

    Given two words beginWord and endWord, and a dictionary wordList, return the number
    of words in the shortest transformation sequence from beginWord to endWord, or 0 if
    no such sequence exists.

    Example 1:
        Input:  beginWord = "hit", endWord = "cog",
                wordList  = ["hot","dot","dog","lot","log","cog"]
        Output: 5
        Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
                     which is 5 words long.

    Example 2:
        Input:  beginWord = "hit", endWord = "cog",
                wordList  = ["hot","dot","dog","lot","log"]
        Output: 0
        Explanation: endWord "cog" is not in wordList, so no valid transformation exists.

    Constraints:
        - 1 <= beginWord.length <= 10
        - endWord.length == beginWord.length
        - 1 <= wordList.length <= 5000
        - wordList[i].length == beginWord.length
        - beginWord, endWord, and wordList[i] consist of lowercase English letters only.
        - beginWord != endWord
        - All words in wordList are unique.

思路：
    先透過 Dictionary 建立查詢字，方便日後查找，再使用 BFS 逐一討論，並逐層疊加。

複雜度：
    Time: O(m*(n^2))
    Space: O(m*n) m = wordList長度, n = 單個字串長 可以產出n種wildWord
"""
from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                wordSet[word[:i] + '*' + word[i+1:]].append(word)

        count = 1
        tmp = deque([beginWord])
        visited = set()
        
        while tmp:
            n = len(tmp)
            for _ in range(n):
                popWord = tmp.popleft()
                if popWord == endWord:
                    return count
                for i, c in enumerate(popWord):
                    wild = popWord[:i] + '*' + popWord[i+1:]
                    
                    for candi in wordSet[wild]:
                        if candi in visited:
                            continue
                        visited.add(candi)
                        tmp.append(candi)
            count += 1
        return 0


if __name__ == "__main__":
    s = Solution()

    # Case 1: 標準最短路徑
    assert s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5, "Case 1"

    # Case 2: endWord 不在 wordList
    assert s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0, "Case 2"

    # Case 3: 一步到位
    assert s.ladderLength("a", "c", ["a", "b", "c"]) == 2, "Case 3: single letter"

    # Case 4: beginWord 剛好等於某個 wordList 元素（但仍需變換）
    assert s.ladderLength("hot", "dog", ["hot", "dog"]) == 0, "Case 4: no intermediate"

    # Case 5: 較大範例確認
    assert s.ladderLength("hot", "dog", ["hot", "dog", "dot"]) == 3, "Case 5"

    print("All tests passed!")
