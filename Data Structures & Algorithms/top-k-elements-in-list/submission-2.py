class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        k_count = Counter(nums)
        tuple = sorted(k_count.items(), key=lambda item: item[1], reverse=True)[:k]
        arr = []

        for (x,y) in tuple:
            arr.append(x)

        return arr