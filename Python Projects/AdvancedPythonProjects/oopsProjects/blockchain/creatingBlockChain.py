import hashlib

class Block:
    def __init__(self, data):
        self.hash = hashlib.sha256()
        self.nonce = 0  # number to be incremented to generate hash
        self.data = data

    # hashing a block
    def mine(self, diffculty):
        self.hash.update(str(self).encode('utf-8'))
        # update the hash object
        while int(self.hash.hexdigest(), 16) > 2 ** (256-diffculty):
            # hexdigest return string object of double length containing hexadecimal
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf-8'))
            # utf-8 translate any Unicode character to a matching unique binary string

    
    def __str__(self):
        return "{}{}".format(self.data, self.nonce)



class Chain():
    def __init__(self, diffculty):
        self.diffculty = diffculty
        self.blocks = []
        self.pool = []
        
    def proof_of_work(self, block):
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        # return block.hash.hexdigest() = h.hexdigest() and
