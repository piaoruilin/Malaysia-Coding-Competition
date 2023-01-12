'''N = 5425327

a=11
b=9
c=20
d=20
e=25

final=1
count=0

for i in range(5,N):
    f=a+b+c+d+e
    if f%3==0:
        final+=1
    a=b
    b=c
    c=d
    d=e
    e=f

print(final)

def fibonacci(n): 
  
    a = 11
    b = 9
    c = 20
    d = 20
    e = 25
    if (n <= 1): 
        return n 
    for i in range(5, n+1): 
      
        f = a + b + c + d + e
        a = b 
        b = c
        c = d
        d = e
        e = f
      

    return f
  
# Returns true if n-th Fibonacci  
# number is multiple of 10. 
def isMultipleOf3(n): 
    kitty = fibonacci(17) 
    return (kitty % 3 == 0) 
  
# Driver code
final=[]
 
n = 17
if (isMultipleOf3(n)): 
    final.append(n)

print(len(final))'''






#another method with shorter-ass array
#INPUT
N = 5425327
 
#first 5 kitty numbers
kitty = [11, 9, 20, 20, 25] #also tried putting previous case’s last kitty numbers in here
 
ans = 1 #and previous case’s answer in here
 
#generate kitty number up till N
for i in range (5, N): #and replacing 5 with previous case’s N
   kittyNew = kitty[4] + kitty[3] + kitty[2] + kitty[1] + kitty[0]
   if kittyNew % 3 == 0:
     ans +=1
   kitty.pop(0)
   kitty.append(kittyNew)
print(ans)
