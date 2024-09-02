## link: https://leetcode.com/problems/find-median-from-data-stream/description/

class MedianFinder:

    """
    We use two heaps, small (max heap) and large (min heap)
    and store two halfs of elements in two heaps.
    Such that elements in small heap and smaller than elements in large heap.

    We need to handle edge cases like,
    1. uneven size of heaps.
    2. if elements in small heap are larger than large heap elements.

    To find median we just use max of small heap and min of large heap to calculate median.
    """

    def __init__(self):
        self.small = []
        self.large = []
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    # time complexity : O(logn)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure small heap elements are smaller than large heap.
        if (self.small and self.large and 
            -1 * self.small[0] > self.large[0]):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)

        # uneven sizes
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    # time complexity: O(1)
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()