file = open(r"input.txt","r")
lines = [line.split('|') for line in file]
file.close()

# Len of each number
lens = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
#not sure if i can do this above
for line in lines:
	line[0] = line[0].strip()
	line[1] = line[1].strip()

count = 0
for line in lines:
	output = line[1]
	parts = output.split(' ')
	for part in parts:
		#print('part', part, ' ', len(part), ' lens[4]', lens[4])
		if len(part) == lens[1] or len(part) == lens[4] or len(part) == lens[7] or len(part) == lens[8]:
			count += 1

print(count)