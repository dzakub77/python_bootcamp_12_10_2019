
a = [9, 1, 6, 8, 4, 3, 2, 0]

for i in range(len(a)):
    #print(a[i:])
    index_min = i
    for j in range(i, len(a)):
        #print(a[j], end = " ")
        if a[j] < a[index_min]:
            index_min = j
    a[i], a[index_min] = a[index_min], a[i]
    print(a)


assert a == [0, 1, 2, 3, 4, 6, 8, 9] #assert sposob na sprawdzenie, jesli nie jest spelniony dostaniemy blad
