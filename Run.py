import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
import random
from getPeople import getViewersOnChannel, getViews, getFollowers # Un-Finnished
import time
from cleverbot import Cleverbot
import os
from datetime import timedelta
from threading import Thread
from putTime import StartTimer, StartPoints



# Variables :-? #
admin = ["coolkidscode", "pukateiubeste", "tutasmaster"]
s = openSocket()
joinRoom(s)
readbuffer = ""
gypsyBot = "tinybattles"
pukastrftime = time.strftime("%d-%m-%Y")
print "Time Test : ", pukastrftime
logs = open("logs/logs0"+pukastrftime+".txt", 'a')
cb = Cleverbot('my-app')
# End #

# ------------------------------------ #
# Start the thread for timer and points #
try:
	t = Thread(target=StartTimer)
	t2 = Thread(target=StartPoints)
	t.daemon = True # tnx god
	t.start()
	t2.daemon = True # tnx god
	t2.start()
	print "Thread1 started."
	print "Thread2 started."
except Exception as egg:
	print egg

	# Start main loop #
while True:
		readbuffer = readbuffer + s.recv(2048)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()

		for line in temp:
			#print(line)
			if "PING" in line:
				s.send("PONG tmi.twitch.tv\r\n")
				break
			user = getUser(line)
			message = getMessage(line)
			print user + " typed :" + message
			logs.write(user + " typed : " + message + "\r\n")


			if message == "!time\r":
				if (os.path.isfile('p_time/'+user.lower()+'.txt') != True):
					sendMessage(s, "The user " + user.lower() + " doesn't exists in the current database.")
					break
				else:
					f = open('p_time/'+user.lower()+'.txt', 'r')
					k = f.read()
					poop =  str(timedelta(minutes=int(k)))
					pop = poop.split(":")
					sendMessage(s, "You have been watching this stream for " + pop[0] + " hours and "
								+ pop[1] + " minutes.")
					f.close()
					break


			# Test Commands 2 #
			if message == "!joinrandom\r":
				o_c = [line.rstrip() for line in open('say/random_class.txt')]
				o_b = [line.rstrip() for line in open('say/random_builds.txt')]
				r_c = random.choice(o_c)
				r_b = random.choice(o_b)
				r_f = r_c + r_b
				sendMessage(s, "join " + r_f)
				break
			# Test Commands #
			if message == "!commands\r":
				sendMessage(s, "@" + user + " Current commands are: !time, "
							+ "!time <user>, > message, !views, !points, !points <user>")
				break

			# --------------------------------- #
			#
			# Un-Finished #
			#
			# --------------------------------- #
			if message == "!test_f\r":
				sendMessage(s, ".")
				getFollowers()
				break


			# Points command #
			if message == "!points\r":
				if (os.path.isfile('points/'+user.lower()+'.txt') != True):
					sendMessage(s, "You are not in the current database @" + user.lower())
					break
				else:
					f = open('points/'+user.lower()+'.txt', 'r')
					k = f.read()
					#poop =  str(timedelta(minutes=int(k)))
					#pop = poop.split(":")
					sendMessage(s, "You have " + k + " points. @" + user)
					f.close()
					break
			# End #

			if message.startswith("!points "):
				k = message.split(" ")
				final_s = k[1]
				final_s = final_s.replace("\r", "")
				if (os.path.isfile('points/'+final_s.lower()+'.txt') != True):
					sendMessage(s, "The user " + final_s.lower() + " doesn't exists in the current database.")
					break
				else:
					f = open('points/'+user.lower()+'.txt', 'r')
					k = f.read()
					#poop =  str(timedelta(minutes=int(k)))
					#pop = poop.split(":")
					sendMessage(s, "The user " + final_s.lower() + " haves " + k + " points.")
					f.close()
					break




			# Time command #
			if message.startswith("!time "):
				k = message.split(" ")
				final_s = k[1]
				final_s = final_s.replace("\r", "")
				if (os.path.isfile('p_time/'+final_s+'.txt') != True):
					sendMessage(s, "The user " + final_s + " doesn't exists in the current database.")
					break
				else:
					#print final_s
					final_s = final_s.replace("\r", "")
					f = open('p_time/'+final_s+'.txt', 'r')
					lj = f.read()
					#print lj
					#str(timedelta(minutes=100))
					poop =  str(timedelta(minutes=int(lj)))
					pop = poop.split(":")
					print pop
					#print poop
					if pop[0] == '0':
						sendMessage(s, final_s + " have been watching this stream for " + pop[1]
									+ " minutes.")
					else:
						sendMessage(s, final_s + " have been watching this stream for " + pop[0]
								+ " hours and " + pop[1] + " minutes.")
					f.close()
					break

			# End #

			#  #
			if message.startswith(">"):
				k = message.split(">")
				final_s = "".join(k[1:])
				#print final_s
				p = cb.ask(final_s)
				sendMessage(s, p)
				break

			if "http://" in message or "https://" in message or "www." in message:
				sendMessage(s, ".timeout " + user + " 10")
				sendMessage(s, "No links allowed!!! @" + user)
				break
			if message.startswith("!") and "type" in message:
				sendMessage(s, "The type of message is " + str(type(message)))
				break
			if message.startswith("!") and "views" in message:
				sendMessage(s, getViews())
				break
			if message.startswith("!") and "test" in message:
				sendMessage(s, "test")
				break
			if message.startswith("!") and "quit" in message and user in admin:
				sendMessage(s, "Bye <3 Kappa")
				quit("\n\n\n\r\n BYE ~~~~")
			# End #
