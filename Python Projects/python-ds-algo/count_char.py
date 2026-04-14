# count characters in a word

def count_characters(word):
    output = {}
    for char in word:
        if char not in output:
            output[char] = 1
        else:
            output[char] += 1

    return output
        


print(count_characters('loop'))