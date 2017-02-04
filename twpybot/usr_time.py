from os import path

VIEWTIME_PATH = 'p_time'


def usr_time(user):
    time_path = path.join(VIEWTIME_PATH, user, '.txt')
    if path.isfile(time_path) is False:
        return '@{} no time data yet'.format(user)
    with open(time_path) as time_file:
        minutes = int(time_file.read())
    hours = minutes / 60
    return '@{} youve watched for {} hours and {} minutes'\
           .format(hours, minutes)
