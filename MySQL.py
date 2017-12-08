#!/usr/bin/python3

import os, sys, glob 

class MySQL():
	"""Import and export database for mysql"""
	def __init__(self, config):
		self.config = config

	def get_all_db(self, source="source"):
		print("saving db names...")
		username	= self.config[source]["username"]
		password	= self.config[source]["password"]
		db_name_file= self.config[source]["backup_dir"] + "/mysql.db_name"

		cmd = "mysql -u {} --password='{}' -e 'show databases' > {}".format(username, password, db_name_file)
		# print(cmd)
		os.system(cmd)

		db_list = open(db_name_file).read().splitlines()
		# print(db_list)
		if db_list:
			db_list.remove("Database")
			return db_list
		print("Not found any database")
		sys.exit(1)


	def export_dbs(self):
		backup_dir = self.config["source"]["backup_dir"]
		username = self.config["source"]["username"]
		password = self.config["source"]["password"]

		# filter
		all_db = self.get_all_db()
		export_db = []
		for db in all_db:
			user_input = input("Do you want to export {}: ".format(db))
			if user_input in ['y', 'Y']:
				export_db.append(db)
		print("\n" * 3)

		# confirm
		print("Are you to export this dbs:")
		for db in export_db:
			print(db)
		print("\n" * 3)
		user_input = input("If yes then type 'y' else 'n': ")
		if user_input not in ['y', 'Y']:
			sys.exit(1)

		print('exporting...')
		for db in export_db:
			file = backup_dir + "/" + db + ".sql"
			print("dumping {} db to {} file...".format(db, file))
			cmd = "mysqldump -u {} --password='{}' {} > {}".format(username, password, db, file)
			# print(cmd)
			os.system(cmd)
			print("dumped {}".format(db))
			print("\n" * 3)
		print("all export done, check {} directory".format(backup_dir))


	def import_dbs(self):
		backup_dir = self.config["destination"]["backup_dir"]
		username = self.config["destination"]["username"]
		password = self.config["destination"]["password"]

		# filter
		all_dbs_path = glob.glob("{}/*.sql".format(backup_dir))
		all_dbs = [ os.path.basename(db).replace(".sql", "") for db in all_dbs_path ]
		# print(all_dbs)
		import_db = []
		for db in all_dbs:
			user_input = input("Do you want to import {}: ".format(db))
			if user_input in ["y", "Y"]:
				import_db.append(db)
		print("\n" * 3)

		print("You want to import this dbs")
		for db in import_db:
			print(db)
		user_input = input("'y' for yes, anythin else is no: ")
		if user_input not in ['y', 'Y']:
			sys.exit(1)

		print("\n" * 3)

		for db in import_db:
			file = backup_dir + "/" + db + ".sql"
			print("importing {} from {}".format(db, file))

			# create db
			cmd = "mysql -u {} --password='{}' -e 'CREATE DATABASE {}'".format(username, password, db)
			# print(cmd)
			os.system(cmd)

			# import
			cmd = "mysql -u {} --password='{}' {} < {}".format(username, password, db, file)
			# print(cmd)
			os.system(cmd)
			print("imported {}".format(db))
			print("\n" * 3)
		print("all import done.")
		imported_dbs = self.get_all_db("destination")
		for db in imported_dbs:
			print(db)
		print("---" * 3)
