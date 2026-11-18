from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        answer = self.cache[key]
        self.cache.move_to_end(key, last=False)
        return answer
        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) >= self.capacity:
            self.cache.popitem(last=True)
        self.cache[key] = value
        self.cache.move_to_end(key, last=False)

