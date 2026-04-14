# check if a list has duplicate items or not
# if duplicate return True

def duplicate_items(lst):
    # create a new empty list
    newLst = []
    # iterate over the list 
    for i in lst:
        # check if element is in new list or not
        if i in newLst:
            # return true if item in newLst
            return True
        # append all elemnets one by one in the newlst
        newLst.append(i)
    return False 

# Let's try
lst = [1,2,3,4,5,6, 7, 6, 7, 50]
print(duplicate_items(lst))
# it is working 

# now remove the duplicates 

def remove_duplicate(lst):
    newLst = []
    for i in lst:
        if i not in newLst:
            newLst.append(i)
    return newLst
print(remove_duplicate(lst))

# Thank you