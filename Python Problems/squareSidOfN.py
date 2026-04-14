# Square of side 'N'
def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    """
    # Your code here
    newLst = []
    res = 1;
    for i in range(n):
        newLst.append( n * '*')
    return newLst
