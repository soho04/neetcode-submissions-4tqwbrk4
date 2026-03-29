class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        zipFleet = zip(position, speed)
        stack = []
        res = 0

        cars = list(zipFleet)
        cars.sort(reverse=True)
        
        cars[::-1]
        print(cars)

        for i in range(len(cars)):

            time = (target - cars[i][0]) / cars[i][1]

            if stack and stack[-1] >= time:
                continue

            stack.append(time)

        return len(stack)
            
