import re

# So for each letter number, we prefix it with the value, so 'fooone' becomes 'foo1one'.
# We don't need to remove the original number, and in fact we can't cuz we might have
# oneight which is two numbers
# So the issue I ran into by prefixing is that it 'breaks' oneight. So now my first part
# will make an index of matches, and THEN do the inserts
def getCalibrationValue(s):
	numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	inserts = []

	# Failure - doesn't support finding it more than once
	#for x, n in enumerate(numbers):
	#	match = s.find(n)
	#	#print("for ",n," match is", match, "x is",x)
	#	if match != -1:
	#		inserts.append({"pos": match, "value":x+1 })
	for x, n in enumerate(numbers):
		p = re.compile(n)
		for m in p.finditer(s):
			inserts.append({"pos":m.start(), "value":x+1})



	#print("inserts: ", inserts)
	# a reverse doesn't work ray
	#inserts.reverse()
	inserts = sorted(inserts, key=lambda i:i["pos"])
	inserts.reverse()
	#print("inserts: ", inserts)
	# We reverse the list so our inserts pos val doesnt get off
	for i in inserts:
		s = s[:i["pos"]] + str(i["value"]) + s[i["pos"]:]

	#print("s is NOW ",s)

	matches = re.findall(r'\d', s)
	if(len(matches) >= 2):
		return int(matches[0] + matches[len(matches)-1])
	elif(len(matches) == 1):
		return int(matches[0] + matches[0])
	else:
		# this should not fire
		return 0
	
#input = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]
#input = ["jgb95ninetwonine"]
input = [line.rstrip() for line in open('input.txt','r')]

total = 0
for i in input:
	calibration = getCalibrationValue(i)
	print("input", i, "calibration", calibration)
	total += calibration

# 54143 is too high
# 54076 is too low
print("\nTotal", total)
