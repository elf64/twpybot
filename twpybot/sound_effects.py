from utils import get_points, store_points
from playsound import playsound

MIN_POINTS = 5


def play_sfx(effect):
    path = '{}.mp3'.format(effect)
    if path.isfile(path):
        playsound(path, True)
        return True
    return False


def run_sfx(user, effect_name):
    points = get_points()
    if points >= MIN_POINTS:
        # if true, the sfx played and the file existed
        if play_sfx(user, effect_name):
            points -= 5
            store_points(user, points)
            return '@{} played {}'.format(user. effect_name)
        # if false the sfx does not exist
        return False, '@{} that effect doesnt exist'.format(user)
    return '@{} you dont have enough points'.format(user)
