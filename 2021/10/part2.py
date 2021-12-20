import math

testinput = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

file = open(r"input.txt","r")
input = file.read()
file.close()

#input = testinput

input = input.strip()

lines = input.split("\n")

def openerOrCloser(s):
	if s in ["(","[","{","<"]:
		return "opener"
	else:
		return "closer"

def validCloser(char, opener):
	if char == "}" and opener != "{":
		return False
	if char == ">" and opener != "<":
		return False
	if char == "]" and opener != "[":
		return False
	if char == ")" and opener != "(":
		return False
	return True

# I return "" for a valid line, or X if a bad car was found
def validLine(s):
	openers = []
	for char in s:
		# im either an opener or closer
		type = openerOrCloser(char)
		if type == "opener":
			openers.append(char)
		else:
			# this is where we validate, my last opener must be my pair
			lastOpener = openers[len(openers)-1]
			#print("im at ",char," and my last opener is ",lastOpener)

			if validCloser(char, lastOpener) == False:
				return char
			else:
				openers.pop()


	return openers

# should return }
#print(validLine("{([(<{}[<>[]}>{[]{[(<()>"))
# should return )
#print(validLine("[[<[([]))<([[{}[[()]]]"))


scores = []
print("how many lines?",len(lines))
for line in lines:
	res = validLine(line)
	if isinstance(res,list):
		thisTotal = 0
		"""
		Ok, so we need to figure out closers, which is the opposite of
		every item in the array, and then we get a score for that, but 
		honestly, we don't have to 'flip' the chars, no real point

		edit: we do need to reverse it to get the math right
		"""
		res.reverse()
		for char in res:
			if char == "{":
				charScore = 3
			if char == "(":
				charScore = 1
			if char == "[":
				charScore = 2
			if char == "<":
				charScore = 4

			thisTotal = thisTotal * 5 + charScore

		print("thisTotal",thisTotal, " for ",line, " res was ", res)
		scores.append(thisTotal)

scores.sort()
size = len(scores)
middle = math.ceil(size/2)
print(scores[middle-1])