class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        self.maxHeap = []

        for stone in stones:
            heapq.heappush(self.maxHeap, -stone)

        print(self.maxHeap)

        while len(self.maxHeap) >= 2:

            x = -heapq.heappop(self.maxHeap)
            y = -heapq.heappop(self.maxHeap)

            print(x, y)

            print(x-y)
            heapq.heappush(self.maxHeap, -(x-y))

            print(self.maxHeap)

        return -self.maxHeap[0]

        





    # -6, -4, -3, -2, -2

    # 6, 4 -> 2
    # 2, 3 -> 1
    # 1, 2 -> 1
    # 1, 2 -> 