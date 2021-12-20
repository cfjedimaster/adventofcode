testinput = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""

file = open(r"input.txt","r")
input = file.read()
file.close()

input = input.strip()

ground = []
rows = input.split("\n")
for row in rows:
	ground.append([])
	for part in row:
		ground[len(ground)-1].append(int(part))

x=0
y=0
lowPoints = []

while x < len(ground):
	while y < len(ground[x]):
		locHeight = ground[x][y]
		#print("Working with ",x,",",y, " = ",locHeight)
		# check for 4 (at most) blocks around me
		isLow = True 
		# only check left if not at left
		if x >= 1:
			if ground[x-1][y] <= locHeight:
				isLow = False
		# only check above if not at top
		if y >= 1:
			if ground[x][y-1] <= locHeight:
				isLow = False
		# only check right if not at end
		if x < len(ground)-1:
			#print("debug rigt check", ground[x+1])
			#print("y is",y)
			#print("val i checked is", ground[x+1][y])
			if ground[x+1][y] <= locHeight:
				isLow = False
		# only chek bottom if not at bottom
		if y < len(ground[x])-1:
			if ground[x][y+1] <= locHeight:
				isLow = False

		if isLow:
			lowPoints.append(locHeight)

		y = y+1

	x = x+1
	y = 0

#print(lowPoints)
riskSum = 0
for p in lowPoints:
	riskSum += (p+1)

# 1830 is too high
print(riskSum)