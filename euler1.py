i = 0
lst = []
num = list(range(1,1001))
for number in num :
    if number%3 == 0 and number%5 == 0 :
        lst.append(number)
print(sum(lst))

