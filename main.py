#!/usr/bin/python3

import os, sys, glob 

from config import config
from util import *
from MySQL import MySQL
from Mongo import Mongo


def main():
	if len(sys.argv) == 2:
		action = sys.argv[1]
		if action == "mysql.export":
			MySQL(config["mysql"]).export_dbs()
		elif action == "mysql.import":
			MySQL(config["mysql"]).import_dbs()
		elif action == "mongo.export":
			Mongo(config["mongo"]).export_dbs()
		elif action == "mongo.export":
			Mongo(config["mongo"]).import_dbs()
		elif action == "debug":
			debug()
		else:
			print("unknown action")
			usage()
	else:
		print("please pass parameter")
		usage()

if __name__ == '__main__':
	main()
