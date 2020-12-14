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
		for letter in person:
			questions[letter] = 1

	return len(questions.keys())

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