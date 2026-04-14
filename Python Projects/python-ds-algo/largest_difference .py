# largest_difference 
# [1,2,3,4,5]

def largest_difference(lst):
    large = lst[0]
    small = lst[0]
    for i in lst:
        if i > large:
            large = i 
        elif i < small:
            small = i
    
    return large - small 

lst = [70,60,75,20,99,10]

print(largest_difference(lst))

