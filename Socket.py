import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL
import json


with open('config.json', 'r') as f:
    config = json.load(f)

def openSocket():

	s = socket.socket()
	s.connect((HOST, PORT))
	s.send("PASS " + config['oauth'] + "\r\n")
	s.send("NICK " + config['name'] + "\r\n")
	s.send("JOIN #" + config['channel'] + "\r\n")
	return s

def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(messageTemp + "\r\n")
	print("Sent: " + messageTemp)
