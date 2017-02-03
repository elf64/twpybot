import string
from Socket import sendMessage
import random

# Initialize .txt file
def joinRoom(s):
	readbuffer = ""
	Loading = True
	while Loading:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()

		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	with open("say/random_join.txt") as f:
		sendMessage(s, random.choice(f.readlines()))

def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True
