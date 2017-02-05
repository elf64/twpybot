from getPeople import getFollowers
import time
import json
import requests

# https://api.twitch.tv/kraken/users/coolkidscode
# 146634280 - coolkidscode _id


def get_id(user, chnl):
    with open('config.json', 'r') as f:
        config = json.load(f)
    channel = chnl
    s = requests.session()
    headers = {
        'Client-ID': config['client-id']
    }
    p = s.get('https://api.twitch.tv/kraken/users/'+channel, headers=headers)
    f.close()
    pk = json.loads(p.text)
    return '@{} the _id of the channel is: {}'.format(pk['_id'])


def get_hosts():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        s = requests.session()
        headers = {
            'Client-ID': config['client-id']
        }
        p = s.get(
            'http://tmi.twitch.tv/hosts?include_logins=1&target=146634280',
            headers=headers)
        f.close()
        pk = json.loads(p.text)
        k = pk['hosts']
        print k[0]['host_display_name']
    except Exception as egg:
        print egg


def new_follower():
    follower = getFollowers()  # last follower
    follower2 = follower
    while True:
        follower = getFollowers()
        print follower
        if follower != follower2:
            # do something cuz there is a new follower
            follower2 = follower
            print '@{} Thanks for the follow :D Hope you enjoy the stream.'\
                .format(follower)
        time.sleep(1)
