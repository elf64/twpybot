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


def StartPoints():
    while True:
        for i in getAllUsr():
            if (os.path.isfile(points_path+i+extension) != True):
                files = open(points_path+i+extension, "w+")
                files.write("1")
                files.close()
            f = open(points_path+i+extension, 'r')
            try:
                prev_value = f.read()
                #print prev_value
            except:
                f = open(points_path+i+extension, 'w')
                f.write("1")
                f.close()
                f = open(points_path+i+extension, 'r')
                prev_value = f.read()
                f.close()
            #print prev_value
            f = open(points_path+i+extension, 'w')
            final_value = int(prev_value) + 1
            #print final_value
            f.write(str(final_value))
            f.close()

        for i in getAllMods():
            if (os.path.isfile(points_path+i+extension) != True):
                files = open(points_path+i+extension, "w+")
                files.write("1")
                files.close()
            f = open(points_path+i+extension, 'r')
            try:
                prev_value = f.read()
                #print prev_value
            except:
                f = open(points_path+i+extension, 'w')
                f.write("1")
                f.close()
                f = open(points_path+i+extension, 'r')
                prev_value = f.read()
                f.close()
            #print prev_value
            f = open(points_path+i+extension, 'w')
            final_value = int(prev_value) + 1
            #print final_value
            f.write(str(final_value))
            f.close()
        print "done for points"
        time.sleep(900)


def StartTimer():
    while True:
        for i in getAllUsr():
            if (os.path.isfile(time_path+i+extension) != True):
                files = open(time_path+i+extension, "w+")
                files.write("1")
                files.close()
            f = open(time_path+i+extension, 'r')
            try:
                prev_value = f.read()
                #print prev_value
            except:
                f = open(time_path+i+extension, 'w')
                f.write("1")
                f.close()
                f = open(time_path+i+extension, 'r')
                prev_value = f.read()
                f.close()
            #print prev_value
            f = open(time_path+i+extension, 'w')
            final_value = int(prev_value) + 1
            #print final_value
            f.write(str(final_value))
            f.close()


        for i in getAllMods():
            if (os.path.isfile(time_path+i+extension) != True):
                files = open(time_path+i+extension, "w+")
                files.write("1")
                files.close()
            f = open(time_path+i+extension, 'r')
            try:
                prev_value = f.read()
                #print prev_value
            except:
                f = open(time_path+i+extension, 'w')
                f.write("1")
                f.close()
                f = open(time_path+i+extension, 'r')
                prev_value = f.read()
                f.close()
            #print prev_value
            f = open(time_path+i+extension, 'w')
            final_value = int(prev_value) + 1
            #print final_value
            f.write(str(final_value))
            f.close()
        print "done for time"
        time.sleep(60)
