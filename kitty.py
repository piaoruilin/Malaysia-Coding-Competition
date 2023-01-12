
kitty=[11,9,20,20,25]
i=0

N = 17

r=N-5

for i in range(r):
    a=kitty[-1]+kitty[-2]+kitty[-3]+kitty[-4]+kitty[-5]
    kitty.append(a)

print(kitty)

for i in range(r):
    a=kitty[i]+kitty[i+1]+kitty[i+2]+kitty[i+3]+kitty[i+4]
    kitty.append(a)

count=0
final=0
for count in range(N):
    if (kitty[count])%3==0:
        final=final+1

print(final)

		
