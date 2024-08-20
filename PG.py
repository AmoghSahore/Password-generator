import random
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCase = "abcdefghijklmnopqrstuvwxyz"
digits = "1234567890"
specialChars = '()[]{},;._/\\?+= '

upperC, lowerC, digs, specials = True, True, True, True

all = ""

if upperC:
    all += upperCase

if lowerC:
    all += lowerCase

if digs:
    all += digits

if specials:
    all += specialChars

length = 15
password = "".join(random.sample(all, length))
print(password)