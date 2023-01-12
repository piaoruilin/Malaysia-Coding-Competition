#setting up the arrays#
n=[]
b=[]
e=[]
m=[]
s=[]
c=[]
bma=[]
ena=[]
maa=[]
sca=[]
csa=[]
totalarray=[]
lengtharray=[]
avgarray=[]
rank=[]
sorting = []
reverse = []
tablestdnum=1
count=0

#defining what grade is (more efficient, but not used here)
#def grade(x):
#    if x>=90 and x<=100:
#        return 'A*'
#   elif x>=80 and x<90:
#        return 'A'
#   elif x>=70 and x<80:
#        return 'B'
#    elif x>=60 and x<70:
#        return 'C'
#    elif x>=50 and x<60:
#        return 'D'
#    else:
#        return 'E'

#heading#
print("STUDENT MARKS 2018")

#number of students#
students=int(input("Enter the number of students in your class: "))
if students >0:
    print('Your class has',students,'students.')
else:
    print('ERROR: Please input a valid number.')

#the questions#
for i in range(students):
    names=str(input("Student's name: "))
    print('You have 5 subjects: BM,  English, Maths, Science, Computer')
    BM=int(input('Enter BM marks: '))

    if BM <= 49:
        if BM>=0:
            bmv="E"
        else:
            bmv="Invalid!"
    elif BM <= 59:
        bmv="D"
    elif BM <= 69:
        bmv="C"
    elif BM <= 79:
        bmv="B"
    elif BM <= 89:
        bmv="A"
    elif BM <= 100:
        bmv="A*"
    else:
        print('Invalid!')
        
    English=int(input('Enter English marks: '))

    if English <= 49:
        if English>=0:
            env="E"
        else:
            env="Invalid!"
    elif English <= 59:
        env="D"
    elif English <= 69:
        env="C"
    elif English <= 79:
        env="B"
    elif English <= 89:
        env="A"
    elif English <= 100:
        env="A*"
    else:
        print('Invalid!')
    
    Maths=int(input('Enter Maths marks: '))

    if Maths <= 49:
        if Maths>=0:
            mav="E"
        else:
            mav="Invalid!"
    elif Maths <= 59:
        mav="D"
    elif Maths <= 69:
        mav="C"
    elif Maths <= 79:
        mav="B"
    elif Maths <= 89:
        mav="A"
    elif Maths <= 100:
        mav="A*"
    else:
        print('Invalid!')
    
    Science=int(input('Enter Science marks: '))

    if Science <= 49:
        if Science>=0:
            scv="E"
        else:
            scv="Invalid!"
    elif Science <= 59:
        scv="D"
    elif Science <= 69:
        scv="C"
    elif Science <= 79:
        scv="B"
    elif Science <= 89:
        scv="A"
    elif Science <= 100:
        scv="A*"
    else:
        print('Invalid!')

    Computer=int(input('Enter Computer marks: '))

    if Computer <= 49:
        if Computer>=0:
            csv="E"
        else:
            csv="Invalid!"
    elif Computer <= 59:
        csv="D"
    elif Computer <= 69:
        csv="C"
    elif Computer <= 79:
        csv="B"
    elif Computer <= 89:
        csv="A"
    elif Computer <= 100:
        csv="A*"
    else:
        print('Invalid!')

   

    
    
#storing name, score, and grade#    
    n.append(names)
    b.append(BM)
    e.append(English)
    m.append(Maths)
    s.append(Science)
    c.append(Computer)
    bma.append(bmv)
    ena.append(env)
    maa.append(mav)
    sca.append(scv)
    csa.append(csv)

#storing total and average#
    total=(BM+English+Maths+Science+Computer)
    avg=total/5

    totalarray.append(total)
    avgarray.append(avg)
    sorting.append(avg)
    reverse.append(avg)
    sorting.sort()
    reverse.sort(reverse = True)

#ranking#
def rankify(A):
     
    R = [0 for x in range(students)]
       
    for i in range(students):
        (r, s) = (1, 1)
        for j in range(students):
            if j != i and avgarray[j] > avgarray[i]:
                r += 1
            if j != i and avgarray[j] == avgarray[i]:
                s += 1      
            
           
        R = r + (s - 1) / (students)
        rank.append(R)
     
        
    return R
     

        
A= avg

        
x=(rankify(avg))


#printing the results#
print('')
print('PROGRESS REPORT')
print('====================')
print('NO.','\t','NAME','\t','BM','\t','GRD','\t','ENG','\t','GRD','\t','MATHS','\t','GRD','\t','SCI','\t','GRD','\t','COMP','\t','GRD','\t','TOT','\t','AVG','\t','POS')

for i in range(students):
    print(tablestdnum,"\t",n[count],"\t", b[count],"\t",bma[count],"\t",e[count],"\t",ena[count],"\t",m[count],"\t",maa[count],"\t",s[count],"\t",sca[count],"\t",c[count],"\t",csa[count],"\t",totalarray[count],"\t",avgarray[count],"\t",rank[count])

    tablestdnum+=1
    count+=1

#highest and lowest average#
highest = avgarray.index(max(avgarray))
lowest = avgarray.index(min(avgarray))
print('')
print(n[highest],"obtained the highest average of",reverse[0])
print(n[lowest],"obtained the lowest average of",sorting[0])
