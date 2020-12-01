
file = open(r"input.txt","r")

input = []
for line in file:
	input.append(int(line))

file.close()

# This version needs 3 loops
# this one seemed noticebly slower. I need to figure out how to abort
# think i got it with the IFs, def ran quicker
haveAnswer = False
for i,x in enumerate(input):
	if(haveAnswer == True):
		break
	for j,y in enumerate(input):
		if(haveAnswer == True):
			break
		for k,z in enumerate(input):
			if (i != j) and (i != k) and (x+y+z == 2020) and (haveAnswer == False):
				print(x*y*z)
				haveAnswer = True 
				break




