#!/usr/bin/python3

import ms8250b
import time
import os

def run():
	if os.name == "nt":
		meter = ms8250b.Multimeter("COM14")
	else:
		meter = ms8250b.Multimeter("/dev/ttyUSB0")

	while(1):
		time.sleep(1)
		v = meter.getValue()
		if "value" in v.keys():
			print("Value: %f %s" % (v["value"], v["type"]))

if __name__ == "__main__":
	run()