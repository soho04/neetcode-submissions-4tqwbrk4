class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for currentIndex in range(len(temperatures)):

            while stack and temperatures[currentIndex] > temperatures[stack[-1]]:
                
                index = stack.pop()
                res[index] = currentIndex - index

            stack.append(currentIndex)

        return res

            

            

                

