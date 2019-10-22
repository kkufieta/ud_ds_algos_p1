#%% [markdown]
# # Problem 6: Union and Intersection of Two Linked Lists
# 
# Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.
# 
# You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.
#%% [markdown]
# ### Node

#%%
class Node:
    def __init__(self, value):
        """
        Simple node with a pointer to the next node.
        """
        self.value = value
        self.next = None

    def __str__(self):
        """
        String representation of the node
        """
        return str(self.value)

#%% [markdown]
# ## Linked List

#%%
class LinkedList:
    def __init__(self):
        """
        Linked list with a reference to both the head and the tail.
        """
        self.head = None
        self.tail = None
        self.len = 0

    def append(self, value):
        """
        Appends a value to the end of the linked list.
        """
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.len += 1
        
    def get_head(self):
        """
        Returns the head of the linked list.
        """
        return self.head
    
    def get_tail(self):
        """
        Returns the tail of the linked list.
        """
        return self.tail
    
    def __iter__(self):
        """
        Iterates through the linked list.
        """
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __len__(self):
        """
        Returns the length of the linked list.
        """
        return self.len
    
    def __str__(self):
        """
        String representation of the linked list.
        """
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

#%% [markdown]
# ## Union

#%%
def union(list_1, list_2):
    """
    Returns a linked list containing the union of the two linked lists.
    """    
    items = set()
    for item in list_1:
        items.add(item)
    for item in list_2:
        items.add(item)
    union = LinkedList()
    for item in items:
        union.append(item)
    return union

#%% [markdown]
# ## Intersection

#%%
def intersection(list_1, list_2):
    if len(list_1) == 0:
        return list_1
    if len(list_2) == 0:
        return list_2
    
    items_1 = set()
    items_2 = set()
    for item in list_1:
        items_1.add(item)
    for item in list_2:
        items_2.add(item)
    
    # using sorted on a set transforms the set into a sorted list
    items_1 = sorted(items_1)
    items_2 = sorted(items_2)
    
    i_1, i_2 = 0, 0
    intersection = LinkedList()
    while i_1 < len(items_1) and i_2 < len(items_2):
        if items_1[i_1] == items_2[i_2]:
            intersection.append(items_1[i_1])
            i_1 += 1
            i_2 += 1
        elif items_1[i_1] < items_2[i_2]:
            i_1 += 1
        else:
            i_2 += 1
    return intersection

#%% [markdown]
# ## Tests

#%%
# Test case 1
l_1 = LinkedList()
l_2 = LinkedList()

for el in [3,2,4,35,6,65,6,4,3,21]:
    l_1.append(el)

for el in [6,32,4,9,6,1,11,21,1]:
    l_2.append(el)

# Expected output (another order is possible) in linked list format
# should contain these elements:
# [32, 5, 2, 35, 3, 4, 6, 1, 9, 11, 21]
print("Union: ", union(l_1,l_2))

# Expected output (another order is possible) in linked list format
# [4, 6, 21]
print("Intersection: ", intersection(l_1,l_2))


#%%
# Test case 2
l_1 = LinkedList()
l_2 = LinkedList()

for el in [3,2,4,35,6,65,6,4,3,23]:
    l_1.append(el)

for el in [1,7,8,9,11,21,1]:
    l_2.append(el)

# Expected output (another order is possible) in linked list format
# [3,2,4,35,65,6,23,7,8,9,11,21,1]
print("Union: ", union(l_1,l_2))

# Expected output (another order is possible) in linked list format
# []
print("Intersection: ", intersection(l_1,l_2))


#%%
# Test case 3
l_1 = LinkedList()
l_2 = LinkedList()

# We don't append any information

# Expected output (another order is possible) in linked list format
# []
print("Union: ", union(l_1,l_2))

# Expected output (another order is possible) in linked list format
# []
print("Intersection: ", intersection(l_1,l_2))


#%%
# Test case 4
l_1 = LinkedList()
l_2 = LinkedList()

for el in [1,1,1]:
    l_2.append(el)

# Expected output (another order is possible) in linked list format
# [1]
print("Union: ", union(l_1,l_2))

# Expected output (another order is possible) in linked list format
# []
print("Intersection: ", intersection(l_1,l_2))


#%%
# Test case 5
l_1 = LinkedList()
l_2 = LinkedList()

for el in [1,1,1]:
    l_2.append(el)
    l_1.append(el)

# Expected output (another order is possible) in linked list format
# [1]
print("Union: ", union(l_1,l_2))

# Expected output (another order is possible) in linked list format
# [1]
print("Intersection: ", intersection(l_1,l_2))


#%%



