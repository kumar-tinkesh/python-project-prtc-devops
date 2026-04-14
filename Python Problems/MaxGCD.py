#  find the hihgest GCD for two numbers

def findMaxGCD3(number1, number2):
    commonFactor = 0;
    # min baecause factor will not be greater than number1
    for i in range(1, min(number1, number2)):
        if number1 % i ==0 and number2 % i == 0:
            commonFactor=i

    return commonFactor


print(findMaxGCD3(14,96))


# def findMaxGCD2(number1, number2):
#     gcdLst = []
#     # min baecause factor will not be greater than number1
#     for i in range(1, min(number1, number2)):
#         if number1 % i ==0 and number2 % i == 0:
#             gcdLst.append(i)

#     return gcdLst[-1]


# print(findMaxGCD2(14,63))




# def findMaxGCD(number1, number2):
#     fnum1= []
#     for i in range(1, number1+1):
#         if number1 % i ==0:
#             fnum1.append(i)

#     fnum2= []
#     for i in range(1, number2+1):
#         if number2 % i ==0:
#             fnum2.append(i)
#     fnum3=[]
#     for i in fnum1:
#         if i in fnum2:
#             fnum3.append(i)
    
#     return fnum3[-1]


# print(findMaxGCD(14, 63))
