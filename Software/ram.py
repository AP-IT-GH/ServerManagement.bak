"""
    ram.py: tool to eat RAM memory
    ram.py is copyright 2015 Jeroen Doggen.
"""

import time

a = []
while True:
    print ("Currently using " + str(len(a)) + "MB Ram Memory")
    a.append(' ' * 10**6)
    time.sleep(0.1) # adding some sleep to slow down the process
