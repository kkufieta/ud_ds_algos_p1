# Explanation for problem 4: Active Directory

## Requirements
There were no requirements for this problem.

## Code Design
This problem reminded me of a graph traversal where you have to watch out for closed loops where you might get stuck in.

I use a queue where I keep track of all the groups I have to search in order to find out if the user is in the group. To make sure that I don't get stuck in a closed loop, I keep a set of visited groups. If I have already visited a group previously, I simply pass over it.

## Efficiency

### Time efficiency
Assuming that the input size is how deeply nested the groups are, e.g. a graph of groups with `N` nodes, I visit each node once. Then, when the list of users is of size `M`, I search the list once for the desired user.

Thus, the time complexity for this search operation is `O(N*M)` in the worst case.

### Space efficiency
I keep a queue with groups I have to search through, and a set of groups I have visited. Each of them has at most `N` entries, so the total of required space is in the worst case `O(2N)`, or simplified for large `N`: `O(N)`.

