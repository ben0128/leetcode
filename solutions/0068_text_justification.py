"""
LeetCode 68. Text Justification
Difficulty: Hard
Tags: Array, String
URL: https://leetcode.com/problems/text-justification/

Problem:
    Given an array of strings `words` and a width `maxWidth`, format the text
    such that each line has exactly `maxWidth` characters and is fully (left
    and right) justified.

    You should pack your words in a greedy approach; that is, pack as many
    words as you can in each line. Pad extra spaces ' ' when necessary so that
    each line has exactly `maxWidth` characters.

    Extra spaces between words should be distributed as evenly as possible. If
    the number of spaces on a line does not divide evenly between words, the
    empty slots on the left will be assigned more spaces than the slots on the
    right.

    For the last line of text, it should be left-justified, and no extra space
    is inserted between words.

    Note:
        - A word is defined as a character sequence consisting of non-space
          characters only.
        - Each word's length is guaranteed to be greater than 0 and not exceed
          maxWidth.
        - The input array `words` contains at least one word.

    Example 1:
        Input: words = ["This", "is", "an", "example", "of", "text",
                        "justification."], maxWidth = 16
        Output:
        [
           "This    is    an",
           "example  of text",
           "justification.  "
        ]

    Example 2:
        Input: words = ["What","must","be","acknowledgment","shall","be"],
               maxWidth = 16
        Output:
        [
          "What   must   be",
          "acknowledgment  ",
          "shall be        "
        ]
        Explanation: Note that the last line is "shall be " instead of
        "shall be", because the last line must be left-justified instead of
        fully-justified. Note that the second line is also left-justified
        because it contains only one word.

    Example 3:
        Input: words = ["Science","is","what","we","understand","well",
                        "enough","to","explain","to","a","computer.","Art",
                        "is","everything","else","we","do"], maxWidth = 20
        Output:
        [
          "Science  is  what we",
          "understand      well",
          "enough to explain to",
          "a  computer.  Art is",
          "everything  else  we",
          "do                  "
        ]

    Constraints:
        - 1 <= words.length <= 300
        - 1 <= words[i].length <= 20
        - words[i] consists of only English letters and symbols.
        - 1 <= maxWidth <= 100
        - words[i].length <= maxWidth

思路：
    這題的重點在判斷何時需要left justify(如果是最後一行或是這行只有一個字) 何時需要 justify(單行多字)

複雜度：
    Time: O(maxWidth*行數)
    Space: O(maxWidth) 不考慮ans, 考慮ans => O(maxWidth*行數)
"""

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        tmp = [0]
        tmpWordLen = len(words[0]) # no space
        ans = []
        def _justify(currList):
            currLine = words[currList[0]]
            lastSpace = maxWidth - tmpWordLen
            baseSpace = ' ' * (lastSpace // (len(currList)-1))
            needOneMore = lastSpace % (len(currList)-1)
            for idx in range(1, len(currList)):
                currLine += baseSpace+ (' ' if needOneMore > 0 else '')+words[currList[idx]]
                needOneMore -= 1
            return currLine

        def _left_justify(currList):
            currLine = words[currList[0]]
            for idx in range(1, len(currList)):
                currLine += ' '+words[currList[idx]]
            
            currLine += ' '*(maxWidth-len(currLine))
            return currLine

        for i in range(1, n):
            currWordLen = len(words[i])
            # if push currWord inside:
            if currWordLen + tmpWordLen + len(tmp) > maxWidth:
                if len(tmp) != 1:
                    ans.append(_justify(tmp))
                else:
                    ans.append(_left_justify(tmp))
                tmp, tmpWordLen = [], 0
            
            tmp.append(i)
            tmpWordLen += currWordLen
        
        ans.append(_left_justify(tmp))
        return ans



if __name__ == "__main__":
    s = Solution()

    assert s.fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."], 16
    ) == [
        "This    is    an",
        "example  of text",
        "justification.  ",
    ], "Case 1"

    assert s.fullJustify(
        ["What", "must", "be", "acknowledgment", "shall", "be"], 16
    ) == [
        "What   must   be",
        "acknowledgment  ",
        "shall be        ",
    ], "Case 2"

    assert s.fullJustify(
        ["Science", "is", "what", "we", "understand", "well", "enough", "to",
         "explain", "to", "a", "computer.", "Art", "is", "everything", "else",
         "we", "do"], 20
    ) == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ], "Case 3"

    # Edge case: single word shorter than maxWidth -> left-justified, padded
    assert s.fullJustify(["hello"], 10) == ["hello     "], "Edge: single word"

    print("All tests passed!")
