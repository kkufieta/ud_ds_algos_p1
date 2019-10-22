 # Explanation for problem 6: Union & Intersection of Two Linked Lists
 
 ## Requirements
 There were no requirements for this problem.
 
 ## Code Design
 
 ### Union
 I go through all items in both linked lists and put them into a set. That way I keep only unique items from both lists. I then iterate through all items in the set to create a new linked list.
 
 ### Intersection
 If any of the two linked lists are empty, I can simply return an empty linked list. 
 
 Otherwise, I put the items from each linked list into a separate set. That way, I remove all duplicate values. By using `sorted()` on the sets, I receive automatically lists where the values are sorted.
 
 I go then through both lists at the same time, adding values that exist in both lists to my new linked list, and skipping over values that are unique.
 
 
 ## Efficiency
 Assumption: 
 * `N1` is the number of elements in the first linked list.
 * `N2` is the number of elements in the second linked list.
 * `N = N1+N2` is the total number of elements in both lists.
 
 ### Time efficiency
 
 #### Union
 I loop through both linked lists once: `O(N1) + O(N2)`, and then once more through the set of all elements to create a new linked list, which is worst case `O(N)`. The total time efficiency is therefore `O(N)`.
 
 #### Intersection
 I loop through both linked lists to retrieve all elements: `O(N1) + O(N2)`. I then sort both sets into lists, which costs in the worst case `O(N1*log(N1)) + O(N2*log(N2))`. I then loop through each list once to create a new linked list, which again costs `O(N1) + O(N2)`.
 
 The total time necessary for the intersection is therefore `O(N1*log(N1)) + O(N2*log(N2))`.
 
 
 ### Space efficiency
 
 #### Union
 I use a set to collect all items in both lists, which needs in the worst case `O(N)` space. I then create a new linked list of the same size.
 
 The space requirement for the union is therefore `O(N)`.
 
 #### Intersection
 For the intersection, I create two sets for the items in each linked list, which requires `O(N1) + O(N2)` space. I reuse that space for the sorted lists. The `sorted` algorithm may require temporarily additional space of size `O(N1) + O(N2)`. I then create a new linked list that requires also `O(N1) + O(N2)`.
 
 The total space requirement for the intersection is therefore `O(N)`.