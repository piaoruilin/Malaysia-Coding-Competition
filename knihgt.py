#INPUT
T = 3
cases = [[2, 0, 0, 3, 3], [5, -2, -2, 100, 100], [2, 0, 0, 1, 2]]

#KNIGHT MOVEMENTS
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

#Array for YES or NO answer
yesOrNo = ["DUNNO" for i in range (len(cases))]

#Arrays for states
queue = []
visited = []

for i in range (len(cases)):
    #define origin and target
    origin = [cases[i][1], cases[i][2], 0]
    target = [cases[i][3], cases[i][4], cases[i][0]]
    
    #add origin to queue
    queue.append(origin)
    depth = 0
    
    while queue != [] and queue[0][2] < target[2]:
        for j in range (8):
            x = queue[0][0] + dx[j]
            y = queue[0][1] + dy[j]
            depth = queue[0][2] + 1
            if [x, y, depth] not in visited:
                queue.append([x,y, depth])
            visited.append(queue[0])
            queue.pop(0)
    if target in queue:
    	yesOrNo[i] = "YES"
    else:
        yesOrNo[i] = "NO"
finalString = '\n'.join(yesOrNo)
print(finalString)
