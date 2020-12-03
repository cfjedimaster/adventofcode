# sample data
raw = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

raw = raw.strip()

#input = raw.splitlines()

file = open(r"input.txt","r")

input = []
for line in file:
	input.append(line)

file.close()

# my position top left
posX = 0
posY = 0

# my slope is right 3 and down 1
slopeRight = 3
slopeDown = 1

# I loop until posY is 'below' the bottom, so lets figure that out
height = len(input)
# due to arrays being 0 index, when we get to height, we are done
print('height of my forest is',height)

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
	print('row',row, len(row))

	print('currently at ',posX,posY)

	# get the object there
	relX = posX % len(row)
	print('relX', relX)
	charAt = row[relX]
	print('charAt',charAt)
	if charAt == '#':
		treesHit = treesHit + 1
	print('')

# 24 is not the right answer, cuz i forgot to remove sanity check
# 72 isn't right either
# 71 isnt right either :(
print('Done, we hit this many trees:',treesHit)

# Note to self - my bug was not having rstrip() when I considered the length of the line!