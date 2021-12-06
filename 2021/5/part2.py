import pprint

pp = pprint.PrettyPrinter(indent=4)

testInput = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

#input = testInput
file = open(r"input.txt","r")
input = file.read()
file.close()

input = input.strip().split("\n")

# Define our field as a 1Mx1M 2d array
field = [[]] * 1000
for x in range(0, len(field)):
	field[x] = [0] * 1000

goodLines = []
# strip to horiz/vert
for line in input:
	firstPos, secondPos = line.split(' -> ')
	x1, y1 = firstPos.split(',')
	x2, y2 = secondPos.split(',')

	x1 = int(x1)
	x2 = int(x2)
	y1 = int(y1)
	y2 = int(y2)
	if x1 == x2:
		if y1 > y2:
			x1,x2 = x2,x1
			y1,y2 = y2,y1
	if y1 == y2:
		if x1 > x2:
			x1,x2 = x2,x1
			y1,y2 = y2,y1

	goodLines.append({
		"pos1":{
			"x":x1,
			"y":y1
		},
		"pos2":{
			"x":x2,
			"y":y2
		}
	})

#pp.pprint(goodLines)

def printGrid(field):
	for x in range(0, len(field)):
		for y in range(0, len(field[x])):
			val = field[x][y]
			if val == 0:
				val = '.'
			print(val,end='')
		print("")

# for each input, map
for line in goodLines:
	#print(line)
	if line["pos1"]["x"] == line["pos2"]["x"]:
		#print("vertical")
		xpos = line["pos1"]["x"]
		ypos = line["pos2"]["y"]
		for x in range(line["pos1"]["y"], line["pos2"]["y"]+1):
			field[xpos][x] +=1
	elif line["pos1"]["y"] == line["pos2"]["y"]:
		#print("horiz")
		xpos = line["pos1"]["x"]
		ypos = line["pos1"]["y"]
		for x in range(line["pos1"]["x"], line["pos2"]["x"]+1):
			field[x][ypos] +=1
	else:
		#print("do diagonal", line)
		# so my new logic is to go from x1 to x2, cuz since we have a 45 degree diag, there should be the same
		# of steps - i'll also note if x is going up or down and y ditto. this feels lame
		# btw - looking at the logic now, i think diagonal would work for all and make things MUCH simpler
		# but im being lazy
		xDir = 1
		yDir = 1

		if line["pos1"]["x"] > line["pos2"]["x"]:
			xDir = -1
		if line["pos1"]["y"] > line["pos2"]["y"]:
			yDir = -1
		total = abs(line["pos1"]["x"] - line["pos2"]["x"])

		current = {
			"x":line["pos1"]["x"],
			"y":line["pos1"]["y"]
		}

		for x in range(0, total+1):
			field[current["x"]][current["y"]] += 1
			current["x"] += xDir
			current["y"] += yDir

	#printGrid(field)

# count bad
bad = 0	
for x in range(0, len(field)):
	for y in range(0, len(field[x])):
		if field[x][y] >= 2:
			bad += 1

#7219 is too low
print("Bad", bad)
