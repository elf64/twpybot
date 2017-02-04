import string
import json
import requests
import playsound
import glob
import random
import time

from threading import Thread
from putTime import StartTimer, StartPoints
from lastFollow import get_id
# unfinished
from getPeople import getViews, getFollowers
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from cleverbot import Cleverbot
import sound_effects
import usr_time
import os


# Variables :-? #
sfx_play = False
sfx = ''
sfx_list = []
admin = ['pukateiubeste', 'coolkidscode']
s = openSocket()
msgjoinRoom(s)
readbuffer = ''
gypsyBot = 'tinybattles'
pukastrftime = time.strftime('%d-%m-%Y')
print 'Time Test : ', pukastrftime
logs = open('logs/logs0{}.txt'.format(pukastrftime), 'a')
cb = Cleverbot('my-app')
# End #

# Get all sfx files from directory and change back to the main one #
cwd = os.getcwd()
os.chdir('sfx/')
for file in glob.glob('*.mp3'):
    print(file)
    sfx_list.append(file)
os.chdir(cwd)
print sfx_list
# End #


# Function for a new follower #
def newFollower():
    last_follower = getFollowers()  # Returns the last follower of the channel
    next_follower = last_follower
    while True:
        last_follower = getFollowers()
        if last_follower != next_follower:
            # do something cuz there is a new follower
            next_follower = last_follower
            sendMessage(s, '@{} Thank you very much for the follow' +
                        ' :D Hope you enjoy the stream.'.format(last_follower))
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
    twitch_api = 'http://tmi.twitch.tv/hosts?include_logins=1&target=146634280'
    with open('config.json', 'r') as f:
        config = json.load(f)
    # s = requests.session()
    headers = {
        'Client-ID': config['client-id']
        }
    f.close()
    with requests.Session() as session:
        p = session.get(twitch_api, headers=headers)
        pk = json.loads(p.text)
        p2 = pk['hosts']
    # s.config['keep_alive'] = False
    while True:
        with requests.Session() as session:
            p = session.get(twitch_api, headers=headers)
            pk = json.loads(p.text)
            p3 = pk['hosts']
            if p3 != []:
                if p3 != p2:
                    host_user = p3[0]['host_display_name']
                    sendMessage(s, host_user + ' is now hosting the channel.')
                    p2 = p3
            if p3 == []:
                logs.write('no hosts found \r\n')

        time.sleep(1)


#
# Wait for sfx command #
def waitSfx():
    while True:
        global sfx_play
        if sfx_play is True:
            playsound.playsound('sfx/{}.mp3'.format(sfx, True))
            sfx_play = False
# End #

# ------------------------------------ #
# Start the thread for timer #
try:
    t = Thread(target=StartTimer)
    t2 = Thread(target=StartPoints)
    t3 = Thread(target=newFollower)
    t4 = Thread(target=getHosts)
    t5 = Thread(target=waitSfx)
    t.daemon = True  # tnx god
    t.start()
    t2.daemon = True  # tnx god
    t2.start()
    t3.daemon = True
    t3.start()
    t4.daemon = True  # the thread is working now.. intresting <
    t4.start()
    t5.daemon = True
    t5.start()
    print 'Thread1 started.'
    print 'Thread2 started.'
    print 'Thread3 started.'
    print 'Thread4 started.'
    print 'Thread5 started.'  # Kappa
except Exception as egg:
    print egg

#    # Start main loop #   #

while True:
        readbuffer += s.recv(2048)
        temp = string.split(readbuffer, '\n')
        readbuffer = temp.pop()

        for line in temp:
            if 'PING' in line:
                s.send('PONG tmi.twitch.tv\r\n')
                break
            user = getUser(line).lower()
            message = getMessage(line)
            log_message = '{} typed :{}'.format(user, message)
            print log_message
            logs.write(log_message + '\r\n')

            if message == '!time\r':
                msg = usr_time.usr_time(user)
                sendMessage(s, msg)
                break

            # Sfx command #
            if message == '!sfx\r':
                sendMessage(s, 'Sfx usage: type in chat' +
                            ' !sfx <name of sfx> Ex: !sfx fart')
                break

            if message == '!sfx list\r':
                sendMessage(s, 'Sfx list: ' + str(sfx_list))
                break

            if message.startswith('!sfx '):
                k = message.split(' ')
                sfxname = k[1]
                sfxname = sfxname.replace('\r', '')
                msg = sound_effects.run_sfx(user, sfxname)
                sendMessage(s, msg)
                break
            # get the id of a channel #
            if message.startswith('!id '):
                k = message.split(' ')
                channel = k[1].replace('\r', '')
                msg = get_id(user, channel)
                sendMessage(s, msg)
                break

            if message == '!joinrandom\r':
                o_c = [line.rstrip() for line in open('say/random_class.txt')]
                o_b = [line.rstrip() for line in open('say/random_builds.txt')]
                r_c = random.choice(o_c)
                r_b = random.choice(o_b)
                r_f = r_c + r_b
                sendMessage(s, 'join ' + r_f)
                break
            # Test Commands #
            if message == '!commands\r':
                commands = ('!time', '!time <user>', '> message', '!views',
                            '!points', '!points <user>', '!github',
                            '!transfer <user> <amount>', '!sfx <sfx_name>')
                sendMessage(s, '@{} Current commands are: {}'
                            .format(user, commands))
                break

            # Github Command #
            if message == '!github\r':
                sendMessage(s, '@{} You can find me on github :> ' +
                            'https://github.com/pukapy/twpybot'.format(user))
                break
            # End #

            # parse !follow command
            if message == '!lfollow\r':
                sendMessage(s, 'Last follower is ' + getFollowers())
                break
            # Transfer points to a player #
            if message.startswith('!transfer '):
                k = message.split(' ')
                # get name of person to transfer points to
                to_user = k[1]
                to_user = to_user.replace('\r', '').lower()
                points = k[2]
                msg = point_transfer(user, to_user, amount)
                sendMessage(s, msg)
                break

            # Give points to a player #
            if message.startswith('!give '):
                if user not in admin:
                    sendMessage(s, '@{} you dont have acces to that command.'
                                .format(user))
                    break
                k = message.split(' ')
                final_s = k[1]
                amount = int(k[2])
                recipient = final_s.replace('\r', '')
                msg = admin.give_points(recipient, amount)
                sendMessage(s, msg)
                break

            if message == '!give\r':
                if user not in admin:
                    sendMessage(s, '@{} you dont have acces to that command.'
                                .format(user))
                    break
                sendMessage(s, 'Usage is !give <user> <amount>')
                break

            # Points command #
            if message == '!points\r':
                points = get_points(user)
                sendMessage(s, 'You have {} points. @{}'.format(points, user))
                break
            # End #

            if message.startswith('!points '):
                points = get_points(user)
                sendMessage(s, 'You have {} points. @{}'.format(points, user))
                break

            # Time command #
            if message.startswith('!time '):
                k = message.split(' ')
                final_s = k[1]
                usr = final_s.replace('\r', '')
                msg = usr_time(usr)
                sendMessage(s, msg)
                break
            is_http_https = 'http://' in message or 'https://' in message
            is_http_msg = is_http_https or 'www.' in message
            if is_http_msg:
                if user not in admin:
                    sendMessage(s, '.timeout {} 10'.format(user))
                    sendMessage(s, 'No links allowed!!! @' + user)
                    break
                break

            # parse messages
            if message == '!type\r':
                sendMessage(s, 'The type of message is ' + str(type(message)))
                break
            if message == '!views\r':
                sendMessage(s, getViews())
                break
            if message == '!test\r':
                sendMessage(s, 'test')
                break
            if message == '!quit\r':
                if user not in admin:
                    sendMessage(s, '@{} you dont have acces to that command.'
                                .format(user))
                    break
                sendMessage(s, 'Bye <3 Kappa')
                quit('\n\n\n\r\n BYE ~~~~')
            # End #
