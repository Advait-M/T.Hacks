#!/usr/bin/python
import sentiment

# -----------------------------------------------------------------------
# twitter-search-geo
#  - performs a search for tweets close to New Cross, and outputs
#    them to a CSV file.
# -----------------------------------------------------------------------

import csv

from twitter import *

latitude = 8.6195#42.3#18.563747#51.474144#49.28402 ##51.474144  # geographical centre of search
longitude = 0.8248#-83#-72.142439#-0.035401#-123.11765 ##-0.035401  # geographical centre of search
max_range = 200  # search range in kilometres
num_results = 1 # minimum results to obtain
outfile = "output.csv"

# -----------------------------------------------------------------------
# load our API credentials
# -----------------------------------------------------------------------
config = {}
with open("config.py") as f:
    code = compile(f.read(), "config.py", 'exec')
    exec(code, config)
# print(config)
# -----------------------------------------------------------------------
# create twitter API object
# -----------------------------------------------------------------------
twitter = Twitter(auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

# -----------------------------------------------------------------------
# open a file to write (mode "w"), and create a CSV writer object
# -----------------------------------------------------------------------
csvfile = open(outfile, "w")
csvwriter = csv.writer(csvfile)
# -----------------------------------------------------------------------
# add headings to our CSV file
# -----------------------------------------------------------------------
row = ["user", "text", "latitude", "longitude"]
csvwriter.writerow(row)

# -----------------------------------------------------------------------
# the twitter API only allows us to query up to 100 tweets at a time.
# to search for more, we will break our search up into 10 "pages", each
# of which will include 100 matching tweets.
# -----------------------------------------------------------------------
result_count = 0
last_id = None
while result_count < num_results:
    # -----------------------------------------------------------------------
    # perform a search based on latitude and longitude
    # twitter API docs: https://dev.twitter.com/docs/api/1/get/search
    # -----------------------------------------------------------------------
    query = twitter.search.tweets(q="", geocode="%f,%f,%dkm" % (latitude, longitude, max_range), count=100,
                                  max_id=last_id, until="2016-10-22")
    print(len(query["statuses"]))
    for result in query["statuses"]:
        # -----------------------------------------------------------------------
        # only process a result if it has a geolocation
        # -----------------------------------------------------------------------
        user = result["user"]["screen_name"]
        text = result["text"]
        text = text.encode('ascii', 'replace')

        # now write this row to our CSV file
        row = [user, text]
        csvwriter.writerow(row)
        result_count += 1
        sentiment.sentimentcalc(result["text"])
    last_id = result["id"]
    print()
    # -----------------------------------------------------------------------
    # let the user know where we're up to
    # -----------------------------------------------------------------------
    print("got %d results" % result_count)

# -----------------------------------------------------------------------
# we're all finished, clean up and go home.
# -----------------------------------------------------------------------
csvfile.close()

print("written to %s" % outfile)
print ()
