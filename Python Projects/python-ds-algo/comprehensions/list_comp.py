names = ['james', 'sally', 'marko','rajeev']
initals = [name[0]+name[-1] for name in names]

print(initals)

names = [('james', 'allan'), ('sally', 'rain') ,('marko','robbinson'),('rajeev','sen')]

new_initials = [name[0][0] + name[1][0] for name in names]

print(new_initials)

cities = ['liverpol', 'london','otawa','orange']
cities_2 = [city.replace('o','oo') for city in cities if city]

print(cities_2)


def half_double(n):
    try:
        return n*2 if n>10 else n / 2
    except:
        return 0
    
x = [half_double(n) for n in ('baba', 1,11)]
print(x)