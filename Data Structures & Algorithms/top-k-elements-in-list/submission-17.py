class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = defaultdict(int)

        for number in nums:
            frequency[number] += 1
            print(number, frequency[number])

        ordered_results = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        print(ordered_results)

        res = []
        for index in range(k):
            res.append(ordered_results[index][0])

        return res
        
