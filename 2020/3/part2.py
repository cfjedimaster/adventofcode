# So for this one, I take N slopes, take the result, and multiple them
# So I took my code from part1 and turned it into a function

file = open(r"input.txt","r")

input = []
for line in file:
	input.append(line)

file.close()


def numTrees(right,down):
	# my position top left
	posX = 0
	posY = 0

	# my slope is right 3 and down 1
	slopeRight = right
	slopeDown = down

	# I loop until posY is 'below' the bottom, so lets figure that out
	height = len(input)
	# due to arrays being 0 index, when we get to height, we are done

	# ok, so loop and move our position
	# to handle repeating a row, I considered taking the row and making 100 copies of it, a brute force version,
	# but instead, we should be able to mod, right? so if my str is 4 chars long, pos 10 is 2. i think :)

	# this is because i know my code is going to suck at first and loop forever
	#sanity = 0

	treesHit = 0

	while posY < (height-1):
		posY = posY + slopeDown
		posX = posX + slopeRight

		row = input[posY].rstrip()
		#print('row',row, len(row))

		#print('currently at ',posX,posY)

		# get the object there
		relX = posX % len(row)
		#print('relX', relX)
		charAt = row[relX]
		#print('charAt',charAt)
		if charAt == '#':
			treesHit = treesHit + 1

	return treesHit

print('3,1',numTrees(3,1))
print('1,1',numTrees(1,1))
print('5,1',numTrees(5,1))
print('7,1',numTrees(7,1))
print('1,2',numTrees(1,2))

# I multipled the results with my calculator 3,847,183,340
# nah, dont be lazy ray

answer = numTrees(3,1) * numTrees(1,1) * numTrees(5,1) * numTrees(7,1) * numTrees(1,2)
print('Puzzle solution', answer)