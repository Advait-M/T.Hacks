#!/usr/bin/python
import unicodedata
from django.utils import encoding

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *

def convuni(x):
    """
    >>> convert_unicode_to_string(u'ni\xf1era')
    'niera'
    """
    return encoding.smart_str(x, encoding='ascii', errors='ignore')
#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
with open("config.py") as f:
    code = compile(f.read(), "config.py", 'exec')
    exec(code, config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://dev.twitter.com/docs/api/1/get/search
#-----------------------------------------------------------------------
latitude = 18.563747

longitude = -72.142439#-0.035401  # geographical centre of search
max_range = 100
query = twitter.search.tweets(q = "hurricane", geocode="%f,%f,%dkm" % (latitude, longitude, max_range))

#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------
print ("Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"]))

#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
for result in query["statuses"]:
        print(result)
        creation, username, text, lat, long = convuni(result["created_at"]), convuni(result["user"]["screen_name"]), convuni(result["text"], convuni(result["geo"]["coordinates"][0]), convuni(result["geo"]["coordinates"][1]))
##        unicodedata.normalize("NFKD", creation).encode("ascii", "ignore")
##        unicodedata.normalize("NFKD", username).encode("ascii", "ignore")
##        unicodedata.normalize("NFKD", text).encode("ascii", "ignore")
        print("(%s) @%s %s %s" % (creation, username, text, lat, long))
