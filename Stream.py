#! /usr/bin/env python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "bunkdeath"
__date__ = "$Mar 10, 2012 10:54:32 AM$"

import json
import pycurl

STREAM_URL = "https://stream.twitter.com/1/statuses/sample.json"

USER = "bunkdeath"
PASS = "*********"


def on_receive(data):
    parseStreamingTweet(data)


def parseStreamingTweet(tweet):
    print "\n"
    try:
        singleTweetJson = json.loads(tweet)
        for index in singleTweetJson:
            if index == 'text':
                print "text : ", singleTweetJson[index]
            if index == 'created_at':
                print "created at : ", singleTweetJson[index]
            if index == 'geo':
                print "geo : ", singleTweetJson[index]
            if index == 'in_reply_to_status_id':
                print "in reply to : ", singleTweetJson[index]
    except ValueError:
        print tweet
        return

conn = pycurl.Curl()
conn.setopt(pycurl.USERPWD, "%s:%s" % (USER, PASS))
conn.setopt(pycurl.URL, STREAM_URL)
conn.setopt(pycurl.WRITEFUNCTION, on_receive)
conn.perform()
