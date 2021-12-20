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


	return ""

# should return }
#print(validLine("{([(<{}[<>[]}>{[]{[(<()>"))
# should return )
#print(validLine("[[<[([]))<([[{}[[()]]]"))

total = 0

for line in lines:
	res = validLine(line)
	if res != "":
		#print(line, " ==== ",res)
		if res == ")":
			total += 3
		if res == "]":
			total += 57
		if res == "}":
			total += 1197
		if res == ">":
			total += 25137

print(total)