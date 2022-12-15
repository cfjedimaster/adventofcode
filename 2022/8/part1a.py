import sys

input = """
30373
25512
65332
33549
35390
"""

input = input.strip().split('\n')

forest = []
for i in input:
	toAdd = []
	for c in i:
		toAdd.append(c)
	forest.append(toAdd)

#print(forest)

"""
Given an array, and pos, I'm visible if everything BELOW my pos is <, or everything
ABOVE my pos is <
"""
def checkVisible(pos, arr):
	print("ENTER FUNC", arr, pos)
	mySize = arr[pos]
	print(f"mySize is {mySize}")
	goodLeft = True
	goodRight = True

	for x in range(0, pos):
		print(f'LEFT: checking at {x}')
		if arr[x] >= mySize:
			print('failed to left')
			goodLeft = False

	for x in range(pos+1, len(arr)):
		print(f'RIGHT: checking at {x}')
		if arr[x] >= mySize:
			print('failed to right')
			goodRight = False



	return goodLeft or goodRight


totalVisible = 0
for idx,row in enumerate(forest):
	# we can ignore top and bottom
	if idx != 0 and idx != len(forest)-1:
		for idy,col in enumerate(row):
			# we can ignore beg and end
			if idy != 0 and idy != len(row)-1:
				me = forest[idx][idy]
				print(f"I'm tree {me} at {idx}/{idy}")
				# get my row and col
				#print(f"my row is {row}")
				col = []
				for x,v in enumerate(forest):
					col.append(forest[x][idy])

				#print(f"my col is {col}")

				isVisible = False
				# so, am i the biggest in my row? 
				if checkVisible(idy, row) == True:
					#print("I was biggest in my row in a dir")
					isVisible = True

				if checkVisible(idx, col) == True:
					#print("I was biggest in my col in a dir")
					isVisible = True

				#print("\n")
				print("visible? ", isVisible)
				print("\n")
				if isVisible:
					totalVisible = totalVisible + 1
		#sys.exit()


print("------------")
print(f"Total ",totalVisible)

ext = 2 * len(forest) + 2 * len(forest[0]) - 4
print(ext)

realTotal = ext + totalVisible
print("FINAL", realTotal)
