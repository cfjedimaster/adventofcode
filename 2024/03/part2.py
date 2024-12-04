import re

input = open('input.txt', 'r').read()

total = 0

# Instructions is an array of obs, in order, of pos:X, ins:do() or don't()
instructions = []

instructionRe = re.finditer(r"(don't\(\))|(do\(\))", input)
for i in instructionRe:
	instructions.append({"pos":i.start(), "ins":i.group()})

#print(instructions)

# As before, we get all, this time in an iter, and BEFORE we add shit, we see what the last instruction was

matches = re.finditer(r"mul\(\d{1,3},\d{1,3}\)", input)
for match in matches:
	pos = match.start()
	op = match.group()

	doIt = True 
	for i in instructions:
		if i["pos"] < pos:
			if i["ins"] == "do()":
				doIt = True
			else:
				doIt = False 
	
	#print("ok for this", op, " we do it? ", doIt)
	if doIt:
		op = op.replace("mul(","")
		op = op.replace(")","")
		nums = op.split(",")
		toAdd = int(nums[0]) * int(nums[1])
		total = total + toAdd



print("Total", total)