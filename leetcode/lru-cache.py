class LRUCache:

    def __init__(self, capacity: int):
        self.cur_cap = 0
        self.max_cap = capacity
        self.cache = {}
        self.p = []
    
    def forward (self, key):
         self.p.insert(0, self.p.pop(self.p.index(key)))

    def get(self, key: int) -> int:
        if key in self.p:
            self.forward(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        
        if key in self.p:
            self.forward(key)
        else:
            if self.cur_cap >= self.max_cap:
                remove_key = self.p.pop()
                del self.cache[remove_key]
            self.cur_cap += 1
            self.p.insert(0, key)
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
