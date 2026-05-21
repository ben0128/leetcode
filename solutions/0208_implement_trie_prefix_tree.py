"""
LeetCode 208. Implement Trie (Prefix Tree)
Difficulty: Medium
Tags: Design
URL: https://leetcode.com/problems/implement-trie-prefix-tree/

Problem:
    A trie (pronounced as "try") or prefix tree is a tree data structure used to
    efficiently store and retrieve keys in a dataset of strings. There are
    various applications of this data structure, such as autocomplete and
    spellchecker.

    Implement the Trie class:

        - Trie() Initializes the trie object.
        - void insert(String word) Inserts the string word into the trie.
        - boolean search(String word) Returns true if the string word is in the
          trie (i.e., was inserted before), and false otherwise.
        - boolean startsWith(String prefix) Returns true if there is a
          previously inserted string word that has the prefix prefix, and false
          otherwise.

    Example 1:
        Input:
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
            [[],     ["apple"], ["apple"], ["app"], ["app"],      ["app"],   ["app"]]
        Output:
            [null,   null,      true,      false,   true,         null,      true]

        Explanation:
            Trie trie = new Trie();
            trie.insert("apple");
            trie.search("apple");     // return True
            trie.search("app");       // return False
            trie.startsWith("app");   // return True
            trie.insert("app");
            trie.search("app");       // return True

    Constraints:
        - 1 <= word.length, prefix.length <= 2000
        - word and prefix consist only of lowercase English letters.
        - At most 3 * 10^4 calls in total will be made to insert, search, and
          startsWith.

思路：
    build trie, let search more efficiently, use dict to build each layer
    and use maxWordLen to speed up search
    use '#' mark end of string

複雜度：
    Time:
        n = preflix length, m = word length
        insert: O(m)
        search: O(m)
        startsWith: O(n)
    Space: O(插入總字元數)
"""


class Trie:
    def __init__(self):
        self.trie = {}
        self.maxWordLen = 0

    def insert(self, word: str) -> None:
        head = self.trie
        self.maxWordLen = max(self.maxWordLen, len(word))
        for w in word:
            if w not in head:
                head[w] = {}
            head = head[w]
        head['#'] = True
        return 

    def search(self, word: str) -> bool:
        if len(word) > self.maxWordLen:
            return False
        head = self.trie
        for w in word:
            if w not in head:
                return False
            head = head[w]
        return '#' in head


    def startsWith(self, prefix: str) -> bool:
        if len(prefix) > self.maxWordLen:
            return False
        head = self.trie
        for w in prefix:
            if w not in head:
                return False
            head = head[w]
        return True


if __name__ == "__main__":
    # Case 1: LeetCode example
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True, "Case 1a: exact match"
    assert trie.search("app") is False, "Case 1b: prefix not inserted as word"
    assert trie.startsWith("app") is True, "Case 1c: prefix exists"
    trie.insert("app")
    assert trie.search("app") is True, "Case 1d: now app is a word"

    # Case 2: multiple words sharing prefix
    trie2 = Trie()
    trie2.insert("car")
    trie2.insert("card")
    trie2.insert("cards")
    assert trie2.search("car") is True, "Case 2a: shortest"
    assert trie2.search("card") is True, "Case 2b: middle"
    assert trie2.search("cards") is True, "Case 2c: longest"
    assert trie2.search("ca") is False, "Case 2d: prefix only"
    assert trie2.startsWith("ca") is True, "Case 2e: startsWith works"
    assert trie2.startsWith("cars") is False, "Case 2f: no such prefix"

    # Edge: empty-ish / single char
    trie3 = Trie()
    trie3.insert("a")
    assert trie3.search("a") is True, "Edge: single char word"
    assert trie3.startsWith("a") is True, "Edge: single char prefix"
    assert trie3.search("b") is False, "Edge: not inserted"

    print("All tests passed!")
