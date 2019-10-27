

dane = (1, 2, 3, 4, 5)

def sumator(*args, **kwargs):     #taka funckja moze przyjac dowolna liczbe argumentow
    print("args", args)
    print("kwargs", kwargs)
    return sum(args)

print(sumator())
print(sumator(1))
print(sumator(1, 10, 100))
print(sumator(*dane))

print(sumator(a=1, b=2))