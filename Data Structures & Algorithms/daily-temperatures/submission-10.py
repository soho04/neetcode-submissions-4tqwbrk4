class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)

        stack = []

        for index, temperature in enumerate(temperatures):

            while stack and temperature > stack[-1][1]:
                value = stack.pop()
                result[value[0]] = index - value[0]

            stack.append((index, temperature))

        return result

            


        