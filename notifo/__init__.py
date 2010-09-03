# encoding: utf-8

from notifo import Notifo

__author__ = "Daniel Schauenberg"
__version__ = "0.2.1"
__license__ = "MIT"

def send_message(login, pw, **kwargs):
    return Notifo(login, pw).send_message(**kwargs)

def send_notification(login, pw, **kwargs):
    return Notifo(login, pw).send_notification(**kwargs)

def subscribe_user(login, pw, user):
    return Notifo(login, pw).subscribe_user(user)
