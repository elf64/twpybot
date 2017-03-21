import os
import pytest

from twpybot.utils import (get_points, store_points, POINTS_PATH,
                           get_message, get_user)


@pytest.fixture()
def user_temp():
    points_file = os.path.join(POINTS_PATH, 'test.txt')
    with open(points_file, 'w') as f:
        f.write('420')
    return 'test'


def test_get_points_no_user():
    points = get_points('foo')
    assert points is None


def test_get_points(user_temp):
    points = get_points(user_temp)
    assert points == 420


def test_store_points():
    points = store_points('test', 666)
    assert points is not None


def test_no_points_stored():
    points = store_points('foo', 666)
    assert points is None


def test_get_message():
    line = ':tmi.twitch.tv 003 twitch_username :foo bar'
    msg = get_message(line)
    assert msg == 'foo bar'


def test_get_user():
    line =\
        ':test!usr@test.tmi.twitch.tv PRIVMSG #channel :message that was sent'
    user = get_user(line)
    assert user == 'test'
