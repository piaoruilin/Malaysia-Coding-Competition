students = [[],[],[],[]]
males = [[],[],[]]
females = [[],[],[]]
array = [students, males, females]
array_2 = ["All Students", "Males", "Females"]

for i in range (4) :
    gender = input("Enter your gender [M/F]")
    while gender not in ("M", "F") :
        gender = input("Try Again \nEnter your gender [M/F]")
    students[3].append (gender)

    original = input("Enter your original height : ")
    while original.isdigit() is False :
        original = input("Try Again \nEnter your original height : ")
    students[0].append (int(original))

    new = input("Enter your new height : ")
    while new.isdigit() is False :
        new = input("Try Again \nEnter your new height : ")
    students[1].append (int(new))

    change = int(new) - int(original)
    students[2].append(change)

    if gender == "M" :
        males[0].append (int(original))
        males[1].append (int(new))
        males[2].append (change)
    elif gender == "F" :
        females[0].append (int(original))
        females[1].append (int(new))
        females[2].append (change)
    else :
        print("Try Again")

for y in range (4) :
    print(y+1,""*(4 - len(str(students[0][y],""*(13 - len(str(students[1][y]))), students[1][y],""*(14 - len(str(students[1][y]))), students[2][y])

for z in range (3) :
    x = array[z]
    print("\nAverage height change for", array_2[z], (sum(x[2]))/(len(x[2])))
    print("Largest height change for", array_2[z], max(x[2]))
    print("Smallest height change for", array_2[z], min(x[2]))
