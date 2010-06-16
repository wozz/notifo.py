# encoding: utf-8

""" notifo.py - python wrapper for notifo.com """

import json
import urllib
import urllib2

class Notifo:
    """ Class for wrapping notifo.com """
    def __init__(self, user, api_secret):
        self.user = user
        self.api_secret = api_secret
        self.root_url = "https://api.notifo.com/v1/"

    def subsribe_user(self, user):
        """ method to subscribe a user to a service
        """
        url = self.root_url + "subscribe_user"
        values = {}
        values["username"] = user
        return self._query(url, values)

    def send_notification(self):
        """ method to send a message to a user
        """
        pass


    def _query(self, url, data = None):
        """ query method to do HTTP POST/GET

            Parameters:
                url -> the url to POST/GET
                data -> header_data as a dict (only for POST)

            Returns:
                Parsed JSON data as dict
                or
                None on error
        """
        # build basic auth stuff
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, url, self.user, self.api_secret)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)

        if data is not None: # we have POST data if there is data
            values = urllib.urlencode(data)
            request = urllib2.Request(url, values)
        else: # do a GET otherwise
            request = urllib2.Request(url)
        try:
            response = urllib2.urlopen(request)
        except IOError: # no connection
            return None
        json_data = response.read()
        data = json.loads(json_data)
        return data