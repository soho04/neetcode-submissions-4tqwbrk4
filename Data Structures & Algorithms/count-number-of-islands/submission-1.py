class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = defaultdict(list)
        Xboundary, Yboundary = len(grid[0]), len(grid)

        def bfs(i, j):

            bfs_queue = deque([[i,j]])

            while bfs_queue:

                print(bfs_queue)
                y, x = bfs_queue.popleft()

                islands[(i,j)].append((y,x))

                if y-1 in range(Yboundary) and grid[y-1][x] == "1":
                    grid[y-1][x] = "0"
                    bfs_queue.append([y-1, x])

                if y+1 in range(Yboundary) and grid[y+1][x] == "1":
                    grid[y+1][x] = "0"
                    bfs_queue.append([y+1, x])
                    
                if x-1 in range(Xboundary) and grid[y][x-1] == "1":
                    grid[y][x-1] = "0"
                    bfs_queue.append([y, x-1])

                if x+1 in range(Xboundary) and grid[y][x+1] == "1":
                    grid[y][x+1] = "0"
                    bfs_queue.append([y, x+1])
        
        for i in range(Yboundary):

            for j in range(Xboundary):
      
                if grid[i][j] == "1":
                    bfs(i, j)

        return len(islands.keys())

# grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]