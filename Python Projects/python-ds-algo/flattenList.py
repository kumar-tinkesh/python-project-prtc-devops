# flatten a list with nested list
# from [[1,2],[3,4]]
# to [1,2,3,4]

# let's do it

def flatten_list(lst):
    # create a new empty list
    newLst = []
    # loop over list
    for sublst in lst:
        # again loop over sublst
        for sub in sublst:
            newLst.append(sub)
    return newLst


# let's try
l = [[1,2],[3,4],[5,6]]
print(flatten_list(l))

# thank you
