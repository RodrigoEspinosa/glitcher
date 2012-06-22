import random

openFile = "calle.bmp"
outfile = "glitched.bmp"

with open(outfile,"wb") as out:
	for line in open(openFile, "rb"):
		process = line
		rand = random.randint(1,10000)
		if (rand == 2):
			process *= 2
		elif(rand == 4):
			process *= 4
		elif(rand == 6):	
			process *= 6
		elif(rand == 8):
			process *= 8
		out.write(process)
