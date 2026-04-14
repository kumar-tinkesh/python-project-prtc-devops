#Hollow Square of side 'N'
def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.

    Input: 3
    Output: ['***', '* *', '***']
    """
    newLst = []
    if n == 1:
        return ['*']
    
    newLst.append(n * '*')
    for i in range(n-2):
        newLst.append('*' + ' ' * (n-2) + '*')

    newLst.append('*' * n)
    
    return newLst


print(generate_hollow_square(3))