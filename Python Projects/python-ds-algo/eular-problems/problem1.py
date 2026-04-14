# sum of multiples 
sum_total = 0 
for i in range(1, 1000):
    # is i divisible evenly 
    if(i % 3 == 0 or i % 5==0):
        sum_total+=i
        print(f"{i} is divisable by 3 or 5")
    #
# print(sum_total)

total = sum([i for i in range(1, 1000) if(i % 3 == 0 or i % 5==0)])
print(total)