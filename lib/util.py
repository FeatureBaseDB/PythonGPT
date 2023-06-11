import os
import string
import random
from coolname import generate_slug

from lib.database import featurebase_query

def random_string(size=6, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

# super basic authentication
auth_filename = ".auth"
username_key = "username="


def set_username(username):
	with open(auth_filename, "w") as file:
		file.write(f"{username_key}{username}\n")
	return username

def get_username():
	if os.path.exists(auth_filename):
		with open(auth_filename, "r") as file:
			content = file.readlines()
			username_found = False
			for line in content:
				if line.startswith(username_key):
					username = line[len(username_key):].strip()
					username_found = True
					print(f"system> You are logged in as `{username}`.")
					return username
			if not username_found:
				username = generate_slug(2)
	else:
		username = generate_slug(2)

	return set_username(username)
		
def drop_databases():
	# drop FeatureBase database
	fb_query = featurebase_query( { "sql": "DROP TABLE python_keyterms;" })
	fb_query = featurebase_query( { "sql": "DROP TABLE python_code;" })

def create_databases():
	# create FeatureBase database
	fb_table = "python_code"
	fb_query = featurebase_query( { "sql": "CREATE TABLE %s (_id string, filename string, prompt string, explanation string, prev_id string, code string);" % fb_table })

	# check status
	if fb_query.get('error'):
		if "exists" in fb_query.get('error'):
			print("FeatureBase database `%s` already exists." % fb_table)
		else:
			print(fb_query.get("explain"))
			print("FeatureBase returned an error. Check your credentials or create statement!")
			sys.exit()
	else:
		print("Created `%s` database on FeatureBase Cloud." % fb_table)


	# create FeatureBase database
	fb_table = "python_keyterms"
	fb_query = featurebase_query( { "sql": "CREATE TABLE %s (_id string, filenames stringset, uuids stringset, page_ids stringset);" % fb_table }
	)

	# check status
	if fb_query.get('error'):
		if "exists" in fb_query.get('error'):
			print("FeatureBase database `%s` already exists." % fb_table)
		else:
			print(fb_query.get("explain"))
			print("FeatureBase returned an error. Check your credentials or create statement!")
			sys.exit()
	else:
		print("Created `%s` database on FeatureBase Cloud." % fb_table)
