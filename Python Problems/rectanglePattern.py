def generate_ractangle(n, m):
    newLst = []
    res = 1;
    for i in range(n):
        newLst.append( m * '*')
    return newLst



print(generate_ractangle(4,5))
print(generate_ractangle(3, 2))