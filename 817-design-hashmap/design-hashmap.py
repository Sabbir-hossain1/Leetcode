# approach 1
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]        
    def _hash(self, key):
        return key%self.size
    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k,v) in enumerate(bucket):
            if k==key:
                bucket[i]=(key,value)
                return
        bucket.append((key,value))

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]
        for k,v in bucket:
            if k==key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return         

# approach 2:  direct addressing
# class MyHashMap:
#     def __init__(self):
#         self.map = [-1]*1000001

#     def put(self,key:int,value:int)->None:
#         self.map[key]=value
#     def get(self,key:int)->int:
#         return self.map[key]

#     def remove(self,key:int)->None:
#         self.map[key]=-1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)