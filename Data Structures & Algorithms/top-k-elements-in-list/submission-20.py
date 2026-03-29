class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = defaultdict(int)

        for number in nums:
            frequencies[number] += 1

        heap = []

        for key, frequency in frequencies.items():

            heapq.heappush(heap, (frequency, key))

            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]