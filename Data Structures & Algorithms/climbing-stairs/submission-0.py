class Solution:
    def climbStairs(self, n: int) -> int:
        
        arr = [1] * (n+1)

        for i in range(len(arr)-1, -1, -1):
            if i == len(arr) - 1 or i == len(arr) - 2:
                arr[i] = 1
            else:
                arr[i] = (arr[i+1] + arr[i+2])
 
        return arr[0]
        
                
