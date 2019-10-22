# Explanation for problem 2: File Recursion

## Requirements
There were no requirements for this problem.

## Code Design
Given a directory and a suffix, I am supposed to find and print all files in the directory with the specified suffix. That reminds me of searching a tree. I decided to use depth first search (DFS) and recursion to solve this problem.

## Efficiency

### Time efficiency
Since it traverses all `N` (sub)directories, the time efficiency is equal to the total number of (sub)directories: `O(N)`

### Space efficiency
Worst case it saves all `N` paths in an array, so the space efficiency is `O(N)`.

