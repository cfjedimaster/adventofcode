
#input = [1721,979,366,299,675,1456]
file = open(r"input.txt","r")

input = []
for line in file:
	input.append(int(line))

file.close()

#Loop over the list and find the two numbers that when summed == 2020
#Afaik, there are only 2
# this loop will find the right answer twice
# break only seemed to break the inner loop, so used a bool, the code is still looping though
# which isn't performant. meh.

haveAnswer = False
for i,x in enumerate(input):
	for j,y in enumerate(input):
		if (i != j) and (x+y == 2020) and (haveAnswer == False):
			print(x*y)
			haveAnswer = True 
			break




