# 1-3 a: abcde


def validPassword(s):
	parts = s.split(' ')
	minMax = parts[0].split('-')
	min = int(minMax[0])
	max = int(minMax[1])

	requiredLetter = parts[1].replace(":","")
	input = parts[2]
	#print(min,max,requiredLetter,input)

	letterAtMin = input[min-1]
	letterAtMax = input[max-1]

	#print('letterAtMin',letterAtMin,'letterAtMax',letterAtMax)

	# both cant be true
	if(letterAtMax == requiredLetter) and (letterAtMin == requiredLetter):
		return False

	if(letterAtMax == requiredLetter) or (letterAtMin == requiredLetter):
		return True
	
	return False
	


#print(validPassword('1-3 a: abcde'))
#print(validPassword('1-3 b: cdefg'))
#print(validPassword('2-9 c: ccccccccc'))

file = open(r"input.txt","r")

input = []
for line in file:
	input.append(line)

file.close()

valid = 0

for password in input:
	if(validPassword(password)):
		valid = valid + 1

print('Done and we have',valid,'passwords.')