import re

# So ignore most of the comments below as it's a copy from p1, I'm mostly going to talk changes
# here. In my new logic, a 'good' # is only good is by a star. I will record an array of objects
# where I store the number and the POSITION of the found star.
# Then when done, I can loop over my array and see if I have matches. I will also keep a record of 
# stars "already" used such that when I come to the next number w/ a star, I don't multiply it again

input = """
467..114..
...*......
..35..633.
......#...
617*12...
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
#lines = input.strip().split('\n')

lines = [line.rstrip() for line in open('input.txt','r')]

# So in theory, the logic is:
# Find the numbers per line, and then I need to look "around" to see if I'm touching a symbol. If so, I'm included

total = 0
usedStars = []
gears = []

for (x, line) in enumerate(lines):
	#print(x, line)
	# First, find the numbers
	for m in re.finditer(r'\d+', line):
		# simple boolean to determine if we add this number
		toAdd = False
		match = line[m.start():m.end()]
		#print("\nWorking on",match)
		# Given we know where we are, check above, bottom, and immediate left+right

		# For our 4 conditions, if food, we add immediately, because I don't believe we will ever add 2+ times
		# First, check above me, if I can

		# Current bug - I'm marking the star's X position relative to the string I get 'around' the gear, 
		# but it needs to be where it was in the string in general. So in theory, found pos + where I started?

		if x >= 1:
			#print("checking above")
			#print("my substr start is ",max(0,m.start()-1))
			length = len(match)
			previousStr = lines[x-1][max(0,m.start()-1):min(len(lines[x-1]),m.end()+1)]
			#print("previousStr", previousStr)
			# so, not number and not a dot. In theory, regex could do that, but I'm not sure how.
			star = previousStr.find('*')
			if star >= 0:
				#print("Adding a star match at", star+max(0,m.start()-1),x-1)
				toAdd = True
				gears.append({
					"number": int(match), 
					"star": {
						"x": star + max(0,m.start()-1), 
						"y": x-1
					}
				})
			#else:
			#	print("no chars")

		# Now check below
		if x < len(lines)-1:
			#print("checking below")
			#print("my substr start is ",max(0,m.start()-1))
			length = len(match)
			nextStr = lines[x+1][max(0,m.start()-1):min(len(lines[x+1]),m.end()+1)]
			#print("nextStr", nextStr)
			# so, not number and not a dot. In theory, regex could do that, but I'm not sure how.
			star = nextStr.find('*')
			if star >= 0:
				#print("Adding a star match at", star+max(0,m.start()-1),x+1)
				toAdd = True
				gears.append({
					"number": int(match), 
					"star": {
						"x": star + max(0,m.start()-1), 
						"y": x+1
					}
				})
			#else:
			#	print("no chars")

		# Now check immediate left
		if m.start() > 0:
			#print("check left")
			left = lines[x][m.start()-1:m.start()]
			#print("left is", left)
			if left == '*':
				#print("Adding a star match at", m.start()-1,x)
				toAdd = True
				gears.append({
					"number": int(match), 
					"star": {
						"x": m.start()-1, 
						"y": x
					}
				})
			#else:
			#	print("no chars")

		# Now check immediate right
		if m.end() < len(lines[x]):
			#print("check right")
			right = lines[x][m.end():m.end()+1]
			#print("right is", right)
			if right == '*':
				#print("Adding a star match at", m.end(),x)
				toAdd = True
				gears.append({
					"number": int(match), 
					"star": {
						"x": m.end(), 
						"y": x
					}
				})
			#else:
			#	print("no chars")


def contains(list, filter):
	for x in list:
		#print("contains", x, "filter", filter)
		if filter["x"] == x["x"] and filter["y"] == x["y"]:
			return True
	return False
	
# Ok, so we loop through gears, and for each, check ever OTHER one to see if we have a matching star that's NOT in usedStars
for x,gear in enumerate(gears):
	#print("working on gear", gear)

	for a,b in enumerate(gears):
		if a != x:
			#print("gear.star.x", gear["star"]["x"], "b.star.x", b["star"]["x"])
			if gear["star"]["x"] == b["star"]["x"] and gear["star"]["y"] == b["star"]["y"]:
				if contains(usedStars, b["star"]) == False:
					#print("UNIQUE MATCH")
					usedStars.append(gear["star"])
					total += gear["number"] * b["number"]


# 70771730 is too low
print("\nTOTAL", total)