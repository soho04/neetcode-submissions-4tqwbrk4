class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        self.heap = []

        for number in nums:
            heapq.heappush(self.heap, number)

            if len(self.heap) > k:
                heapq.heappop(self.heap)

        return self.heap[0]

