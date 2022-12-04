input2 = [
	"vJrwpWtwJgWrhcsFMMfFFhFp",
	"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
	"PmmdzqPrVvPwwTWBwg",
	"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
	"ttgJtRGJQctTZtZT",
	"CrZsJsPPZsGzwwsLwLmpwMDw"
]

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

# given 3 strings, find the char thats in all 3
def findMatchingItem(a,b,c):
	# we must have exactly one, so this is safe, honest
	for char in a:
		if b.find(char) != -1 and c.find(char) != -1:
			return char



# so input[::3] works but when you ask for index, it is the for loop index, not the array
# index, ie for me it was 0 and 1, not the position in the array
# i used a more manual loop
totalPriority = 0
idx = 0
while idx + 3 <= len(input):
	ourGroup =	[
		input[idx], 
		input[idx+1],
		input[idx+2]
	]
	#print(ourGroup)
	matchingItem = findMatchingItem(ourGroup[0], ourGroup[1], ourGroup[2])
	#print('matching item', matchingItem)

	idx = idx + 3

	priority = getPriority(matchingItem)
	#print('pri is ', priority)
	totalPriority = totalPriority + priority

print(totalPriority)
