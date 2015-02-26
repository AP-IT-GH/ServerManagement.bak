"""
    awake.py: tool to eat CPU cycles
    awake.py is copyright 2015 Jeroen Doggen.
"""

import time
import datetime

while True:
	""" Print 'stay awake' in an infinte loop"""
	print("Stay awake")
	print("Current time: " + str(datetime.datetime.now()))
	time.sleep(100) # you can lower the load by adding some sleep
