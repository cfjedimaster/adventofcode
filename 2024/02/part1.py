
lines = [line.rstrip() for line in open('input.txt','r')]
reports = []

for line in lines:
	report = line.split(' ')
	report = [ int(x) for x in report ]
	reports.append(report)

print(f"Total reports: {len(reports)}")
totalSafe = 0

for i,report in enumerate(reports):
	isSafe = True
	# default to no direction at first
	lastDirection = ""
	for x,item in enumerate(report):
		if x > 0:
			# are we higher or smaller?
			if report[x] > report[x-1]:
				direction = "up"
			elif report[x] < report[x-1]:
				direction = "down"
			
			if lastDirection != "" and direction != lastDirection:
				#print(f"lastDirection was {lastDirection} and this is {direction}, not safe!")
				isSafe = False
			
			diff = abs(report[x] - report[x-1])
			if diff < 1 or diff > 3:
				#print(f"Too much diff, {diff}")
				isSafe = False

			lastDirection = direction

	
	print(f"Final decision for report {i+1}, is it safe? {isSafe}")
	if isSafe:
		totalSafe = totalSafe + 1

print(f"Total Safe: {totalSafe}")