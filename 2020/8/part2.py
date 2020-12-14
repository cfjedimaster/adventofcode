
input = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

file = open(r"input.txt","r")
input = file.read()
file.close()

rules = input.strip().split('\n')
print('There are',len(rules),'rules.')

# New rule is, find all JMP/NOP. Create a list. The list is all the indexes of JMP/NOP.
# The initial program is definitely an infinite loop, so we loop over the JMP LIST (lets call it that), 
# where each val is the position of a jmp or nop. We execute our program, and in THAT execution, when 
# we get to the "target" line, we flip the instruction.

def runProgram(rules, targetFlip):
	#print("running program and flipping",targetFlip)
	usedRules = {}
	accumulator = 0
	currentLine = 0
	running = True
	sanity = 0

	while(running):

		#print(currentLine, 'cmd', rules[currentLine])

		if(currentLine in usedRules):
			#print('INIFINITE LOOP')
			running = False
			return "IL"
			continue
		#print("try to get rule #", currentLine, "running", running)
		thisLine = rules[currentLine]
		#print(thisLine)
		usedRules[currentLine] = 1
		
		parts = thisLine.split(' ')
		op = parts[0]
		arg = parts[1]

		if(currentLine == targetFlip):
			#print("FLIP this:",op)
			if op == 'nop':
				op = 'jmp'
			else:
				op = 'nop'
			#print("op is now",op)

		if(op == 'nop'):
			currentLine = currentLine + 1
			if currentLine >= len(rules):
				running = False
			continue

		if(op == 'acc'):
			arg = int(arg)
			accumulator = accumulator + arg
			currentLine = currentLine + 1
			if currentLine >= len(rules):
				running = False
			continue 

		if(op == 'jmp'):
			currentLine = currentLine + int(arg)
			if currentLine >= len(rules):
				running = False
			continue

		print('op', op, 'arg', arg)

		if currentLine >= len(rules):
			running = False

		sanity = sanity + 1
		if(sanity > 100):
			running = False

	#print('Done, accumulator:',accumulator)
	return accumulator

jmpList = []
print("Ok, make my jmp list")

for (x,rule) in enumerate(rules):
	parts = rule.split(' ')
	if(parts[0] == 'nop') or (parts[0] == 'jmp'):
		jmpList.append(x)

print("Our jmp list has ",len(jmpList)," items to check. Here goes nothing.")
#print(jmpList)
for target in jmpList:
	result = runProgram(rules, target)
	if result != 'IL':
		print("result",result)