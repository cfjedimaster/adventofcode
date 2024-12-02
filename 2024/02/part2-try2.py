
lines = [line.rstrip() for line in open('input.txt','r')]
reports = []

for line in lines:
	report = line.split(' ')
	report = [ int(x) for x in report ]
	reports.append(report)

print(f"Total reports: {len(reports)}")
totalSafe = 0

def safeReport(report):
	print(f"Testing {report}")
	isSafe = True

	# default to no direction at first
	lastDirection = ""

	for x,item in enumerate(report):
		if x > 0:
			direction = ""
			# are we higher or smaller?
			if report[x] > report[x-1]:
				direction = "up"
			elif report[x] < report[x-1]:
				direction = "down"
			
			if lastDirection != "" and direction != lastDirection:
				#print(f"lastDirection was {lastDirection} and this is {direction}, not safe!")
				# do a test w/o and if ok, we dont set to false
				isSafe = False

			
			diff = abs(report[x] - report[x-1])
			if diff < 1 or diff > 3:
				#print(f"Too much diff, {diff}")
				isSafe = False

			lastDirection = direction
	
	return isSafe	

def generateVariants(list):
	variants = [list]

	for x,v in enumerate(list):
		newList = list.copy()
		del newList[x]
		variants.append(newList)

	return variants

for i,report in enumerate(reports):

	# Given a source array, generate a new list of variants
	variants = generateVariants(report)
	#print(variants)

	isSafe = False
	for v in variants:
		thisSafe = safeReport(v)
		if thisSafe == True:
			isSafe = True
	#isSafe = safeReport(report)
	
	print(f"Final decision for report {i+1}, is it safe? {isSafe}")
	if isSafe:
		totalSafe = totalSafe + 1

print(f"Total Safe: {totalSafe}")

# 249 is too low