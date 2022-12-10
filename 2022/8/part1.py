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

totalVisible = 0
for idx,row in enumerate(forest):
	# we can ignore top and bottom
	if idx != 0 and idx != len(forest)-1:
		for idy,col in enumerate(row):
			# we can ignore beg and end
			if idy != 0 and idy != len(row)-1:
				#
				# So - now need to check my row and col, Ray, return here
				#
				print(idx,idy,"=",col)