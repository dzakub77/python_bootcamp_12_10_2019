x = int(input("Podaj położenie x: "))
y = int(input("Podaj położenie y: "))

if x <= 10 and y <= 10:
    print("LDR")
elif x <= 10 and y > 10 and y < 90:
    print("LK")
elif x <= 10 and y >= 90:
    print("LGR")
elif x > 10 and x < 90 and y > 90:
    print("GK")
elif x >= 90 and y >= 90:
    print("PGR")
elif x >= 90 and y > 10 and y < 90:
    print("LK")
elif x >= 90 and y <= 10:
    print("PDR")
elif x > 10 and x < 90 and y <= 10:
    print("DK")
elif x > 10 and x < 90 and y > 10 and y < 90:
    print("Centrum")
