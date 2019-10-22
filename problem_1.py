#%% [markdown]
# # Problem 1: LRU Cache
#%% [markdown]
# In this problem, the goal is to design a data structure known as a Least Recently Used (LRU) cache. This is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. This problem is related to hash maps.
# 
# Both `get()` and `set()` operations are considered as "using" an entry.
# 
# The lookup operations (i.e. `get()` and `set()`) are supposed to be fast. 
# 
# `get()`:
# * If the entry is found in the cache, it is known as a cache hit.
# * If the entry is not found, it is a cache miss.
# 
# ### Upper bound
# When designing a cache, we place an upper bound on the size of the cache. When the cache is full, we handle the situation by removing the least recently used entry as described above. Once the entry is removed, we use the `put()` operation to insert the new element.
# 
# ### Behavior
# In case of a cache hit, the `get()` operation should return the appropriate value.
# In case of a cache miss, the `get()` should return -1.
# 
# While putting an element in the cache, the `set()` operation must insert the element. If the cache is full, the least recently used entry must be removed before inserting the new element.
# 
# All operations must take O(1) time.

#%%
class Node():
    
    def __init__(self, key, value):
        """
        Node with pointers to previous and next nodes.
        """
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
    def get_data(self):
        """
        Return the key and value.
        """
        return self.key, self.value


#%%
class DoublyLinkedList():
    
    def __init__(self):
        """
        Doubly linked list.
        """
        self.head = None
        self.tail = None
        
    def prepend(self, key, value):
        """
        Creates a new node and prepends it to the front of the list.
        """
        node = Node(key, value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return node
    
    def update_node_to_mru(self, node):
        """
        Updates the node position to be the most recently used (mru) node.
        """
        if node is not self.head:            
            prevNode = node.prev
            nextNode = node.next
            # Move node to the front of the list
            node.next = self.head
            self.head.prev = node
            self.head = node
            # Fix the "gap" I've created by moving the node to the front
            prevNode.next = nextNode
            if nextNode:
                nextNode.prev = prevNode
            else:
                self.tail = prevNode
                
    def remove_lru(self):
        """
        Remove the least recently used (lru) node, which is located
        at the end of the list.
        """
        key, value = self.tail.get_data()
        self.tail = self.tail.prev
        self.tail.next = None
        
        return key, value
        
    def __str__(self):
        """
        String representation of the doubly linked list.
        """
        s = ""
        node = self.head
        while node:
            s += str(node.get_data()[1]) + " <--> "
            node = node.next
        return s
        

class LRU_Cache(object):

    def __init__(self, capacity):
        """
        Least recently used (LRU) cache with a fixed capacity.
        """
        assert(type(capacity) == int), "Capacity has to be an integer"
        assert(capacity > 0), "Capacity has to be larger than 0"
        # Initialize class variables
        self.cache = {}
        self.ll = DoublyLinkedList()
        self.capacity = capacity

    def get(self, key):
        """
        Retrieves the item with the provided key. 
        Returns -1 if nonexistent.
        """
        if key in self.cache:
            self.ll.update_node_to_mru(self.cache[key])
            return self.cache[key].get_data()[1]
        else:
            return -1

    def set(self, key, value):
        """
        Sets the value if the key is not present in the cache.
        
        If the cache is at capacity, it removes the oldest item before
        inserting the new item.
        """
        if key in self.cache:
            self.ll.update_node_to_mru(self.cache[key])
        elif len(self.cache) < self.capacity:
            node = self.ll.prepend(key, value)
            self.cache[key] = node
        else:
            removedKey, _ = self.ll.remove_lru()
            self.cache.pop(removedKey)
            node = self.ll.prepend(key, value)
            self.cache[key] = node
            
    def __str__(self):
        """
        String representation of the cache
        """
        return str(self.ll)

#%% [markdown]
# ## Testcases

#%%
# ==== Testcase 1: Set elements ====
# max capacity: 5
# input: [1, 2, 3, 4]
# expected output: 
# 1 <--> 
# 2 <--> 1 <--> 
# 3 <--> 2 <--> 1 <--> 
# 4 <--> 3 <--> 2 <--> 1 <--> 

print("--- Testcase 1: Set elements ---")
cache = LRU_Cache(5)
for v in [1, 2, 3, 4]:
    cache.set(v, v)
    print(cache)


#%%
# ==== Testcase 2: Get elements ====
# input: [1, 2, 9]
# expected output: 
# get value  1  from cache:  1
# 1 <--> 4 <--> 3 <--> 2 <--> 
# get value  2  from cache:  2
# 2 <--> 1 <--> 4 <--> 3 <--> 
# get value  9  from cache:  -1 (because 9 is not present in cache)
# 2 <--> 1 <--> 4 <--> 3 <--> 

print("--- Testcase 2: Get elements ---") 
for v in [1, 2, 9]:
    print("get value ", v, " from cache: ", cache.get(v))       
    print(cache)


#%%
# ==== Testcase 3: Set more elements ====
# input: [5, 6, 7]
# expected output: 
# 5 <--> 2 <--> 1 <--> 4 <--> 3 <--> 
# 6 <--> 5 <--> 2 <--> 1 <--> 4 <--> 
# 7 <--> 6 <--> 5 <--> 2 <--> 1 <-->

print("--- Testcase 3: Set more elements ---")
print(cache)
for v in [5, 6, 7]:
    cache.set(v, v) 
    print(cache)


#%%
cache.cache


#%%
# ==== Testcase 4: Get more elements ====
# input: [3, 4, 5, 'a']
# expected output: 
# get value  3  from cache:  -1
# 7 <--> 6 <--> 5 <--> 2 <--> 1 <--> 
# get value  4  from cache:  -1
# 7 <--> 6 <--> 5 <--> 2 <--> 1 <--> 
# get value  5  from cache:  5
# 5 <--> 7 <--> 6 <--> 2 <--> 1 <--> 

print("--- Testcase 4: Get more elements ---")
for v in [3, 4, 5, 'a']:
    print("get value ", v, " from cache: ", cache.get(v))  
    print(cache)


#%%
# ==== Testcase 5: Don't set elements, try to retrieve elements ====
# set input: []
# get input: [1, 2, 3]
# expected output: 
# get value  3  from cache:  -1
# 
# get value  4  from cache:  -1
# 
# get value  5  from cache:  -1
# 
# get value  a  from cache:  -1
# 

cache = LRU_Cache(5)
print("--- Testcase 5: Don't set elements, try to retrieve elements ---")
for v in [3, 4, 5, 'a']:
    print("get value ", v, " from cache: ", cache.get(v))  
    print(cache)


#%%
# ==== Testcase 6: Set duplicate elements and non-numeric entries ====
# max capacity: 5
# input: [1, 2, 3, 4, 1]
# expected output: 
# 1 <--> 
# 2 <--> 1 <--> 
# 1 <--> 2 <--> 
# 4 <--> 1 <--> 2 <--> 
# 5 <--> 4 <--> 1 <--> 2 <--> 

print("--- Testcase 6: Set elements ---")
cache = LRU_Cache(5)
for v in [1, 2, 1, 4, 5, 'abc', 8, 'abc']:
    cache.set(v, v)
    print(cache)


#%%
# ==== Testcase 7: Play around with cache with max limit 0 ====
# set input: [1, 2, 3]

print("--- Testcase 7: Play around with cache with max limit 0 ---")
cache = LRU_Cache(0)
for v in [1, 2, 3]:
    cache.set(v, v)
    print(cache)


#%%



