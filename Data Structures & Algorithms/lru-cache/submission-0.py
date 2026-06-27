class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {} # key --> node

        # left = LRU
        # right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    #always remove LRU
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node

        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.nodes:
            self.remove(self.nodes[key])
            self.insert(self.nodes[key])
            return self.nodes[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.remove(self.nodes[key])

        self.nodes[key] = Node(key, value)
        self.insert(self.nodes[key])
        
        if len(self.nodes) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.nodes[lru.key]
        

        
