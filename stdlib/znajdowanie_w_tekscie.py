import re

with open('input.txt') as f:
    pattern_data = "\d{2} [a-zA-Z]+ \d{4}"
    pattern_kod_pocztowy = "\d{2}\-\d{3}"
    pattern_email = "[\w\.\-]+@(?:\w+\.)+\w+"
    patern = re.compile(pattern_data)
    patern2 = re.compile(pattern_email)
    patern3 = re.compile(pattern_kod_pocztowy)
    line = f.read()
    print(patern.findall(line))
    print(patern2.findall(line))
    print(patern3.findall(line))
