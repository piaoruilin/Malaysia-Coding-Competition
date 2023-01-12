import itertools
#Generate Sub Sequences Function
def SubSequences(STR):
   global combs
   combs = [[()]]
   for l in range(1, len(STR)+1):
       combs.append(list(itertools.combinations(STR, l)))
 
# <-- INPUT -->
N = 13
Numbers = [3, -1, -12, 6, 11, -7, 9, -10, 2, -5, 8, 13]

#sort Numbers
Numbers.sort()
 
#set ans
ans = 0
 
#array for numbers from 1 to N
arr = []
for i in range (1,N+1):
   arr.append(i)
 
#generate and define K
K = []
for i in range (-N*3, N*3+1):
   K.append(i)
 
#[1] REMOVE 1 NUMBER
for i in range (N):
   removedArr = arr.copy()
   removedArr.pop(i)
   #[2] MAKE SOME NUMBERS NEGATIVE
   SubSequences(removedArr)
   for j in range (len(combs)):
       for k in range (len(combs[j])):
           negArr = removedArr.copy()
           for l in range (len(combs[j][k])):
               negArr[negArr.index(combs[j][k][l])] = -combs[j][k][l]
           #[3] ADD k
           for m in range (len(K)):
               addedArr = [z+K[m] for z in negArr]
               addedArr.sort()
               #[4] CHECK IF MATCHES
               if addedArr == Numbers:
                   ans += i+1
print("ans:", ans)
