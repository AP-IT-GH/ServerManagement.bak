"""
    download.py: tool to eat CPU cycles
    download.py is copyright 2015 Jeroen Doggen.
"""

import time
import urllib
import os

attempts = 0
limit = 1000

while attempts < limit:
	""" Download a file in a loop -> causes a high server load"""
	attempts += 1
	try:
		#urllib.urlretrieve("http://google.com/index.html", filename="index.html")
		urllib.urlretrieve("http://localhost", filename="index.html")
		os.remove("index.html")
		time.sleep(0.1) # you can lower the load by adding some sleep time
		print(attempts)
	except urllib.URLError as e:
		print type(e)
