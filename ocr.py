file = open("ocrinput.txt", "r")

txt = file.read()
countDict = {}
for i in range(len(txt)):
    if txt[i] in countDict:
        countDict[txt[i]] = countDict[txt[i]] + 1
    else:
        countDict[txt[i]] = 1
uniqueChars = ""
for i in countDict:
    if countDict[i] == 1:
        uniqueChars += i
print(uniqueChars)