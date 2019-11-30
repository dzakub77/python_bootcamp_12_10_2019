import re

test_data = """123 23 123;123 123 123; 23 23 23;999 999 999"""
test_data2 = "123 123 123"
test_data3 = """123 23 123;123 111 123; 23 23 23;999 999 999"""
phone_prattern = "\d{3} \d{3} \d{3}"

patern = re.compile(phone_prattern)
print(patern.match(test_data2))
print(patern.search(test_data3))
print(patern.findall(test_data))
print(patern.finditer(test_data))