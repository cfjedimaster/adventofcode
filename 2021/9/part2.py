testinput = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""

# Parse data
file = open(r"input.txt","r")
input = file.read()
file.close()

#input = testinput
input = input.strip()

ground = []
rows = input.split("\n")
for row in rows:
	ground.append([])
	for part in row:
		ground[len(ground)-1].append(int(part))

def getLowPoints(ground):
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
				lowPoints.append({"height":locHeight,"x":x,"y":y})

			y = y+1

		x = x+1
		y = 0

	return lowPoints

def usedCoordListCheck(l,x,y):
	for loc in l:
		if loc["x"] == x and loc["y"] == y:
			return True
	return False

"""
Recursive func to get a size for a basin. Bug I ran into is that I sometimes tried to 
get the same size for a thing I already had
"""
def getBasinSize(ground, h, x, y, used=[]):
	size = 1
	#print("get for",x,y,"height of",h)
	"""
	check everyone around me. if > me and NOT 9, +1 to size and recurse call
	"""
	if x >= 1:
		if ground[x-1][y] > h and ground[x-1][y] != 9:
			if usedCoordListCheck(used, x-1, y) == False:
				used.append({"x":x-1, "y":y})
				size += getBasinSize(ground, ground[x-1][y], x-1, y, used)  
	# only check above if not at top
	if y >= 1:
		if ground[x][y-1] > h and ground[x][y-1] != 9:
			if usedCoordListCheck(used, x, y-1) == False:
				used.append({"x":x, "y":y-1})
				size += getBasinSize(ground, ground[x][y-1], x, y-1, used) 
	# only check right if not at end
	if x < len(ground)-1:
		if ground[x+1][y] > h and ground[x+1][y] != 9:
			if usedCoordListCheck(used, x+1, y) == False:
				used.append({"x":x+1, "y":y})
				size += getBasinSize(ground, ground[x+1][y], x+1, y, used) 
	# only chek bottom if not at bottom
	if y < len(ground[x])-1:
		if ground[x][y+1] > h and ground[x][y+1] != 9:
			if usedCoordListCheck(used, x, y+1) == False:
				used.append({"x":x, "y":y+1})
				size += getBasinSize(ground, ground[x][y+1], x, y+1, used) 
	#print("returning size",size, "my height was ",h)
	return size


lowPoints = getLowPoints(ground)	
print("i've determined the low points, there are", len(lowPoints))

sizes = []
for lp in lowPoints:
	size = getBasinSize(ground, lp["height"], lp["x"], lp["y"])
	#print("size was ",size)
	sizes.append(size)

#print("should be 3:")
#print(getBasinSize(ground, lowPoints[0]["height"], lowPoints[0]["x"], lowPoints[0]["y"]))

#print("should be 9:")
#print(getBasinSize(ground, lowPoints[1]["height"], lowPoints[1]["x"], lowPoints[1]["y"]))

#print("should be 14:")
#print(getBasinSize(ground, lowPoints[2]["height"], lowPoints[2]["x"], lowPoints[2]["y"]))

sizes.sort(reverse=True)
print(sizes)

topThree = sizes[0] * sizes[1] * sizes[2]
print(topThree)