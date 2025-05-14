p = "attack postponed to tomorrow and do not use our secret paper until further info"
key = "the quick brown fox jumps over the lazy dog"
c = ""

k = dict()
ind = 0
l = []
for i in key:
    if i not in k:
        k[i] = ind
        l.append(i)

l2 = len(l)
d = dict()
ind = 0
for i in p:
    if i not in d:
        d[i] = l[ind]
        c += d[i]
    else:
        c += d[i]
    ind += 1
    if ind == l2:
        ind = 0

print(c)