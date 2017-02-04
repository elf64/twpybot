from utils import get_points, store_points


def point_transfer(from_usr, to_usr, amount):
    if amount < 1:
        return '@{} transfer value must be more zero'.format(from_usr)

    usr_points = get_points(from_usr)
    recipient_points = get_points(to_usr)

    if usr_points < amount:
        return '@{} You only have {} points!'.format(from_usr, usr_points)
    usr_points -= int(amount)
    recipient_points += int(amount)

    store_points(from_usr, usr_points)
    store_points(to_usr, recipient_points)

    return '@{} sent @{} {} points, what a pal'.format(
            from_usr, to_usr, amount)
