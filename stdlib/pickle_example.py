

text = 'Zażółć gęślą jaźń'
with open("text.txt", 'wb') as f:
    f.write(text.encode())

with open("text.txt", 'rb') as f:
   # print(f.read())
    print(f.read().decode())