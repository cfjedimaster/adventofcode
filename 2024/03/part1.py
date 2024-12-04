import re

input = open('input.txt', 'r').read()

total = 0

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)
for match in matches:
	# weak sauce, but works
	match = match.replace("mul(","")
	match = match.replace(")","")
	nums = match.split(",")
	toAdd = int(nums[0]) * int(nums[1])
	total = total + toAdd

print("Total", total)