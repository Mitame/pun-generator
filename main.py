#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import sys

# rhymezone.com/r/rhyme.cgi?Word=wok&typeofrhyme=sim&org1=syl&org2=l

word = sys.argv[1]
sim_res = requests.get(
    "http://rhymezone.com/r/rhyme.cgi",
    {
        "Word": word,
        "typeofrhyme": "sim",
        "org1": "syl",
        "org2": "l"
    },
    headers={
        "User-Agent": "curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)"
    }
)

soup = BeautifulSoup(sim_res.text, "lxml")

similars = list(x.text for x in soup.find_all("a", {"class": "r"}))

quotes = open("quotes.txt", "r").read().strip().split("\n\n")

for quote in quotes:
    for sim in similars:
        sim = " %s " % sim # don't replace within words
        if sim in quote:
            # print("Replacing %s with %s." % (sim, word))
            print(quote.replace(sim, " %s " % word))
