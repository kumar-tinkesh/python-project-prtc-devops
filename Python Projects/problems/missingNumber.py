def missingNumber(lst):
    missingNum = []
    for i in range(lst[0], lst[-1]):
        if i not in lst:
            missingNum.append(i)
    return missingNum
    

    
print(missingNumber([0,1,2,4,5,6,8]))
print(missingNumber([4,5,6,8, 10]))
print(missingNumber([5,6,8, 11]))
