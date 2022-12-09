input = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
input = input.strip().split('\n')

structure = []
cd = ''

def isCmd(s):
	return s[0] == "$"

# returns an object with the cmd and possible arg
# currently we only support cd and ls
def getCmd(s):
	raw = s[2:]
	#print(f'raw={raw}')
	if raw.find('ls') == 0:
		return {
			'cmd':'ls'
		}
	
	else: 
		result = {
			'cmd':'cd'
		}
		
		arg = raw[3:]
		result['arg'] = arg

		return result

def parseEntry(s):
	size, name = s.split(" ")
	if size != "dir":
		return {
			"size":int(size), 
			"name":name
		}
	else:
		return {
			"dir":name
		}


def getSize(entry):
	size = 0
	for e in entry["entries"]:
		if "size" in e.keys():
			size = size + e["size"]
		if "dir" in e.keys():
			# ray, return here, need to find entry
			size = size + 
	
	return size


isListing = False
for output in input:
	#print('LINE',output)

	if isCmd(output):
		isListing = False
		cmd = getCmd(output)
		#print('CMD',cmd)
		if cmd["cmd"] == "cd":
			
			# change to dir
			# not going up
			if cmd["arg"] != "..":
				if cd != '':
					if cd != '/':
						newdir = cd + "/" + cmd["arg"]
					else: 
						newdir = cd + cmd["arg"]
				else:
					newdir = cmd["arg"]
			else: 
				#print("GOIND BACK FROM",cd)
				newdirArr = cd.split("/")
				newdirArr.pop()
				#print("NEWEDIRARR",newdirArr)
				newdir = "/".join(newdirArr)
				if newdir == "":
					newdir = "/"
				#print("went back",newdir)

			#print("changing to", newdir)

			cd = newdir

			exists = False
			for drive in structure:
				if drive["label"] == newdir:
					exists = True
			
			if exists == False:
				#print("New directory")
				structure.append({"label":newdir, "entries":[]})

		elif cmd["cmd"] == "ls":
			#print("LIST CMD")
			isListing = True

	else:
		# we must be listing
		entry = parseEntry(output)
		for aEntry in structure:
			if aEntry["label"] == cd:
				#print('add', aEntry)
				#structure[entry]["entries"].append(entry)
				aEntry["entries"].append(entry)



print('-------------')
for s in structure:
	print(s)
	size = getSize(s)
	print(size)