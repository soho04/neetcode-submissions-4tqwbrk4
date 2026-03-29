class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}
        arr = []
        x = 0

        for n in nums:
            if not map.get(n):
                map[n] = 1
            else:
                map[n] += 1
        
        ans = heapq.nlargest(k, map, key=map.get)

        return ans


        