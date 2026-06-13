"""
LeetCode 127. Word Ladder
Difficulty: Hard
Tags: String
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
    我會用 Graph，並用 BFS 求最短路徑, 因為 BFS 每走一層就計一，這樣子的層數就等於答案, 又因為每個位置最多隻有 26 個字母而已，所以可以直接 for loop 26 個字母，看哪個位置當前有字。可以從兩邊分別做 BFS                                              
  去做查找，這樣子的空間複雜度和時間複雜度會更小。 
    當字串入 queue 的時候，就要順便做 mark，避免重複添加。

複雜度：
    m = len(wordList), n = len(beginWord)
    Time: O(len(wordList) * 10 * 26 * 10)
    Space: O(m*n)
"""
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        tmp = deque([beginWord])
        visited = set([beginWord])
        wordSet = set(wordList)
        n = len(beginWord)
        count = 0
        while tmp:
            m = len(tmp)
            count += 1
            for k in range(m):
                popWord = tmp.popleft()
                for i in range(n): # 最多10
                    for char in 'abcdefghijklmnopqrstuvwxyz': # 26 種
                        newWord = popWord[:i]+char+popWord[i+1:] # 最差就是 分割長度為10的word 
                        if newWord in wordSet and newWord not in visited:
                            visited.add(newWord)
                            if newWord == endWord:
                                return count + 1
                            tmp.append(newWord)
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
    # Case 6: 兩條路可以走
    assert s.ladderLength("hot", "ooo", ["oot", "hoo", "ooo"]) == 3, "two row can arrive endList"
    print("All tests passed!")
