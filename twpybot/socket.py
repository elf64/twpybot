import socket
from Settings import HOST, PORT, CHANNEL
import json


with open('config.json', 'r') as f:
    config = json.load(f)


def open_socket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send('PASS {}\r\n'.format(config['oauth']))
    s.send('NICK {}\r\n'.format(config['oauth']))
    s.send('JOIN #{}\r\n'.format(config['oauth']))
    return s


def send_message(s, message):
    messagetemp = 'PRIVMSG #{} :{}'.format(CHANNEL, message)
    s.send(messagetemp + '\r\n')
    print('Sent: ' + messagetemp)
