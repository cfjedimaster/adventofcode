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
		bags[color] = {}
		bags[color]["count"] = [0]
		return

	children = []
	count = []
	# we dont need numbers, but I bet we will for p2
	for bag in subbags:
		bits = bag.split(' ')
		#its: X A B bag, so we can disregard bits[0] and the end
		#newBag = ' '
		newBag = ' '.join(bits[1:3])
		num = int(bits[0])
		children.append(newBag)
		count.append(num)

	#print(color, children)
	bags[color] = {}
	bags[color]["children"] = children
	bags[color]["count"] = count

#how many bags are 'under' me
def countBags(color):
	total = 0
	print("this bag", color, bags[color])
	if(bags[color]["count"][0] == 0):
		return 0

	for (x,childColor) in enumerate(bags[color]["children"]):
		newTotal = bags[color]["count"][x]  +  (bags[color]["count"][x] * countBags(childColor))
		print("adding",newTotal,"from color",childColor)
		total = total + newTotal

	return total

file = open(r"input.txt","r")
input = file.read()
file.close()

rules = input.strip().split('\n')
print('There are',len(rules),'rules.')
for rule in rules:
	parseRule(rule)

#ok, now we have bag rules
#print(bags)


print(countBags('shiny gold'))	
