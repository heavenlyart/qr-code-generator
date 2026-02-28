a = "HI"
b = ""
b += "0100 " #for modes of text
count = bin(len(a))[2:]
if count != 8 or count <8:
    count = "0"*(8-len(count)) + count
b += count+" "
for ite in a:
    b += "0"+bin(ord(ite))[2:] + " "
b += "0000"
print(b)