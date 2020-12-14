
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

usedRules = {}
accumulator = 0
currentLine = 0
running = True
sanity = 0

while(running):

	print(currentLine, 'cmd', rules[currentLine])

	if(currentLine in usedRules):
		print('INIFINITE LOOP')
		running = False
		continue

	thisLine = rules[currentLine]
	usedRules[currentLine] = 1
	
	parts = thisLine.split(' ')
	op = parts[0]
	arg = parts[1]

	if(op == 'nop'):
		currentLine = currentLine + 1
		continue

	if(op == 'acc'):
		arg = int(arg)
		accumulator = accumulator + arg
		currentLine = currentLine + 1
		continue 

	if(op == 'jmp'):
		currentLine = currentLine + int(arg)
		continue

	print('op', op, 'arg', arg)

	if(currentLine == len(rules)):
		running = False

	sanity = sanity + 1
	if(sanity > 100):
		running = False

print('Done, accumulator:',accumulator)
