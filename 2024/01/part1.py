#list1 = [3, 4, 2, 1, 3, 3]
#list2 = [4, 3, 5, 3, 9, 3]

list1 = []
list2 = []

lines = [line.rstrip() for line in open('input.txt','r')]
for line in lines:
	parts = line.split()
	list1.append(int(parts[0]))
	list2.append(int(parts[1]))

list1.sort()
list2.sort()

totalDiff = 0

for (i,x) in enumerate(list1):
	diff = abs(x - list2[i])
	totalDiff = totalDiff + diff

print("Total Diff", totalDiff)
	