class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        queue = deque([])
        maxHeap = [-x for x in Counter(tasks).values()]
        time = 0 

        heapq.heapify(maxHeap)

        while maxHeap or queue:

            print(maxHeap, queue)

            if maxHeap:
                task = heapq.heappop(maxHeap)
                new_taskValue = -task - 1
                if new_taskValue != 0:
                    queue.append((new_taskValue, time+n))

            if queue:
                if queue[0][1] == time:
                    poppedTask = queue.popleft()
                    print(-poppedTask[0])
                    heapq.heappush(maxHeap, -poppedTask[0])

            time += 1

        return time
            

        # X, X, Y, Y, IDLE
        # X     Y     IDLE
        #    X     Y

        # A, A, A, B, C IDLE