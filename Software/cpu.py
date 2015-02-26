"""
    cpu.py: tool to eat CPU cycles
    cpu.py is copyright 2015 Jeroen Doggen.
"""

import time

while True:
	""" Do nothing in an infinite loop -> causes 100% CPU load"""
	pass
	#time.sleep(0.000001) # you can lower the load by adding some sleep
