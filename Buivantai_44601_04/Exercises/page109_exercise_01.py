"""
Authon: Bui Van Tai
Date:25/09/2021

problem:Write the encrypted text of each of the following words using a Caesar cipher with
a distance value of 3:
a. python
b. hacker
c. wow

solution:
a,plainText = input("python: ")
distance = int(input("3: "))
code = ""
for ch in plainText:
        ordValue = ord(ch)
        cipherValue = ordValue + distance
        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - \
                          (ord('z') - ordvalue + 1)
        code += chr(cipherValue)
print(code)
b.plainText = input("hacker: ")
distance = int(input("3: "))
code = ""
for ch in plainText:
        ordValue = ord(ch)
        cipherValue = ordValue + distance
        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - \
                          (ord('z') - ordvalue + 1)
        code += chr(cipherValue)
print(code)
c.plainText = input("wow: ")
distance = int(input("3: "))
code = ""
for ch in plainText:
        ordValue = ord(ch)
        cipherValue = ordValue + distance
        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - \
                          (ord('z') - ordvalue + 1)
        code += chr(cipherValue)
print(code)
"""
