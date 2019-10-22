#%% [markdown]
# # Problem 3: Huffman Coding
#%% [markdown]
# A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.
# 
# The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.
# 
# There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.
#%% [markdown]
# ## Algorithm
# I chose to implement this algorithm: https://www2.cs.duke.edu/csed/poop/huff/info/
#%% [markdown]
# ### Node

#%%
class Node:
    def __init__(self, letter, left_node, right_node):
        """
        Node that points to a left and right child.
        """
        self.letter = letter
        self.left = left_node
        self.right = right_node

#%% [markdown]
# ### HuffmanTree

#%%
class HuffmanTree:
    def __init__(self):
        """
        Huffman tree with an assigned weight.
        """
        self.root = None
        self.weight = None
        
    def set_root(self, letter, left_node=None, right_node=None):
        """
        Sets the root node with a given letter, and left and right children.
        """
        self.root = Node(letter, left_node, right_node)
        
    def get_root(self):
        """
        Returns the root node.
        """
        return self.root
        
    def set_weight(self, weight):
        """
        Sets the weight of the tree.
        """
        self.weight = weight
        
    def get_weight(self):
        """
        Returns the weight of the tree.
        """
        return self.weight
    
    def _get_node_letter(self, node):
        """
        This functions makes sure that both None and "" are
        printed out.
        """
        letter = node.letter
        if not letter:
            return "None"
        elif letter == " ":
            return "' '"
        else:
            return "'" + letter + "'"
    
    def __str__(self):
        """
        String representation of the tree.
        """
        if not self.root:
            return ""
        s = "Tree with weight: " + str(self.weight) + "\n"
        level = 1
        nodes = [(self.root, level)]
        s += self._get_node_letter(self.root) + "\n"
        while len(nodes) > 0:
            node, new_level = nodes.pop(0)
            if new_level != level:
                s += "\n"
                level = new_level
            if node.left:
                nodes.append((node.left, level+1))
                s += self._get_node_letter(node.left) + " "
            else:
                s += "None "
            if node.right:
                nodes.append((node.right, level+1))
                s += self._get_node_letter(node.right) + " "
            else:
                s += "None "
        s += "\n"
        return s   

#%% [markdown]
# ### Helper functions
# * `merge_trees` takes two Huffman trees and merges them
# * `get_forest` takes a string and returns single node Huffman trees

#%%
def merge_trees(tree1, tree2):
    """
    Merges two Huffman trees into a new tree, with the weight of the
    new tree equal to the sum of the weights of tree1 and tree2.
    
    Returns the merged tree.
    """
    weight = tree1.get_weight() + tree2.get_weight()
    tree = HuffmanTree()
    # Since the root of the tree is not a leaf, 
    # it does not contain a letter
    tree.set_root(None, tree1.get_root(), tree2.get_root())
    tree.set_weight(weight)
    return tree

def get_forest(data):
    """
    Counts the frequency of all letters in data and returns a forest
    of single node Huffman trees.
    """
    assert(type(data) == str), "Input argument 'data' has to be a string"
    frequency = {}
    for letter in data:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    forest = []
    for letter, weight in frequency.items():
        tree = HuffmanTree()
        tree.set_root(letter)
        tree.set_weight(weight)
        forest.append((weight, tree))
        
    # Handle the case when data consists of only character, e.g. "k" or "kkkkk"
    if len(forest) == 1:
        tree = HuffmanTree()
        tree.set_root(None)
        tree.set_weight(0)
        forest.append((weight, tree))
        
    return forest

#%% [markdown]
# ### Helper functions
# * `map_char_to_binary` creates a dictionary that maps letters to their equivalent binary representation based on the Huffman tree
# * `encode_data` encodes the data based on the original data and the equivalent Huffman tree.

#%%
def map_char_to_binary(data, tree):
    """
    Creates a hash map that maps the letter to its binary equivalent,
    based on the Huffman tree.
    """
    nodes = [(tree.get_root(), "")]
    code = {}
    while len(nodes) > 0:
        node, s = nodes.pop(0)
        if node.left:
            nodes.append((node.left, s+"0"))
        if node.right:
            nodes.append((node.right, s+"1"))
        if node.letter:
            code[node.letter] = s
    return code

def encode_data(data, tree):
    """
    Returns the encoded data based on the original data and the equivalent
    Huffman tree.
    """
    ch_to_b = map_char_to_binary(data, tree)
    b = ""
    for ch in data:
        b += ch_to_b[ch]
    return b

#%% [markdown]
# ### huffman_encoding and huffman_decoding
# * `huffman_encoding` creates a Huffman tree from the data and returns both the encoded data and the tree.
# * `huffman_decoding` takes the encoded data and Huffman tree, and decodes the data back into its original form.

#%%
def huffman_encoding(data):
    """
    Creates a Huffman tree from the data and returns both the
    encoded data and the tree.
    """
    assert(type(data) == str), "Input argument 'data' has to be a string"
    assert(len(data) > 0), "An empty string is not a valid input"
    forest = get_forest(data)
    
    while len(forest) > 1:
        forest = sorted(forest, key=lambda weight: weight[0])
        tree1 = forest.pop(0)[1]
        tree2 = forest.pop(0)[1]
        merged_tree = merge_trees(tree1, tree2)
        forest.append((merged_tree.get_weight(), merged_tree))
    tree = forest[0][1]
    code = encode_data(data, tree)
    return code, tree

def huffman_decoding(data, tree):
    """
    Decodes and returns the decoded data.
    """
    assert(type(tree) == HuffmanTree), "Tree has to be a HuffmanTree"
    root = tree.get_root()
    if not root:
        return ""
    node = root
    s = ""
    # Handle the special case then the Huffman tree has only
    # one node/letter
    if not root.left and not root.right:
        raise Exception("The tree contains only one letter, this case has not been implemented yet.")

    for b_num in data:
        if node.letter:
            s += node.letter
            node = root
        if b_num is "0":
            node = node.left
        else:
            node = node.right
    s += node.letter
    return s

#%% [markdown]
# # Tests

#%%
# Test the huffman encoding and decoding
# Input: "go go gophers"
# Output: expect to see most frequent letters ('g', 'o') closer 
# to the root of the tree than the rest of the letters
sentence = "go go gophers"
code, tree = huffman_encoding(sentence)

print(tree)
print(code)

# Expected output: "go go gophers"
print(huffman_decoding(code, tree))


#%%
import sys

def test(sentence):
    print("\n------------------------")
    print("------- New Test -------")
    print("------------------------\n")
    print("Data: '{}'".format(sentence))
    encoded_data, tree = huffman_encoding(sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert(sentence == decoded_data)
    print ("Decoded data: '{}'\n".format(decoded_data))
      
    print ("Encoded data: '{}'\n".format(encoded_data))
    print(tree)

    print ("The size of the data is: {}".format(sys.getsizeof(sentence)))
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))    
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    


#%%
# Input:  
test_sentences = ["The bird is the word", 
                  "Hey, this is Kat. She's the best!",
                  "kkkk",
                  "         ",
                  ""]

# Output: I expect the first two cases to work, and the last one to throw an exception,
# since I defined that an emtpy string is not a valid input.
for sentence in test_sentences:
    test(sentence)


