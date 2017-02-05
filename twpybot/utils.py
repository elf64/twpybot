import os
from ConfigParser import SafeConfigParser

POINTS_PATH = 'points'
ADMIN = ('pukateibeste', 'coolkidscode')


def get_points(user):
    usr_points_path = os.path.join(POINTS_PATH, user + '.txt')
    if os.path.isfile(usr_points_path):
        with open(usr_points_path, 'r') as points_file:
            return int(points_file.read())
    return None


def store_points(user, usr_points):
    usr_points_path = os.path.join(POINTS_PATH, user + '.txt')
    if os.path.isfile(usr_points_path):
        with open(usr_points_path, 'w') as points_file:
            points_file.write(str(usr_points))
            return usr_points
    return None


def msg_allowed(user, message):
    """

    """
    if user in ADMIN:
        return True


def get_user(line):
    """

    """
    separate = line.split(':', 2)
    user = separate[1].split('!', 1)[0]
    return user


def get_message(line):
    """

    """
    separate = line.split(':', 2)
    message = separate[2]
    return message


def get_config():
    """
    Paths checked for twpybot:
        ~/.twpybot
    """
    paths = []
    if 'TWPYBOT_CONFIG' in os.environ:
        paths.append(os.environ['TWPYBOT_CONFIG'])
    paths.append('/etc/twpybot.ini')
    paths.append('/etc/twpybot')

    for path in paths:
        if os.path.isfile(path):
            config = SafeConfigParser()
            config.optionxform = lambda x: x
            config.read(path)
            return config
