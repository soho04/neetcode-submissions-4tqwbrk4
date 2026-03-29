class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = list(zip(position, speed))

        fleets.sort()

        stack = []

        print(fleets)

        for position, speed in fleets:

            finish_time = (target - position) / speed

            while stack and stack[-1] <= finish_time:
                stack.pop()
            
            stack.append(finish_time)

        return len(stack)