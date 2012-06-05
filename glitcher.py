import random

openFile = "calle.bmp"
outfile = "glitched.bmp"
out = open(outfile, "wb")

for line in open(openFile, "rb"):
	process = line
	rand = random.randint(1,10000)
	if (rand == 2):
		process = process*2
	elif(rand == 4):
		process = process*4
	elif(rand == 6):	
		process = process*6
	elif(rand == 8):
		process = process*8
	else: 
		process = process
	out.write(process)
out.close()
