from block import Block

class Chain:
    def __init__(self):
        self.block_chain = []

    def append_genesisblock(self, block):
        if (len(self.block_chain) == 0 and block.index == 0):
            self.block_chain.append(block)
            print(block.current_block)

    def append_block(self, block):
        if (len(self.block_chain) == block.index and block.prev_block == self.block_chain[len(self.block_chain)-1].current_block):
            self.block_chain.append(block)
            print("new block", self.block_chain[len(self.block_chain)-1].current_block)
        else:
            print("len:", len(self.block_chain))
            print("index", block.index)
            print("new block's prev_block", block.prev_block)
            print("chain's current_block", self.block_chain[len(self.block_chain)-1].current_block)