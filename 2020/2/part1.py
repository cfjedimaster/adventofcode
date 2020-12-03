# 1-3 a: abcde
# rule is how many you need and letter

def validPassword(s):
	parts = s.split(' ')
	minMax = parts[0].split('-')
	min = int(minMax[0])
	max = int(minMax[1])

	requiredLetter = parts[1].replace(":","")
	input = parts[2]
	#print(min,max,requiredLetter,input)

	# OK, so at this point, we know what letter must exist and min max, let's count
	totalLetter = input.count(requiredLetter)
	#print(totalLetter)
	if (totalLetter >= min) and (totalLetter <= max):
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