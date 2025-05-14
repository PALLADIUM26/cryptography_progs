p = "" #stores resultant plain text
c = input() #stores input cipher text
k = 0 #key value

for k in range(25):
    p = ""
    for i in c:
        p1 = ord(i)-65
        p2 = (p1-k)%26
        p3 = p2+97
        p += chr(p3)
    print(p)
