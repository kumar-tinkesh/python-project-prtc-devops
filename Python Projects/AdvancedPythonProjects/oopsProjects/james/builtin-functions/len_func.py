#  building an length function 

class LengthError(Exception):
    """Raise an error when attributes not found"""

        
def len_seq(seq):
    """Return the length of a sequence"""
    if hasattr(seq, '__len__'):
        return seq.__len__()
    raise LengthError(f"{type(seq)} has no __len__ attribute")
    


lst = [5,6,8,9]  
num = 25

print(len(lst))
print(len_seq(lst))



