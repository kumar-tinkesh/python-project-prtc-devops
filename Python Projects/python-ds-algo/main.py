# Remove elements from a dictionary
my_dict = {'name':'Coder', 'age':29, 'course':'computer science'}
print(my_dict)
# pop
# result = my_dict.pop('courses', None)
# print(result)
# popitem
# my_dict.popitem()
# print(my_dict)
# del
# del my_dict['course']
# print(my_dict)
# clear
# my_dict.clear()
# print(my_dict)

# how to change the key
my_dict['subject'] = my_dict.pop('course')
print(my_dict)
