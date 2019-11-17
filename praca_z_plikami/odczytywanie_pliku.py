# try:
#     plik = open("nazwa_pliku.txt")
#     1/0
# except:
#     pass
# finally:
#     plik.close()


#context manager
# with open("nazwa_pliku.txt") as fh:
#     for line in fh.read().splitlines():
#         print(line)

with open("nazwa_pliku.txt") as fh:
    print(fh.read())

# with open("nazwa_pliku.txt") as fh:
#     for line in fh:
#         print(line, end="")

with open("text.txt", "w") as fh:
    fh.write("Ala")