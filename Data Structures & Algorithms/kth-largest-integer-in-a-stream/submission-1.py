class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        heapq.heapify(self.heap)

        print(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

        # for number in nums:
        #     heapq.heappush(self.heap, number)
        #     if len(self.heap) > self.k:
        #         heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            value = heapq.heappop(self.heap)

        return self.heap[0]

        # [2, 3, 3, 3]
        # Kth largest is the value at the root after we POP!!!!


    # k = 3
    #         
    # [ 1, 2, 3, 3, 3, 5, 6, 7,