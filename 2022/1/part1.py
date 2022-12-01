
input = [line.rstrip() for line in open('input.txt','r')]

elves = []
elf = {}
elf["total"] = 0

for line in input:
	# if we have a blank line, it's a new elf
	if line == '':
		elves.append(elf)
		elf = {}
		elf["total"] = 0

	else:
		elf["total"] = elf["total"] + int(line)

biggestCal = -1
for elf in elves:
	if elf["total"] > biggestCal:
		biggestCal = elf["total"]

print(biggestCal)

	
