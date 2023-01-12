#MISSING NUMBERS (FALIED ATTEMPT)
'''
n=5
array=[-1,7,4,1]
original_array=[]
a=(-3)*n
b=(3)*n
r=(2*b)+1
i=0

for i in range(r):
    num=a+i
    original_array.append(num)
    i+=1
    if original_array[-1]==b:
        break

counter=0
for counter in range(len(array)):
	original_array.remove(array[counter])
	
print(original_array)
print(sum(original_array))
'''
#==================================================================================
#CIPHER
S = "qutptplhirrkady"
K = 956580
A = "mibnhxsztldkrjagywuopcfqve"
B = "dsrwikfcohxjtpveyumbnlqgza"

i=0
s = list(S)
a = list(A)
b = list(B)
for x in range (K):
    for i in range (len(s)):
    	s[i] = b[a.index(s[i])]
finalString = ''.join(s)
print(finalString)
