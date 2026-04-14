#  find the target sum from array
# [2,4,5,9] ==> 9 
#  [4,5] ==> index [1,2]


def findTwoSums(lst, target):
    sum = 0
    for i in range(len(lst)+1):
        sum = lst[i] + lst[i+1]
        if sum == target:
            return i, i+1
        


print(findTwoSums([2,4,5,9], 9))
print(findTwoSums([2,7, 11, 15], 9))
print(findTwoSums([3,2,4], 6))
