"""
W zadanej liscie zamien ze soba miejscami element najwiekszy i najmnijeszy
"""

x = [6, 2, 1, 9, 12, 18]

min_v = min(x)
max_v = max(x)
i_min_v = x.index(min_v)
i_max_v = x.index(max_v)
x[i_min_v] =  max_v
x[i_max_v] = min_v

i_min_v = 0
i_max_v = 0

for i, v in enumerate(x):
    if v < x[i_min_v]:
        i_min_v = i
    if v > x[i_max_v]:
        i_max_v = i
print(i_min_v, i_max_v)


#1.
temp = x[i_min_v] #wartosc minimalna
x[i_min_v] = x[i_max_v] #tu stracilem wartosc min z x
x[i_max_v] = temp
print(x)

#2.
x[i_min_v], x[i_max_v] = x[i_max_v], x[i_min_v]




