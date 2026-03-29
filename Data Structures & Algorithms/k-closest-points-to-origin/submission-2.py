class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        self.maxHeap = []
        res = []

        for point in points:

            euclideanDistance = (point[0] ** 2) + (point[1] ** 2)
            euclideanDistance = math.sqrt(euclideanDistance)

            print("got distance ", euclideanDistance, " for ", point)

            heapq.heappush(self.maxHeap, (-euclideanDistance, point))

            if len(self.maxHeap) > k:
                print(self.maxHeap)
                heapq.heappop(self.maxHeap)

        res = [point[1] for point in self.maxHeap]

        return res