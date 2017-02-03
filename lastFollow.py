from getPeople import getFollowers
import time
import json
import requests

# https://api.twitch.tv/kraken/users/coolkidscode
# 146634280 - coolkidscode _id


def get_id(chnl):
    with open('config.json', 'r') as f:
        config = json.load(f)
    channel = chnl
    s = requests.session()
    headers = {
        "Client-ID": config['client-id']
    }
    p = s.get("https://api.twitch.tv/kraken/users/"+channel, headers=headers)
    f.close()
    pk = json.loads(p.text)
    return pk['_id']


def getHosts():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        channel = config['channel']
        s = requests.session()
        headers = {
            "Client-ID": config['client-id']
        }
        p = s.get("http://tmi.twitch.tv/hosts?include_logins=1&target=146634280", headers=headers)
        f.close()
        pk = json.loads(p.text)
        k = pk['hosts']
        print k[0]['host_display_name']
    except Exception as egg:
        print egg

def newFollower():
	x = getFollowers() # Returns the last follower of the channel
	x2 = x
	while True:
		x = getFollowers()
		print x
		if x != x2:
			#do something cuz there is a new follower
			x2 = x
			print "@" + x + " Thank you very much for the follow :D Hope you enjoy the stream."
		time.sleep(1)
#getHosts()
#get_id()
