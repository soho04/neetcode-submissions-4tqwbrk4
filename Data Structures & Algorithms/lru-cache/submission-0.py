class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, "left"), Node(0, "right")
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        
    def insert(self, node):
        previous_node, next_node = self.right.prev, self.right
        previous_node.next = node
        self.right.prev = node
        node.prev = previous_node 
        node.next = next_node
       
    def remove(self, node):
        previous_node, next_node = node.prev, node.next
        previous_node.next = next_node
        next_node.prev = previous_node
        node.prev, node.next = None, None

    def put(self, key: int, value: int) -> None:

        createdNode = Node(key, value)

        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = createdNode
            self.insert(createdNode)
        else:
            self.cache[key] = createdNode
            self.insert(createdNode)

        if len(self.cache) > self.cap:
            self.cache.pop(self.left.next.key)
            self.remove(self.left.next)

#      <-   <-   <-   <-
# Left -> 2 -> 3 -> 4 -> Right
