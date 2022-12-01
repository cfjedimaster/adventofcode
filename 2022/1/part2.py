
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


def totalKey(elem):
	return elem["total"]

# sort elves by total
elves.sort(key=totalKey, reverse=True)

print(elves[0]["total"] + elves[1]["total"] + elves[2]["total"])	
