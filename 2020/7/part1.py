input = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

#global variable that parseRule uses, I don't like that
bags = {}

def parseRule(r):
	parts = r.split(' contain ')
	color = parts[0].replace(' bags','')

	subbags = parts[1].split(', ')
	#special rule for 'no other bags'
	if(subbags[0] == 'no other bags.'):
		bags[color] = []
		return

	children = []
	# we dont need numbers, but I bet we will for p2
	for bag in subbags:
		bits = bag.split(' ')
		#its: X A B bag, so we can disregard bits[0] and the end
		#newBag = ' '
		newBag = ' '.join(bits[1:3])
		children.append(newBag)

	#print(color, children)
	bags[color] = children

def holdsGold(color):
	#print('checking',color, bags[color])
	for subcolor in bags[color]:
		if(subcolor == 'shiny gold'):
			return True
		else:
			if(holdsGold(subcolor)):
				return True
	return False

file = open(r"input.txt","r")
input = file.read()
file.close()

rules = input.strip().split('\n')
print('There are',len(rules),'rules.')
for rule in rules:
	parseRule(rule)

#ok, now we have bag rules
#print(bags)

totalHoldsGold = 0
for color in bags:
	if(holdsGold(color)):
		#print('it did!')
		totalHoldsGold = totalHoldsGold + 1

print('Total that holds hold is',totalHoldsGold)
	
