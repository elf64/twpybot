from getPeople import getAllUsr, getAllMods
import time
import os

# Script to add minutes for every user and mods in channel #
# Adds +1 minute every minute Kappa #

# Variables :-? #
time_path = 'p_time/'
points_path = 'points/'
extension = '.txt'
# End #


def startpoints():
    while True:
        for i in getAllUsr():
            if os.path.isfile(points_path+i+extension) is not True:
                files = open(points_path+i+extension, 'w+')
                files.write('1')
                files.close()
            f = open(points_path+i+extension, 'r')
            try:
                prev_value = f.read()
            except:
                f = open(points_path+i+extension, 'w')
                f.write('1')
                f.close()
                f = open(points_path+i+extension, 'r')
                prev_value = f.read()
                f.close()
            f = open(points_path+i+extension, 'w')
            final_value = int(prev_value) + 1
            f.write(str(final_value))
            f.close()

        for i in getAllMods():
            if os.path.isfile(points_path+i+extension) is not True:
                files = open(points_path+i+extension, 'w+')
                files.write('1')
                files.close()
            f = open(points_path+i+extension, 'r')
            try:
                prev_value = f.read()
            except:
                f = open(points_path+i+extension, 'w')
                f.write('1')
                f.close()
                f = open(points_path+i+extension, 'r')
                prev_value = f.read()
                f.close()
            f = open(points_path+i+extension, 'w')
            final_value = int(prev_value) + 1
            f.write(str(final_value))
            f.close()
        print 'done for points'
        time.sleep(900)


def start_timer():
    while True:
        for user in getAllUsr():
            userpath = os.path.join(time_path, user, extension)
            if os.path.isfile(userpath) is not True:
                files = open(userpath, 'w+')
                files.write('1')
                files.close()
            f = open(userpath, 'r')
            try:
                prev_value = f.read()
            except:
                f = open(userpath, 'w')
                f.write('1')
                f.close()
                f = open(userpath, 'r')
                prev_value = f.read()
                f.close()
            with open(userpath, 'w') as f:
                final_value = int(prev_value) + 1
                f.write(str(final_value))

        for i in getAllMods():
            if os.path.isfile(userpath) is not True:
                files = open(userpath, 'w+')
                files.write('1')
                files.close()
            f = open(userpath, 'r')
            try:
                prev_value = f.read()
            except:
                f = open(userpath, 'w')
                f.write('1')
                f.close()
                f = open(userpath, 'r')
                prev_value = f.read()
                f.close()
            with open(userpath, 'w') as f:
                final_value = int(prev_value) + 1
                f.write(str(final_value))
        print 'done for time'
        time.sleep(60)
