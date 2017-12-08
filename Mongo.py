#!/usr/bin/python3

import os, sys, glob

class Mongo():
	"""Mongo import export"""
	def __init__(self):
		self.config = config

	def get_all_dbs():
		pass

	def export_dbs():
		backup_dir = self.config["source"]["backup_dir"]
		cmd = "mongodump --out {}".format(backup_dir)
		# print(cmd)
		os.system(cmd)

	def import_db():
		backup_dir = self.config["destination"]["backup_dir"]
		cmd = "mongorestore {}".format(backup_dir)
		# print(cmd)
		os.system(cmd)
