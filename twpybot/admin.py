from utils import get_points, store_points, ADMIN


def give_points(from_usr, to_usr, amount):
    if from_usr not in ADMIN:
        return '@{} you are not permitted to do that'.format(from_usr)
    points = get_points(to_usr)
    points += int(amount)
    store_points(to_usr, points)
    return '@{} just received {} points from admin {}!!!'\
           .format(to_usr, from_usr, amount)
