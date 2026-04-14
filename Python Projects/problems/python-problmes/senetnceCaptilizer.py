def senetenceCapitalizer(str):
    lst = []
    s = str.split(" ")
    for i in s:
        lst.append(i.capitalize())
        cap_s = " ".join(lst)
    return cap_s




sen = input("enter your sentence:  ")
print(senetenceCapitalizer(sen))