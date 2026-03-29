class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}

        for n in nums:
            if not map.get(n):
                map[n] = 1
            else:
                map[n] += 1

        return list(heapq.nlargest(k, map, key=map.get))


        