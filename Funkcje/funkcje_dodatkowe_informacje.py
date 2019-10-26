a= 10

def foo():

    def bar():
        print("Jestem funckją wewnetrzna")


    global a
    a = 1
    print(a)


foo()


lambda x: x**2   # == def square(x): return x**2

sq = lambda x: x**2
print(sq(4))

def drugi(x):
    return x[1]

x = ["c1", "b12", "a3"]
print(sorted(x, key=drugi))
print(sorted(x, key=lambda x: int(x[1])))
