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
from lastFollow import get_id
import json
import requests
import playsound
import glob

# Imports ^




# Variables :-? #
sfx_play = False
sfx = ""
sfx_list = []
admin = ["pukateiubeste", "coolkidscode"]
s = openSocket()
joinRoom(s)
readbuffer = ""
gypsyBot = "tinybattles"
pukastrftime = time.strftime("%d-%m-%Y")
print "Time Test : ", pukastrftime
logs = open("logs/logs0"+pukastrftime+".txt", 'a')
cb = Cleverbot('my-app')
# End #

# Get all sfx files from directory and change back to the main one #
cwd = os.getcwd()
os.chdir("sfx/")
for file in glob.glob("*.mp3"):
	print(file)
	#file.split("/")
	sfx_list.append(file)
os.chdir(cwd)
print sfx_list
# End #

# Function for a new follower #
def newFollower():
	x = getFollowers() # Returns the last follower of the channel
	x2 = x
	while True:
		x = getFollowers()
		#print x
		if x != x2:
			#do something cuz there is a new follower
			x2 = x
			sendMessage(s, "@" + x + " Thank you very much for the follow :D Hope you enjoy the stream.")
		time.sleep(1)
# End #

# The get host thread is not working correctly #
#
# Not fixed!!! #
#
# I'm so fucking retard
# Now it's working but it updates the host thing every 1 minute :(
#
def getHosts():
	with open('config.json', 'r') as f:
		config = json.load(f)
	channel = config['channel']
	#s = requests.session()
	headers = {
		"Client-ID": config['client-id']
		}
	f.close()
	with requests.Session() as lk:
		p = lk.get("http://tmi.twitch.tv/hosts?include_logins=1&target=146634280", headers=headers)
		pk = json.loads(p.text)
		p2 = pk['hosts']
	#s.config['keep_alive'] = False
	#sendMessage(s, p2[0]['host_display_name'] + " is now hosting the channel. x2")
	while True:
		with requests.Session() as lk:
			p = lk.get("http://tmi.twitch.tv/hosts?include_logins=1&target=146634280", headers=headers)
			pk = json.loads(p.text)
			p3 = pk['hosts']
			if (p3 != []):
				if (p3 != p2):
					host_user = p3[0]['host_display_name']
					#print host_user
					sendMessage(s, host_user + " is now hosting the channel.")
					p2 = p3
			if (p3 == []):
				#print "[] - no host!"
				pass

		#p2 = pk['hosts']
		time.sleep(1)
#
# Wait for sfx command #
def waitSfx():
	while True:
		global sfx_play
		if (sfx_play == True):
			playsound.playsound('sfx/'+ sfx + '.mp3', True)
			sfx_play = False
		else:
			pass
# End #




# ------------------------------------ #
# Start the thread for timer #
try:
	t = Thread(target=StartTimer)
	t2 = Thread(target=StartPoints)
	t3 = Thread(target=newFollower)
	t4 = Thread(target=getHosts)
	t5 = Thread(target=waitSfx)
	t.daemon = True # tnx god
	t.start()
	t2.daemon = True # tnx god
	t2.start()
	t3.daemon = True
	t3.start()
	t4.daemon = True # the thread is working now.. intresting <
	t4.start()
	t5.daemon = True
	t5.start()
	print "Thread1 started."
	print "Thread2 started."
	print "Thread3 started."
	print "Thread4 started."
	print "Thread5 started." # Kappa
except Exception as egg:
	print egg

#	# Start main loop #   #

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

			# Sfx command #
			if message == "!sfx\r":
				sendMessage(s, "Sfx usage: type in chat !sfx <name of sfx> Ex: !sfx fart")
				break


			if message == "!sfx list\r":
				sendMessage(s, 'Sfx list: ' + str(sfx_list))
				break


			if message.startswith("!sfx "):
				k = message.split(" ")
				final_s = k[1]
				final_s = final_s.replace("\r", "")
				# open file and read points #
				f = open('points/'+user.lower()+'.txt', 'r')
				user_points = f.read()
				f.close()
				print user_points
				if (int(user_points) < 5):
					sendMessage(s, "@" + user.lower() + " You don't have enough points to do that")
					break
				if (int(user_points) >= 5):
					if (final_s + ".mp3" in sfx_list):
						f = open('points/'+user.lower()+'.txt', 'w')
						final_points = int(user_points) - 5
						f.write(str(final_points))
						f.close()
						#playsound.playsound('sfx/fart2.mp3', True)
						# Set the sfx value to True #
						sfx = final_s
						sfx_play = True
						break
					else:
						sendMessage(s, "Sfx with name '" + final_s + "' was not found.")
						break
			# get the id of a channel #
			if message.startswith("!id "):
				k = message.split(" ")
				final_s = k[1]
				final_s = final_s.replace("\r", "")
				sendMessage(s, "@" + user.lower() + " The _id of channel is :" + str(get_id(final_s)))
				break
			# Test Commands 2

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
							+ "!time <user>, > message, !views, !points, !points <user>, "
							+ "!github., !transfer <user> <amount>, !sfx <sfx name>")
				break


			# Github Command #
			if message == "!github\r":
				sendMessage(s, "@" + user + " You can find me on github :> "
							+ "https://github.com/pukapy/twpybot")
				break
			# End #


			# --------------------------------- #
			#
			# Un-Finished #
			#
			# --------------------------------- #
			if message == "!lfollow\r":
				sendMessage(s, "Last follower is " + getFollowers())
				#getFollowers()
				break


			# Transfer points to a player #
			if message.startswith("!transfer "):
				k = message.split(" ")
				final_s = k[1]
				final_s = final_s.replace("\r", "")
				if (int(k[2]) < 1):
					sendMessage(s, "@" + user.lower() + " you can't transfer that amount of points.")
					break
				if (os.path.isfile('points/'+final_s.lower()+'.txt') != True):
					sendMessage(s, "The user " + final_s.lower() + " doesn't exists in the current database.")
					break
				if (os.path.isfile('points/' + user.lower() + '.txt') != True):
					xp = open('points/' + user.lower() + '.txt', 'w+')
					xp.write("1")
					xp.close()
				else:
					files_user = open('points/'+user.lower()+'.txt', 'r')
					user_points = files_user.read()
					files_user.close()
					if (int(user_points) < int(k[2])):
						sendMessage(s, "@" + user + " You don't have enough points to transfer.")
						break
					if (int(user_points) >= int(k[2])):
						# Transfer points #
						# First open the current user file and take out the points #
						files_user = open('points/'+user.lower()+'.txt', 'w')
						take_amout = int(user_points) - int(k[2])
						files_user.write(str(take_amout))
						files_user.close()
						# Now open the user transfer file and put the points #
						# Open file for reading the current points #
						files_transfer = open('points/'+final_s.lower()+'.txt', 'r')
						transfer_points = files_transfer.read()
						files_transfer.close()
						# Open file to transfer the points #
						files_transfer = open('points/'+final_s.lower()+'.txt', 'w')
						final_transfer = int(transfer_points) + int(k[2])
						files_transfer.write(str(final_transfer))
						files_transfer.close()

						sendMessage(s, "@" + user.lower() + " added " + k[2] + " points to "
									+ final_s.lower() + " account.")

			# Give points to a player #
			if message.startswith("!give "):
				if user not in admin:
					sendMessage(s, "@" + user.lower() + " you don't have acces to that command.")
					break
				k = message.split(" ")
				final_s = k[1]
				final_s = final_s.replace("\r", "")
				if (os.path.isfile('points/'+final_s.lower()+'.txt') != True):
					sendMessage(s, "The user " + final_s.lower() + " doesn't exists in the current database.")
					break
				else:
					f = open('points/'+final_s.lower()+'.txt', 'r')
					ks = f.read()
					#poop =  str(timedelta(minutes=int(k)))
					#pop = poop.split(":")
					#sendMessage(s, "The user " + final_s.lower() + " haves " + k + " points.")
					f.close()
					f = open('points/'+final_s.lower()+'.txt', 'w')
					added = int(ks) + int(k[2])
					f.write(str(added))
					f.close()
					sendMessage(s, "I just added " + k[2] + " points to " + final_s.lower()
								+ " account.")
					break

			if message == "!give\r":
				if user not in admin:
					sendMessage(s, "@" + user.lower() + " you don't have acces to that command.")
					break
				else:
					sendMessage(s, "Usage is !give <user> <amount>")
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
					f = open('points/'+final_s.lower()+'.txt', 'r')
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
					poop =  str(timedelta(minutes=int(lj))) # This returns 00:00:00 aka h:m:s
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
				if user in admin:
					break
				else:
					sendMessage(s, ".timeout " + user + " 10")
					sendMessage(s, "No links allowed!!! @" + user)
					break
			if message == "!type\r":
				sendMessage(s, "The type of message is " + str(type(message)))
				break
			if message == "!views\r":
				sendMessage(s, getViews())
				break
			if message == "!test\r":
				sendMessage(s, "test")
				break
			if message == "!quit\r":
				if user not in admin:
					sendMessage(s, "@" + user.lower() + " you don't have acces to that command.")
					break
				else:
					sendMessage(s, "Bye <3 Kappa")
					quit("\n\n\n\r\n BYE ~~~~")
			# End #
