

list = [1, 23, 14, 16, 33, 55, 77]
i = 0

while True:
    print(list)
    i = int(input("Ktory element chcesz wyswietlic?: "))
    try:
        print(f"Elementem {i} w liscie jest: ", list[i])
    except:
        print("Ten element nie miesci sie w liscie")
        break
     #if i > len(list):
    #    break
    #print(f"Elementem {i} w liscie jest: ", list[i])
print("sadasf")




