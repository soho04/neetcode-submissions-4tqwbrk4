class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers)-1

        running_sum = numbers[left] + numbers[right]

        if running_sum == target:
            return [left+1, right+1]

        while left < right:

            if running_sum > target:
                right -= 1
                running_sum -= numbers[right+1] - numbers[right]
            
            elif running_sum < target:
                left += 1
                running_sum += numbers[left] - numbers[left-1]

            else:
                return [left+1, right+1]

            
        # l     r         
        # 1, 2, 3, 4    target = 4 running_sum = 5
        #               current = 5 - (4 - 3)




