from creatingBlockChain import Block

block = Block("blockchain")
block.mine(10)

print(block.hash.hexdigest())