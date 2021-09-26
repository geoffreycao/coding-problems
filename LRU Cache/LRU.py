class Node:
    ## Class to enable doubly linked list
    def __init__(self, key = None, val = None, left = None, right = None):
        
        self.left = left
        self.right = right
        self.key = key
        self.val = val
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = dict()
        
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head
        # print('test')


    # Returns a key if it exists, and moves it to the back of the doubly linked list
    def get(self, key: int) -> int:
        if key in self.d:
            self.move_to_back(self.d[key])
            return self.d[key].val        
        return -1

    
    # Places a key: value pair in the doubly linked list, and dictionary (hash map).
    # Evicting as necessary. And ensuring the node is put in the back of the data structure
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].val = value
            self.move_to_back(self.d[key])
        else:
            if self.capacity <= len(self.d):
                self.evict_one()
            temp = Node(key, value)
            self.d[key] = temp
            self.move_to_back(temp)
            
        
    
    
    # Evicts the least recently used key:value pair, and fixes head node
    def evict_one(self):
        node = self.head.right
        
        del self.d[node.key]
        self.head.right = node.right
        node.right.left = self.head
        # print(self.d)

        
    # Moves a node to the back of the linked list, which denotes it being recently used
    def move_to_back(self, node: Node):        
        
        if node.left:
            node.left.right = node.right
        if node.right:
            node.right.left = node.left
        
        
        node.left = self.tail.left
        node.right = self.tail
        
        self.tail.left.right = node
        self.tail.left = node
        
        
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)