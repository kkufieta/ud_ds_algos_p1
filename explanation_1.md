# Explanation for problem 1: LRU Cache

## Requirements
The problem requires that all operations take `O(1)` time.
The operations are: `get()` and `set()`.


## Code Design

Since the requirements are that all operations take `O(1)` time, I decided that combining a doubly linked list and a hash map is a good choice.

The doubly linked list is used to keep track of the timely order when nodes were used.

The hash map allows me to look up the requested node with `O(1)` time complexity.

## Efficiency

### Time efficiency for `get()`
Looks up if the key is in the hash map (amortized `O(1)`). If yes, update the corresponding node in the linked list to be the most recently used node (`O(1)`).

### Time efficiency for `set()`
If the cache has not yet reached its capacity, insert the item both into the linked list and hash map (both `O(1)`).

If the cache is full, remove the least recently used item from both the hash map and linked list (both `O(1)`). Then, add the item to the list and hash map (both `O(1)`).

### Space efficiency
The LRU Cache has a maximum capacity and can hold `N` items. Since we are using both a linked list and a hash map, we need O(2N) space, which we can simplify to `O(N)` space efficiency for large `N`.


