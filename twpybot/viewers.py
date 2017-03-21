import json
import requests


def current_viewers(channel):
    s = requests.session()
    p = s.get('https://tmi.twitch.tv/group/user/{)/chatters'
              .format(channel).json())
    if 'thegypsyknight' in p['chatters']['moderators']:
        return 0
    return 1
# End #


def get_followers():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        channel = config['channel']
        s = requests.session()
        headers = {
            'Client-ID': config['client-id']
        }
        p = s.get('https://api.twitch.tv/kraken/channels/{}/follows?limit=1'
                  .format(channel), headers=headers)
        f.close()
        pk = json.loads(p.text)
        return pk['follows'][0]['user']['display_name']
    except Exception as egg:
        print egg


def get_views():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        channel = config['channel']
        s = requests.session()

        headers = {
            'Client-ID': config['client-id']
        }
        p = s.get('https://api.twitch.tv/kraken/streams/' + channel,
                  headers=headers).json()
        f.close()
        viewers = p['stream']['viewers']
        return 'There are {} people watching. FeelsBadMan'.format(str(viewers))
    except Exception as egg:
        print egg


def get_users():
    channel = 'coolkidscode'
    s = requests.session()
    p = s.get('https://tmi.twitch.tv/group/user/{}/chatters'
              .format(channel)).json()
    users = p['chatters']['viewers']
    return users


def get_mods():
    channel = 'coolkidscode'
    s = requests.session()
    p = s.get('https://tmi.twitch.tv/group/user/{}/chatters'
              .format(channel)).json()
    mods = p['chatters']['moderators']
    return mods
