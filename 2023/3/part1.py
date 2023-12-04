import re

input2 = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
# lines = input.strip().split('\n')

lines = [line.rstrip() for line in open('input.txt','r')]

# So in theory, the logic is:
# Find the numbers per line, and then I need to look "around" to see if I'm touching a symbol. If so, I'm included

total = 0

for (x, line) in enumerate(lines):
	#print(x, line)
	# First, find the numbers
	for m in re.finditer(r'\d+', line):
		# simple boolean to determine if we add this number
		toAdd = False
		match = line[m.start():m.end()]
		#print("Working on",match)
		# Given we know where we are, check above, bottom, and immediate left+right

		# First, check above me, if I can
		if x >= 1:
			#print("checking above")
			length = len(match)
			previousStr = lines[x-1][max(0,m.start()-1):min(len(lines[x-1]),m.end()+1)]
			#print("previousStr", previousStr)
			# so, not number and not a dot. In theory, regex could do that, but I'm not sure how.
			# So for now, my logic is - remove all periods. Then regex for \D, and if a match, we are good
			previousStr = previousStr.replace('.', '')
			nonNum = re.match(r'\D', previousStr)
			if(nonNum):
				#print("yes, i had chars!")
				toAdd = True
			#else:
				#print("no chars")

		# Now check below
		if x < len(lines)-1:
			#print("checking below")
			length = len(match)
			nextStr = lines[x+1][max(0,m.start()-1):min(len(lines[x+1]),m.end()+1)]
			#print("nextStr", nextStr)
			# so, not number and not a dot. In theory, regex could do that, but I'm not sure how.
			# So for now, my logic is - remove all periods. Then regex for \D, and if a match, we are good
			nextStr = nextStr.replace('.', '')
			nonNum = re.match(r'\D', nextStr)
			if(nonNum):
				#print("yes, i had chars!")
				toAdd = True
			#else:
			#	print("no chars")

		# Now check immediate left
		if m.start() > 0:
			#print("check left")
			left = lines[x][m.start()-1:m.start()]
			#print("left is", left)
			left = left.replace('.', '')
			nonNum = re.match(r'\D', left)
			if(nonNum):
				#print("yes, i had chars!")
				toAdd = True
			#else:
			#	print("no chars")

		# Now check immediate right
		if m.end() < len(lines[x]):
			#print("check right")
			right = lines[x][m.end():m.end()+1]
			#print("right is", right)
			right = right.replace('.', '')
			nonNum = re.match(r'\D', right)
			if(nonNum):
				#print("yes, i had chars!")
				toAdd = True
			#else:
			#	print("no chars")

		if toAdd:
			total += int(match)

print("\nTOTAL", total)