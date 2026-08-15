from random import choice
class RandomizedSet:

    def __init__(self):
        self.hmap = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False
        self.hmap[val] = len(self.list)
        self.list.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.hmap:
            # move the last element to the place idx of the element to delete
            last_ele, idx = self.list[-1], self.hmap[val]
            self.list[idx], self.hmap[last_ele] = last_ele, idx          
            self.list.pop()
            del self.hmap[val]
            return True
        
        return False
        

    def getRandom(self) -> int:
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()