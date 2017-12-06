#!/usr/bin/python3


def usage():
	print("""
Usgae python3 db_export.py [action]
	mysql.export
	mysql.import
	mongo.export
	mongo.import
""")

def debug():
	# save_db_name()
	# get_db_name()
	# mysql_import()
	mysql = MySQL()
	mongo = Mongo()


def seprator(n=1):
	print("\n" * n)
