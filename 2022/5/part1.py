"""
I'm going to keep input to directions, and hard code the initial stacks. I think.
I KNOW I'm going to typo this.
"""

stacks = []
stacks.append(["M","J","C","B","F","R","L","H"])
stacks.append(["Z","C","D"])
stacks.append(["H","J","F","C","N","G","W"])
stacks.append(["P","J","D","M","T","S","B"])
stacks.append(["N","C","D","R","J"])
stacks.append(["W","L","D","Q","P","J","G","Z"])
stacks.append(["P","Z","T","F","R","H"])
stacks.append(["L","V","M","G"])
stacks.append(["C","B","G","P","F","Q","R","J"])

print(stacks)

sampleInput = [
"move 1 from 2 to 1",
"move 3 from 1 to 3",
"move 2 from 2 to 1",
"move 1 from 1 to 2"
]

input = [line.rstrip() for line in open('input.txt','r')]

def move(stacks, fromX, toX, total):
	curr = 1
	while curr <= total:
		topBox = stacks[fromX-1].pop()
		stacks[toX-1].insert(len(stacks[toX-1]), topBox)
		curr = curr + 1
		

def topBox(stacks):
	result = ""
	for s in stacks:
		result = result + s.pop()

	return result

for instruction in input:
	moveIns = instruction.split(" from ")
	moveTotal = int(moveIns[0].split(" ")[1])
	fromStack,toStack = moveIns[1].split(' to ')

	fromStack = int(fromStack)
	toStack = int(toStack)

	print(f"Move {moveTotal} boxes from {fromStack} to {toStack}")
	move(stacks, fromStack, toStack, moveTotal)
	#print(stacks)

print('----------------------')
#print(stacks)
print(topBox(stacks))