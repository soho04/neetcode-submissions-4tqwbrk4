class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []

        results = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):

            print("we are on ", index, temperature)

            while stack and stack[-1][0] < temperature:
                tempIndex = stack[-1][1]
                results[tempIndex] = index - tempIndex
                stack.pop()
        

            stack.append([temperature, index])
            print(stack)

        return results


            

            

                

