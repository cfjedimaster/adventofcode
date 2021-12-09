

file = open(r"input.txt","r")
lines = [line.split('|') for line in file]
file.close()

#lines = [
#	['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab ',' cdfeb fcadb cdfeb cdbaf']
#]

'''
1, 4, 7, 8 are special

Number of times A appears: 8
Number of times B appears: 6
Number of times C appears: 8
Number of times D appears: 7
Number of times E appears: 4
Number of times F appears: 9
Number of times G appears: 7

1 4 7 8 share 2 parts

7 8 share 2 parts 1 and 4 do not have

8 and 4 share 2 parts 7 does not have

Num Parts: 
	2 ==  1
	3 ==  7
	4 ==  4
	5 ==  2, 3, 5
	6 ==  0, 6, 9
	7 == 8

# FIRST THING
1 has 2 parts, 7 has 3, the unique one is A

# SECOND THING
F shows up in 9 sequences, unique
FYI, the seq w/o F must be 2

# THIRD THING
B shows up in 6 sequences, unique

# FOURTH THING
We know the code for F, and F is everyone but 2
So we can figure out 2. 3 and 5 has the same len, but only 5 has B, and we know B now
once we know 5, we know 3 and 3 has c which 5 doesnt, so we loop at the parts of 3, and the
one char in 3 thats not in 5 is C!!!!!!!!!!

# FIFTH THING
So we know the signals for 2 and 3, they are exactly the same except for e and f. We know f, 
so if we compare the seq for 2 and 3, one in each will be unique, and together, one is f, so the other is e
for each char in 2, the one i have that 3 does not is E

Ok, now we know ABCEF and numbers: 12357

# Sixth thing
We know the sequence for 4, bcdf. We've solved BCF, so the unknown is D

# Seventh thing - just figure out the one we missed :)

'''

# Len of each number
#       0  1  2  3  4  5  6  7  8  9
lens = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

# Given a signal input, identify the number
def identifySignal(signal):
	if len(signal) == lens[1]:
		return 1
	if len(signal) == lens[4]:
		return 4
	if len(signal) == lens[7]:
		return 7
	if len(signal) == lens[8]:
		return 8

# given a map of codes in random order and a output that has the same letters, 
# return the value for the keymap
def mapOutputToKey(output, keyMap):
	for key in keyMap:
		keyLen = len(key)
		found = 0

		for char in key:
			if output.find(char) != -1:
				found += 1

		if found == keyLen and len(output) == len(key):
			return keyMap[key]

#not sure if i can do this above
for line in lines:
	line[0] = line[0].strip()
	line[1] = line[1].strip()

total = 0
for line in lines:

	# blank initial wire, a-g
	wires = {
		"a":"",
		"b":"",
		"c":"",
		"d":"",
		"e":"",
		"f":"",
		"g":""
	}

	# blank initial number to wire code, it will be seq = "2", 
	# where the number is a string so we can add them together to get the final num and _then_ int it
	numberMap = {

	}

	signals = line[0]
	output = line[1]

	signalParts = signals.split(' ')
	outputParts = output.split(' ')

	# this part determines A
	oneSignal = ""
	sevenSignal = ""
	for signal in signalParts:
		if identifySignal(signal) == 1:
			oneSignal = signal
			numberMap[signal] = "1"
		elif identifySignal(signal) == 7:
			sevenSignal = signal
			numberMap[signal] = "7"
		elif identifySignal(signal) == 8:
			numberMap[signal] = "8"

	#print(signals)
	#print('oneSignal',oneSignal, 'sevenSignal',sevenSignal)
	# ok so the char in seven not in one is A
	for char in sevenSignal:
		if oneSignal.find(char) == -1:
			wires["a"] = char

	# Rule 2, count the num of times a char shows up, if 9, its F
	# Also does rule 3, if 6 then B
	a = 0
	b = 0
	c = 0
	d = 0
	e = 0
	f = 0
	g = 0

	for signal in signalParts:
		a += signal.count('a')
		b += signal.count('b')
		c += signal.count('c')
		d += signal.count('d')
		e += signal.count('e')
		f += signal.count('f')
		g += signal.count('g')
	

	if a == 9:
		wires["f"] = "a"
	elif b == 9:
		wires["f"] = "b"
	elif c == 9:
		wires["f"] = "c"
	elif d == 9:
		wires["f"] = "d"
	elif e == 9:
		wires["f"] = "e"
	elif f == 9:
		wires["f"] = "f"
	elif g == 9:
		wires["f"] = "g"

	if a == 6:
		wires["b"] = "a"
	elif b == 6:
		wires["b"] = "b"
	elif c == 6:
		wires["b"] = "c"
	elif d == 6:
		wires["b"] = "d"
	elif e == 6:
		wires["b"] = "e"
	elif f == 6:
		wires["b"] = "f"
	elif g == 6:
		wires["b"] = "g"

	# Currently we have 3 wires figured out!
	# fourth thing, find the one missing F
	# then find 3 and 5, the one that has b is 5 and the other is 3
	target = wires["f"]
	numberTwoSignal = ""

	for signal in signalParts:
		if signal.count(target) == 0:
			numberMap[signal] = "2"
			# I feel bad about saving this twice, but it makes it easier below
			numberTwoSignal = signal

	# Part 4 - find 3 and 5 which have a signal len of 5, so does 2
	# so first get all that's 5 and not 2
	numberThreeSignal = ""
	numberFiveSignal = ""
	for signal in signalParts:
		if len(signal) == 5 and signal != numberTwoSignal:
			# "5" has "B"
			target = wires["b"]
			if signal.find(target) == -1:
				numberThreeSignal = signal
				numberMap[signal] = "3"
			else:
				numberFiveSignal = signal
				numberMap[signal] = "5"

	# ok, so what's in 3 and not 5 is "c"
	for char in numberThreeSignal:
		if numberFiveSignal.find(char) == -1:
			wires["c"] = char

	# Part 5
	for char in numberTwoSignal:
		if numberThreeSignal.find(char) == -1:
			wires["e"] = char

	# Part 6
	#We know the sequence for 4, bcdf. We've solved BCF, so the unknown is D
	numberFourSignal = ""
	for signal in signalParts:
		if len(signal) == 4:
			numberFourSignal = signal
			numberMap[signal] = "4"
			bcf = wires["b"] + wires["c"] + wires["f"]
			for char in signal:
				if bcf.find(char) == -1:
					wires["d"] = char

	# Part 7 
	options = "abcdefg"
	for w in wires:
		options = options.replace(wires[w], "")
	wires["g"] = options

	# I forgot to "finish" the numberMap, we are missing 3: 6, 8, and 9 and 0!
	# I fixed 8, so we need 6 and 9. 6 requires abdefg
	# 6 has E and 9 does not
	# also, sort the numberMap

	for key in list(numberMap):
		newKey = ''.join(sorted(key))
		numberMap[newKey] = numberMap.pop(key)

	# 0 is abcefg
	num0 = wires['a']+wires['b']+wires['c']+wires['e']+wires['f']+wires['g']
	num0 = ''.join(sorted(num0))
	# 6 is abdefg
	numSix = wires['a']+wires['b']+wires['d']+wires['e']+wires['f']+wires['g']
	numSix = ''.join(sorted(numSix))

	for signal in signalParts:
		signal = ''.join(sorted(signal))
		if len(signal) == 6:
			if signal not in numberMap:
				if signal == num0:
					numberMap[signal] = "0"
				elif signal == numSix:
					numberMap[signal] = "6"
				else:
					numberMap[signal] = "9"

	#print("----------")
	#print("WIRES:")
	#for w in wires:
	#	print(w, "\t", wires[w])

	#print(numberMap)


	finalResult = ""
	for i in output.split(" "):
		# output may not be in the same order
		num = mapOutputToKey(i, numberMap)
		finalResult += num
	finalResult = int(finalResult)
	#print(finalResult)

	# finalResult is just for this sequence, not final final
	total += finalResult

print(total)