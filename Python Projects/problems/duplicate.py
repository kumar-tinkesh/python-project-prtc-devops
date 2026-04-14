# def duplicate(lst):
#     lst.sort()
#     dup_lst = []

#     for i in range(len(lst)-1):
#         if(lst[i] == lst[i+1]):
#             if lst[i] not in dup_lst:
#                 dup_lst.append(lst[i])
#     return len(dup_lst)


def duplicate(lst):
    unq = []
    for i in range(len(lst):
        if lst[i] == lst[i+1]:
            if lst[i] not in unq:
                unq.append(lst[i])
    return len(unq)

print(duplicate([1,1,3,3, 2,2,9, 1, 5,15, 8]))
