option = int(input("Which version do you want? [1/2] : "))
if option == 1 :
    total_sum = 0
    for i in range(1,1000) :
        if (i%3 == 0 and i%5 == 0):
            total_sum = total_sum + i
    print(total_sum)
elif option == 2 :
    total_sum = 0
    for i in range(1,1000) :
        if (i%3 == 0 or i%5 == 0) :
            total_sum = total_sum + i
    print(total_sum)
    

    
             




