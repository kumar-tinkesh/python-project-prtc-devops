def generate_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    pattern = []
    traingle = []
    
    # first way of doing
    res = '*'
    for i in range(n):
            pattern.append(res)
            res += '*'

    # second way of doing
    for i in range(1, n+1):
          traingle.append('*' * i)

    return pattern, traingle

print(generate_triangle(3))
print(generate_triangle(5))