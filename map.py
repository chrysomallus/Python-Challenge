import string

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
transDict = {}
for i in range(97, 123):
    transDict[i] = (i + 2) % 123 + 97 * ((i + 2) // 122)

url = "http://www.pythonchallenge.com/pc/def/map.html"
print(url.translate(transDict))