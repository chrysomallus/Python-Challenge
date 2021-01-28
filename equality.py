import re

file = open("equality.txt", "r")
txt = file.read()
cases = re.findall("[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]", txt)

returnString = ""
for i in cases:
    returnString += i[4]

print(returnString)