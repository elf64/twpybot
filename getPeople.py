import json
import requests



# Command that will be changed when the bot will be ready to play the game #
def getViewersOnChannel(channel):
    s = requests.session()
    p = s.get("https://tmi.twitch.tv/group/user/" + channel + "/chatters").json()
    if "thegypsyknight" in p['chatters']['moderators']:
        return 0
    else:
        return 1
# End #

def getFollowers():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        channel = config['channel']
        s = requests.session()
        headers = {
            "Client-ID": config['client-id']
        }
        p = s.get("https://api.twitch.tv/kraken/channels/" + channel +"/follows?limit=1", headers=headers)
        f.close()
        pk = json.loads(p.text)
        return pk['follows'][0]['user']['display_name']
        #print p['follows'][0]['display_name']
        #print pk
    except Exception as egg:
        print egg


def getViews(): # Gonna add the channel argument tomorrow!!
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        channel = config['channel']
        s = requests.session()
        #k = open("say/client_id.txt", 'r')
        #fuck = k.readlines()

        headers = {
            "Client-ID" : config['client-id']
        }
        p = s.get("https://api.twitch.tv/kraken/streams/" + channel, headers=headers).json()
        f.close()
        return "There are " + str(p['stream']['viewers']) + " people watching. FeelsBadMan"
    except Exception as egg:
        print egg

def getAllUsr():
    channel = "coolkidscode"
    s = requests.session()
    p = s.get("https://tmi.twitch.tv/group/user/" + channel + "/chatters").json()
    mods = p['chatters']['moderators']
    users = p['chatters']['viewers']
    return users


def getAllMods():
    channel = "coolkidscode"
    s = requests.session()
    p = s.get("https://tmi.twitch.tv/group/user/" + channel + "/chatters").json()
    mods = p['chatters']['moderators']
    #users = p['chatters']['viewers']
    return mods
#print getAllPpl()
