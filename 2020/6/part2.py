input = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""

def yesCount(group):
	questions = {}
	#split by lines
	people = group.split('\n')
	for person in people:
		#print('person',person)
		for letter in person:
			#print('letter',letter, letter in questions)
			if(letter in questions) == False:
				#print('letter isnt in',letter)
				questions[letter] = 0
			questions[letter] = questions[letter] + 1

	total = 0
	for letter in questions:
		if(questions[letter] == len(people)):
			total = total+1

	return total

file = open(r"input.txt","r")
input = file.read()
file.close()

#first, get the groups from the input
groups = input.strip().split('\n\n')
print('There are',len(groups),'groups.')

total = 0
for group in groups:
	total = total + yesCount(group)

print(total)