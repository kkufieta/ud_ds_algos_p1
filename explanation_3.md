 # Explanation for problem 3: Huffman Coding
 
 ## Requirements
 There were no requirements for this problem.
 
 ## Code Design
 I chose to implement this algorithm: https://www2.cs.duke.edu/csed/poop/huff/info/
 
 Once I create the tree according to the above mentioned algorithm, I traverse it to create a dictionary that maps letters to their respective binary code (in `map_char_to_binary`). I use that dictionary to encode the data (in `encode_data`).
 
 
 ## Efficiency
 
 ### Time efficiency
 Given the input data of size `N` (number of characters in the sentence), the following operations are performed:
 * Calculate the frequency of the letters and create a forest of single node Huffman trees, requires to go through each letter in the sentence: `O(N)`
 * Merging two trees takes `O(1)`. Before merging, I'm sorting the forest based on the weight of each tree at each iteration. The sorting takes `O(N*log(N))` time. Creating the Huffman Tree then means we we have to do that for `N` single node trees, so the total cost to build the Huffman tree is `O(N^2*log(N))`.
 * Map the letters to their respective binary form requires `O(N)` in the worst case scenario, when the input data has all unique characters.
 * Encoding the data is again `O(N)`, since we have to go through each letter in the input data to encode it.
 * Decoding the tree takes `O(N)`, since we have to go through each letter in the input data.
 
 The total cost for time is `O(N^2*log(N))`.
 
 This is too high and should be reduced. This can be done by using a min-heap based on the weight of each tree, rather than a list of trees that has to be sorted every time a new tree is inserted.
 
 Creating the min-heap will take `O(N*log(N))`, since inserting & deleting require `O(log(N))`, and we have to insert `N` trees. Later, when merging trees, we have to do so `N` times, and each time we delete 2 trees and insert one new tree, thus needing `O(log(N))` for each of these operations, which results in a total of `O(N*log(N))` operations.
 
 ### Space efficiency
 We create these data structures to encode and decode data using Huffman trees:
 * Single Node Huffman trees to begin with, which are later merged into a single Huffman tree containing all letters. Despite the fact that each tree has its own overhead, we can simplify the space efficiency analysis for a large input `N` to be `O(N)` at all times.
 * When encoding data, we create a hash map that maps the letters to their respective binary code. This will take in the worst case when all letters are unique in the input data: `O(N)`.
 
 The total space cost is thus `O(N)`.