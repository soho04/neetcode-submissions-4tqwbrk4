class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = sorted(zip(position, speed), key=lambda x:x[0], reverse=True)
        
        stack = []

        print(fleets)

        for position, speed in fleets:

            completion_time = (target - position) / speed

            while stack and stack[-1] >= completion_time:
                completion_time = stack.pop()

            stack.append(completion_time)

        print(stack)

        return len(stack)


        # stack = [6, 2.6, 5.0]