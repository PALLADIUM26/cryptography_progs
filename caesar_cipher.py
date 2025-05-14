p = input() #stores input plain text
c = "" #stores resultant cipher text
k = 3 #key value

for i in p: #traversing i/p
    if i!=' ': #ignoring space
        #cipher generation
        c1 = ord(i)-97
        c2 = (c1+k)%26
        c3 = c2+65
        c = c + chr(c3)

print(c)