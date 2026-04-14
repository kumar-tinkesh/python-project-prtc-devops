# Build sum elements of a list function. like sum() builtin function

class SumError(Exception):
    """Raised when an error arises during sum_seq."""
    def __init__(self):
        self.error="error printing."


def sum_seq(seq: list  | tuple, start: int | float =0) -> int | float:
    """
        return the total of sequence, plus the optional start params
    """
    total = 0
    if not isinstance(start, (int, float)):
        raise SumError("Start Must be an Int or float")
    for num in seq:
        try:
            total += num
        except TypeError as e:
            raise SumError(e)
    
    return total+start


x = [1,2,3,4, 5]

z= sum_seq(x, start=1)
print(z)