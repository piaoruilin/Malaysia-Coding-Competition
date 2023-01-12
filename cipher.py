
#copy and paste the question here
S = "ctej"
K = 2
A = "zyxwvutsrqponmlkjihgfedcba"
B = "cbafedihglkjonmrqputsxwvzy"

C = "abcdefghijklmnopqrstuvwxyz" #new, alphabetical reference
D = "abcdefghijklmnopqrstuvwxyz" #new map

#turn strings into lists
s = list(S)
a = list(A)
b = list(B)
c = list(C)
d = list(D)
y = list(s)

for i in range (K):
    for j in range (26):
        d[j] = b[a.index(d[j])]

for k in range (len(s)):
    s[k] = d[c.index(s[k])]

finalString = ''.join(s)
print(finalString)
