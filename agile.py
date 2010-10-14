#!/usr/bin/python

# Add "alias tadd='python /path/to/agile.py'" to your 
# .bashrc or .bash_profile.  I put my agile.py in dropbox
# so I have access to it on every computer.

"""Agile Task Adder"""

__author__ = 'mark@agiletask.me (Mark Sanborn)'

VERSION = '0.0.1'

import urllib2
import urllib
import sys

# Config Variables
# ------------------------------------------------------------
creds = 'a6TrlL7P67yiRXi_cQ0o' # Agile Tasks API Key
agileUrl = 'http://agiletask.me/tasks?user_credentials=%s' % (creds)
# ------------------------------------------------------------

def send_data(url, query):
    """Sends data to specified url and returns response"""

    req = urllib2.Request(url)
    # urlencode the query dictionary
    req.data = urllib.urlencode(query)
    try:
        r = urllib2.urlopen(req)
        result = r.read()
    except:
        result = 'The url: %s is not responding.' % (url)
    return result

def main():
    # Get all args and put them into one string
    # so we dont have to put single quotes every
    # time we add a task.
    args = sys.argv[1:]
    task = ''
    for x in args:
        task = task + str(x) + ' '

    # Strip off the leading and trailing spaces of string
    task = task.strip()

    # Send urlencoded params to agile tasks
    query = {'task[name]':task}
    send_data(agileUrl, query)

if __name__ == '__main__':
    main()

