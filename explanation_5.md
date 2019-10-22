# Explanation for problem 5: Blockchain

## Requirements
There were no requirements for this problem.

## Code Design
The block chain is similar to a linked list, where the pointers point to the previous node (as opposed to the next one).

I am therefore keeping track of the "head" of the blockchain, which in my case is the most recently added block. This was merely a choice of terminology.

The genesis block points to the first block that was inserted.


## Efficiency

### Time efficiency
The insertion of a block into the block chain takes `O(1)` time.

Traversing the block chain to retrieve a specific block requires `O(N)` time (here not implemented but is straight forward).


### Space efficiency
The block chain requires `O(N)` space.

