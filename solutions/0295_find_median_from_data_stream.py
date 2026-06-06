"""
LeetCode 295. Find Median from Data Stream
Difficulty: Hard
Tags: Heap, Design
URL: https://leetcode.com/problems/find-median-from-data-stream/

Problem:
    The median is the middle value in an ordered integer list. If the size of
    the list is even, there is no middle value, and the median is the mean of
    the two middle values.
        - For arr = [2,3,4], the median is 3.
        - For arr = [2,3],   the median is (2 + 3) / 2 = 2.5.

    Implement the MedianFinder class:
        - MedianFinder()            initializes the object.
        - void   addNum(int num)    adds the integer num from the data stream.
        - double findMedian()       returns the median of all elements so far.
                                    Answers within 1e-5 of the actual answer
                                    are accepted.

    Example 1:
        Input:
            ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
            [[], [1], [2], [], [3], []]
        Output:
            [null, null, null, 1.5, null, 2.0]
        Explanation:
            MedianFinder mf = new MedianFinder();
            mf.addNum(1);      // arr = [1]
            mf.addNum(2);      // arr = [1, 2]
            mf.findMedian();   // return 1.5  ((1 + 2) / 2)
            mf.addNum(3);      // arr = [1, 2, 3]
            mf.findMedian();   // return 2.0

    Constraints:
        - -1e5 <= num <= 1e5
        - There will be at least one element before findMedian is called.
        - At most 5 * 1e4 calls will be made to addNum and findMedian.

    Follow up:
        - If all numbers from the stream are in the range [0, 100], how would
          you optimize?
        - If 99% of numbers are in [0, 100], how would you optimize?

思路：
    addNum 要做兩段 rebalance(順序不要漏):
    1. push 進小半(maxHeap)
    2. 順序修:若 小半.max > 大半.min → 互換兩個 top
    3. size 修:若 size 差 > 1 → 把多的那邊 top 搬到另一邊

    查找median時,先確認長度是奇數還偶數, 奇數就return 小半的top, 偶數就找平均數

複雜度：
    addNum:     Time O(log(n))  Space O(log(n))
    findMedian: Time O(1)  Space O(1)
"""
from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.sH = [] # maxHeap, num inside it need * -1
        self.bH = [] # minHeap

    def addNum(self, num: int) -> None:
        heappush(self.sH, -num)
        if self.bH and -self.sH[0] > self.bH[0]:
            popS, popB = -heappop(self.sH), heappop(self.bH)
            heappush(self.sH, -popB), heappush(self.bH, popS)
        
        if len(self.sH) - len(self.bH) > 1:
            popS = -heappop(self.sH)
            heappush(self.bH, popS)


    def findMedian(self) -> float:
        isEven = (len(self.sH)+len(self.bH)) % 2 == 0
        if isEven:
            return (-self.sH[0]+self.bH[0]) / 2
        else:
            return -self.sH[0]


if __name__ == "__main__":
    # Test case 1: basic (even then odd)
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5, "Case 1: median of [1,2]"
    mf.addNum(3)
    assert mf.findMedian() == 2.0, "Case 2: median of [1,2,3]"

    # Test case 2: negatives
    mf2 = MedianFinder()
    mf2.addNum(-1)
    mf2.addNum(-2)
    assert mf2.findMedian() == -1.5, "Case 3: median of [-2,-1]"
    mf2.addNum(-3)
    assert mf2.findMedian() == -2.0, "Case 4: median of [-3,-2,-1]"

    # Test case 3: single element
    mf3 = MedianFinder()
    mf3.addNum(5)
    assert mf3.findMedian() == 5.0, "Case 5: single element"

    # Test case 4: duplicates
    mf4 = MedianFinder()
    mf4.addNum(1)
    mf4.addNum(1)
    mf4.addNum(1)
    assert mf4.findMedian() == 1.0, "Case 6: all same"

    # 事後 gate：在這行下面加 >=1 個你自己想的 case（想想哪種插入順序會逼出 rebalance bug）
    # assert ...
    mf4 = MedianFinder()
    mf4.addNum(5)
    mf4.addNum(1)
    mf4.addNum(10)
    assert mf4.findMedian() == 5, "Case 7: rebalance"
    print("All tests passed!")
