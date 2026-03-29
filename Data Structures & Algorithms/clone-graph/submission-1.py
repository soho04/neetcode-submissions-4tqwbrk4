"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return node

        if not node.neighbors:
            clonedNode = Node(node.val)
            return clonedNode

        visited_neighbours = set()
        copyMap = {}

        start = node

        while node not in visited_neighbours:
        
            cloneNode = Node(node.val)
            copyMap[node] = cloneNode
            visited_neighbours.add(node)

            for neighbour in node.neighbors:
                if neighbour not in visited_neighbours:
                    node = neighbour
                    break

        visited_neighbours.clear()

        node = start

        process_queue = deque([node])

        while process_queue:

            node = process_queue.popleft()
            cloneNode = copyMap[node]

            for neighbour in node.neighbors:
                if neighbour not in visited_neighbours:
                    process_queue.append(neighbour)
                if copyMap[neighbour] not in cloneNode.neighbors:
                    cloneNode.neighbors.append(copyMap[neighbour])
            
            visited_neighbours.add(node)
            

        return copyMap[start]

    # 1     2

    # 3     4

    # process_queue = [2, 3]
    # 1

    #    1     2     3     4
    # [[2,3],[1,4],[1,4],[2,3]]

