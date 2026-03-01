# a = "HI"
# b = ""
# b += "0100 " #for modes of text
# count = bin(len(a))[2:]
# if count != 8 or count <8:
#     count = "0"*(8-len(count)) + count
# b += count+" "
# for ite in a:
#     b += "0"+bin(ord(ite))[2:] + " "
# b += "0000"
# print(b)


a = "HI"
b = ""
b += "0100" #for modes of text
count = bin(len(a))[2:]
if count != 8 or count <8:
    count = "0"*(8-len(count)) + count
b += count+""
for ite in a:
    b += "0"+bin(ord(ite))[2:] + ""
b += "0000"
# print(b)
while len(b) % 8 != 0:
    b += "0"

padding =  ["11101100", "00010001"]
index = 0
while len(b) < 208:
    b += padding[index%2]
    index+=1
    
print(b)