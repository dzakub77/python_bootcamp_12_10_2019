
sum = 0
x = 0
while x < 7:
    temp = int(input("Wprowadz temperature: "))
    x += 1
    sum += temp
sr = sum/7
print("Srednia temperatura z 7 ostatnich dni wynosi", sr," stopni")