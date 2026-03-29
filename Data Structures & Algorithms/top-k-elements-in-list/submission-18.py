class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = defaultdict(int)

        for number in nums:
            frequencies[number] += 1

        max_heap = []

        for key, frequency in frequencies.items():

            heapq.heappush(max_heap, (frequency, key))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [pair[1] for pair in max_heap]

        # return res

        # ordered_results = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        # res = []
        # for index in range(k):
        #     res.append(ordered_results[index][0])

        # return res
        
