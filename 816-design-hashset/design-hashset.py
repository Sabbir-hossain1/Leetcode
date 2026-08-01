# approach 1 using the fixed array based on the problem constraints
##class MyHashSet:
##
##    def __init__(self):
##        self.hash = [False] * 100001
##
##    def add(self, key: int) -> None:
##        self.hash[key] = True        
##    def remove(self, key: int) -> None:
##        self.hash[key] = False        
##    def contains(self, key: int) -> bool:
##        return self.hash[key]
# approach 2 using bucket chaning Separte Chaining
##    class MyHashSet:
##
##    def __init__(self):
##        self.size = 1000
##        self.buckets = [[] for _ in range(self.size)]
##        
##    def _hash(self, key):
##        return key % self.size
##        
##
##    def add(self, key: int) -> None:
##        bucket = self.buckets[self._hash(key)]
##        if key not in bucket:
##            bucket.add(key)        
##
##    def remove(self, key: int) -> None:
##        bucket = self.buckets[self._hash(key)]
##        if key in bucket:
##            bucket.remove(key)
##    def contains(self, key: int) -> bool:
##        bucket = self.buckets[self._hash(key)]
##        return key in bucket

# approach 3 array with linkedlist

class ListNode:
    def __init__(self,key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]        

    def add(self, key: int) -> None:
        cur = self.set[key%len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)        

    def remove(self, key: int) -> None:
        cur = self.set[key%len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur =cur.next
    def contains(self, key: int) -> bool:
        cur = self.set[key%len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False

    