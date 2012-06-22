import random

openFile = "calle.bmp"
outfile = "glitched.bmp"

with open(outfile,"wb") as out:
	for line in open(openFile, "rb"):
		process = line
		rand = random.randint(1,10000)
		if (rand in [2,4,6,8]):
			process *= rand
		out.write(process)
