import string
import random

from socket import send_message


# Initialize .txt file
def join_room(s):
    readbuffer = ''
    loading = True
    while loading:
        readbuffer += s.recv(1024)
        temp = string.split(readbuffer, '\n')
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            loading = loading_complete(line)
    with open('say/random_join.txt') as f:
        send_message(s, random.choice(f.readlines()))


def loading_complete(line):
    if 'End of /NAMES list' in line:
        return False
    return True
