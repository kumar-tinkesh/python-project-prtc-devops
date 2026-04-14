def sentenceCapitalizer(string):
    lst = []
    s = string.split(' ')
    for i in s:
        lst.append(i.capitalize())
    return ' '.join(lst)
        
        
        

print(sentenceCapitalizer("This isn't what I ask for? I'm not buying it. "))