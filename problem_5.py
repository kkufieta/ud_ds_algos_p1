#%% [markdown]
# # Problem 5: Blockchain
# 
# A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using:
# * A SHA-256 hash
# * The Greenwich Mean Time when the block was created
# * Text strings as the data
#%% [markdown]
# ## Block

#%%
import hashlib
from time import gmtime, strftime

class Block:
    def __init__(self, timestamp, data, prev_hash, prev_block):
        """
        Creates a block with a timestamp, data, and information
        about the previous block and its hash code.
        """
        assert(type(data) == str), "Data has to be of type String"
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.prev_block = prev_block
        self.hash = self._calc_hash()
        
    def _calc_hash(self):
        """
        Helper function to calculate the hash code.
        """
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) +
                    str(self.data) + 
                    str(self.prev_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
        
    def get_hash(self):
        """
        Returns the hash code.
        """
        return self.hash
    
    def get_data(self):
        """
        Returns the data.
        """
        return self.data
    
    def get_timestamp(self):
        """
        Returns the timestamp.
        """
        return self.timestamp
    
    def __str__(self):
        """
        String representation of the block.
        """
        s = "Block:\n"
        s += "Timestamp: " + strftime("%Y-%m-%d, %H:%M:%S", self.timestamp) + "\n"
        s += "Data: " + str(self.data) + "\n"
        s += "Hash: " + str(self.hash) + "\n"
        return s

#%% [markdown]
# ## Simple blockchain implementation

#%%
class BlockChain:
    def __init__(self):
        """
        Creates a blockchain with the genesis block.
        """
        self.genesis_block = Block(gmtime(), "genesis_block", 0, None)
        self.head = self.genesis_block
        self.size = 1
    
    def add_block(self, data):
        """
        Adds a new block to the blockchain.
        """
        assert(type(data) == str), "Data has to be of type String"
        # prev_hash: hash of the head, update head = block            
        block = Block(gmtime(), data, self.head.get_hash(), self.head)
        self.head = block
        print("Added new block with data: " + str(data) + 
              "\nHash: " + str(block.get_hash()) + "\n")
        self.size += 1
        
    def __len__(self):
        """
        Returns the size of the blockchain.
        """
        return self.size
        
    def __str__(self):
        """
        String representation of the blockchain.
        """
        if not self.head:
            return "Empty Blockchain"
        block = self.head
        block_stack = []
        while block:
            block_stack.insert(0, block)
            block = block.prev_block
        s = "---- Blockchain: ----\n"
        for block in block_stack:
            s += str(block) + "\n"
        return s
            

#%% [markdown]
# ## Tests

#%%
blockchain = BlockChain()
blockchain.add_block("K")
blockchain.add_block("A")
blockchain.add_block("T")
print(blockchain)
print("Number of blocks in blockchain: ", len(blockchain))


#%%
blockchain = BlockChain()
# Length of blockchain is expected to be of length 1, since
# it contains the genesis block.
print(len(blockchain))


#%%
# Test adding data that is not of String type
blockchain = BlockChain()
blockchain.add_block(2)
print(blockchain)
print(len(blockchain))


