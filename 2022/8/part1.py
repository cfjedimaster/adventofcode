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

print(forest)

totalVisible = 0
for idx,row in enumerate(forest):
	# we can ignore top and bottom
	if idx != 0 and idx != len(forest)-1:
		for idy,col in enumerate(row):
			# we can ignore beg and end
			if idy != 0 and idy != len(row)-1:
				print(f"checking tree {idx},{idy} {forest[idx][idy]} and row: {row} and col: {col}")
				#
				# So - now need to check my row and col, Ray, return here
				#
				isVisible = True
				# first, up and down
				for x in range(0, idx):
					print(f"DEBUG - idx, idy, x {idx},{idy},{x}")
					print(f"UP: checking tree at {x},{idy} - val is {forest[x][idy]}")
					if forest[x][idx] >= forest[idx][idy]:
						isVisible = False

				for x in range(idx+1, len(forest[idx])):
					print(f"DOWN: checking tree at {x},{idy} val is {forest[x][idy]}")
					if forest[x][idx] >= forest[idx][idy]:
						isVisible = False

				# now we check row, left and right
				#print(f"row is {row}")
				for x,v in enumerate(row):
					if x != idx:
						print(f" checking x {x} pos val is {v} my real x is {idx}")
						print(f" val is {forest[idx][x]}")
						if forest[idx][x] >= forest[idx][idy]:
							isVisible = False

				print(idx,idy,"=",col, " and is it visible?", isVisible)
				if isVisible == True:
					totalVisible = totalVisible + 1

print("------------")
print(f"Total ",totalVisible)