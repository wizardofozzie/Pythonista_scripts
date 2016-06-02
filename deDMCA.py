# coding: utf-8
## download copyright deleted torrents from KAT 

import appex, console, re, sys, requests
from bs4 import BeautifulSoup
from urllib import urlencode, quote_plus

baseurl = "http://kekasworld2.comli.com/KAT/DMCA/"
RE_MAGNET = re.compile(ur"^[0-9a-fA-F]{64}$")
RE_URL_KAT = re.compile(ur"^http(s)?://kat.cr/*.html$")
RE_URL_KW = re.compile(ur"^http://kekasworld2.comli.com/KAT/DMCA/?*")


tries = 0
inp = ''
while not inp or tries <= 3:
    inp = console.input_alert("Enter hash or KAT URL")
    if re.match("^[0-9a-fA-F]{64}$", inp) or re.match(ur"^http(s)?://kat.cr/*.html$", inp):
        break
    else:
        tries += 1

if inp[0] in 'hH':
    fmturl = baseurl + "?url={0}".format(inp)
else:
    fmturl = baseurl + "?hash={0}".format(inp)
    console.write_link("http://torcache.net/torrent/{hash}.torrent".format(hash=inp))


magnet_uris = []

def get_bs4_urls(pageurl):
	assert pageurl.startswith("http://kekasworld2.comli.com/KAT/DMCA/?") and pageurl.endswith(".html")
	r = requests.get(pageurl)
	if not r.ok:
		sys.stderr.write("no connection w/ kekasworld2.comli.com")
		return 
	soup = BeautifulSoup( r.text, "html.parser")
	ahrefs = []
	for link in soup.find_all("a"): 
		if str(link.get("href")).startswith(("magnet:?", "http://torcache.net/torrent/")):
			ahrefs.append(link)
			if str(link.get("href")).startswith("magnet:?"):
				magnet_uris.append(link)
		else:
			ahrefs = [""] * 2
	res = "{} {}".format(*ahrefs).strip()

	
def write_links(*args):
	for arg in args:
		if arg is None or not arg.startswith("magnet") or not arg.startswith("http://torcache"):
			continue
		console.write_link(str(arg), str(arg))
			
write_links()

#https://kat.cr/the-walking-dead-s06e15-1080p-web-dl-dd5-1-h264-rarbg-t12331954.html
#forumurl = "https://kat.cr/community/search/thread/?search=The+walking+dead&thread=kat-tv-uploaders-unite-post-your-dmca-d-torrents-here"
