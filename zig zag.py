# FUNCTIONS FOR GENERATING ALL SUBSETS OF LENGTH K
import numpy as np
 
 
def zigzag(data, r):
   updown = np.resize([-1,1], r)
   updown[0] = 0
   downup = np.resize([1,-1], r)
   downup[0] = 0
   zigzagArr = [0] * r
  
   for i in range (r-1):
       if data[i+1] > data[i]:
           zigzagArr[i+1] = 1
       elif data[i+1] < data[i]:
           zigzagArr[i+1] = -1
       else:
           zigzagArr[i+1] = 0
       if np.all(zigzagArr == updown) or np.all(zigzagArr == downup):
           ans.append(1)
def combinationUtil(arr, n, r, index, data, i):
   if(index == r):
       zigzag(data, r)
       return
   if(i >= n):
       return
   data[index] = arr[i]
   combinationUtil(arr, n, r,index + 1, data, i + 1)
   combinationUtil(arr, n, r, index,data, i + 1)
def printcombination(arr, n, r):
   data = list(range(r))
   combinationUtil(arr, n, r, 0, data, 0)
 
#<-- INPUT -->
S = "wxrttjey"
K = 3
 
# CONVERT LETTERS TO NUMBERS
ans = []
sArr = list(S)
alphaArr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numArr = []
for i in range (len(S)):
   numArr.append(alphaArr.index(sArr[i]))
 
# GENERATE ALL SUBSETS OF LENGTH K
printcombination(numArr, len(S), K)
print(len(ans))
