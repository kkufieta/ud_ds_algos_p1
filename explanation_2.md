 # Explanation for problem 2: File Recursion
 
 ## Requirements
 There were no requirements for this problem.
 
 ## Code Design
 Given a directory and a suffix, I am supposed to find and print all files in the directory with the specified suffix. That reminds me of searching a tree. I decided to use depth first search (DFS) and recursion to solve this problem.
 
 ## Efficiency
 
 ### Time efficiency
 Since it traverses all `N` (sub)directories, the time efficiency is equal to the total number of (sub)directories: `O(N)`
 
 ### Space efficiency
 The algorithm is recursive and requires therefore additional space due to the call stack. 
 
 If we look at the directory, its subdirectories and files as a tree with a width `N` at each level, and a depth `M` from each level, the call stack will be at most `M` levels deep, and at each level we need space for the array to save `N` paths. The space efficiency is therefore `O(NM)`.