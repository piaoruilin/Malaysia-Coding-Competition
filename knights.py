'''
def knights_moves():
  a = []
  b = (1, 2)
  while 1:
    a.append(b)
    b = (-b[0], b[1])
    a.append(b)
    b = (b[1], b[0])
    if b in a:
      return a

T = 3
cases = [[2, 0, 0, 3, 3], [5, -2, -2, 100, 100], [2, 0, 0, 1, 2]] #[[steps, x-source, y-source, x-dest, y-dest]]

first=[]
last=[]

first.append(cases[0][1])
first.append(cases[0][2])

last.append(cases[0][3])
last.append(cases[0][4])

print(first)
print(last)
'''
#Find number of possible moves of knight 
n = 4; 
m = 4; 

# To calculate possible moves 
def findPossibleMoves(mat, p, q): 
	global n, m; 
	
	# All possible moves of a knight 
	X = [2, 1, -1, -2, -2, -1, 1, 2]; 
	Y = [1, 2, 2, 1, -1, -2, -2, -1]; 

	count = 0; 

	# Check if each possible move 
	# is valid or not 
	for i in range(8): 
		
		# Position of knight after move 
		x = p + X[i]; 
		y = q + Y[i]; 

		# count valid moves 
		if(x >= 0 and y >= 0 and x < n and
		y < m and mat[x][y] == 0): 
			count += 1; 

	# Return number of possible moves 
	return count; 

# Driver code 
if __name__ == '__main__': 
	mat = [[1, 0, 1, 0], [0, 1, 1, 1], 
		[1, 1, 0, 1], [0, 1, 1, 1]]; 

	p, q = 2, 2; 

	print(findPossibleMoves(mat, p, q)); 

# This code is contributed by 29AjayKumar 

