g = {}
X = [] #Vertex processed so far
A = {} #Compute shortest path

with open('dijkstraData.txt', 'r') as inputFile:
	for line in inputFile:
		ints = [x for x in line.split()]
		g[int(ints[0])] = {}
		for x in ints[1:]:
			vd = [int(i) for i in x.split(',')]
			g[int(ints[0])][vd[0]] = vd[1]

X.append(1)
A[1] = 0
myDict = {}

for i in range(1, len(g)):
	#Finding the neighbor with minimum distance
	for v in X:
		temp = {A[v]+g[v][neighbor]: neighbor for neighbor in g[v].keys() if neighbor not in X}
		if temp != {}:
			myDict[min(temp)] = temp[min(temp)]
	#Adding neighbor to Visited list (X)
	X.append(myDict[min(myDict)])
	#Assigning the minimum distance
	A[myDict[min(myDict)]] = min(myDict)
	myDict = {}

print A