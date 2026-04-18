"""
LeetCode 295. Find Median from Data Stream
Difficulty: Hard
Tags: Heap, Design, Two Pointers
URL: https://leetcode.com/problems/find-median-from-data-stream/

思路：
    Using min-heap and max-heap to automatically sort the numbers.

複雜度：
    addNum:  Time O(log(N)) Space O(N)
    findMedian: Time O(1) Space O(1)
"""
import heapq


class MedianFinder:
    def __init__(self):
        self.large = [] # minH
        self.small = [] # maxH

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, num)
        
        m, n = len(self.large), len(self.small)
        if m - n > 1:
            popEl = heapq.heappop(self.large)
            heapq.heappush(self.small, -popEl)
        if self.large and self.small and self.large[0] < -self.small[0]:
            popEl1 = heapq.heappop(self.large)
            popEl2 = -heapq.heappop(self.small)
            heapq.heappush(self.large, popEl2)
            heapq.heappush(self.small, -popEl1)
    def findMedian(self) -> float:
        m, n = len(self.large), len(self.small)
        if m > n:
            return self.large[0]
        elif n > m:
            return -self.small[0]
        else:
            return (self.large[0]-self.small[0]) / 2
        

if __name__ == "__main__":
    # Test case 1: basic
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

    print("All tests passed!")
