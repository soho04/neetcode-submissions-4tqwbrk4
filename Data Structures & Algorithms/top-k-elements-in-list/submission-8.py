class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        print(count)

        arr = [(-count, value) for (value, count) in count.items()]

        arr.sort()

        heapq.heapify(arr)
        
        print(arr)

        return [tuples[1] for tuples in arr[:k]]
        