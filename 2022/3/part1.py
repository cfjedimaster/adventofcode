#input = [
#	"vJrwpWtwJgWrhcsFMMfFFhFp",
#	"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
#	"PmmdzqPrVvPwwTWBwg",
#	"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#	"ttgJtRGJQctTZtZT",
#	"CrZsJsPPZsGzwwsLwLmpwMDw"
#]

input = [line.rstrip() for line in open('input.txt','r')]

# Given an input string, I split it in half
def splitIntoComparments(i):
	csize = int(len(i) / 2)
	return [i[0:csize], i[csize:]]


# Given two strings, find the only matching item in each
def findMatching(one, two):
	# according to puzzle rules, we MUST find at least one
	for char in one:
		if two.find(char) != -1:
			return char

# return priority based on input. in ascii, A=65, Z=90, a=97, z=122
# but for us, a=1, z=26, A=27, Z=52
def getPriority(char):
	ascii = ord(char)
	#print('for ',char,'ascii is',ascii)
	if ascii >= 97 and ascii <= 122:
		return ascii - 96
	if ascii >= 65 and ascii <= 90:
		return ascii - 38
	#print(ascii)

totalPriority = 0
for i in input:
	compartments = splitIntoComparments(i)
	matchingItem = findMatching(compartments[0], compartments[1])
	#print('matchingitem',matchingItem)
	priority = getPriority(matchingItem)
	#print('pri is ', priority)
	totalPriority = totalPriority + priority

print(totalPriority)
