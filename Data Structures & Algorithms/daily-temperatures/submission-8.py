class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []

        results = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):

            while stack and stack[-1][0] < temperature:
                temp = stack.pop()
                results[temp[1]] = index - temp[1]
        
            stack.append([temperature, index])

        return results


            

            

                

