# check if two strings are angram or not
# angram is when two string has same letters but a diffrnt word
# typhoon and opython
# night anf thing
# clinteastwood and westoldaction

# let's do it

def is_anagram(str1, str2):
    # sort the strings
    str1 = sorted(str1)
    str2 = sorted(str2)
    # check the length
    if len(str1) == len(str2):
        # check the strings
        if str1 == str2:
            return True
        return False

# let's try now
print(is_anagram('typhoon','opython'))
print(is_anagram('listen','silent'))

# tha's all 
# Thank you
