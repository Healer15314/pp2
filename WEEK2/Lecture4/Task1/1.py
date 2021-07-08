  
import re

file = open('raw.txt',encoding="utf8")
text = file.read()

BINPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"
BINText = re.search(BINPattern, text).group("BIN")
NamePattern = r"\nФилиал.*(?P<Name>\b[A-Z]+)"
NameText = re.search(NamePattern, text).group("Name")
itemPatternText = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern = re.compile(itemPatternText)

print(NameText)
print(BINText)
for m in re.finditer(itemPattern, text):
    print(m.group("name") + "\n" + " " + m.group("count")+ "\n" + m.group("price") + "\n"+ m.group("total1"))
TimePattern = r"\nВремя: (?P<Time>\b[0-9].*\n{1}(?P<Address>.*))"
Datetext = re.search(TimePattern, text).group("Date")
AddressText = re.search(TimePattern, text).group("Address")
print(Datetext)
file.close()