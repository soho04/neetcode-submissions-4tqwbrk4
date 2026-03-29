class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers)-1
        sum = numbers[l] + numbers[r]

        while l < r:
            if sum > target:
                sum -= numbers[r] - numbers[r-1]
                r -= 1
            elif sum < target:
                sum += numbers[l+1] - numbers[l]
                l += 1
            else:
                return [l+1, r+1]