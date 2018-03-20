import os
import pandas as pd
import yaml
from IPython import embed
import argparse
import re

# ---------------------------------- Config -----------------------------------

base_path = '..'


# ---------------------------------- Program ----------------------------------


parser = argparse.ArgumentParser(description='convert master yml\'s to directory structure, or reverse')
parser.add_argument("command", type=str, nargs=1, help="command")
args = parser.parse_args()
command = args.command[0]
print command



def from_master():

	# --- diagnoses

	with open("../master-diagnoses.yml") as stream:
	    try:
	        master_diagnoses = (yaml.load(stream))
	    except yaml.YAMLError as exc:
	        print(exc)

	# make new folder
	os.system("mkdir " + base_path + "/diagnoses")

	for d in master_diagnoses.values():
		
		# make new folder
		os.system("mkdir " + base_path + "/diagnoses/" + d['name'])

		# write summary to summary.md
		file = open( base_path + "/diagnoses/" + d['name'] + "/summary.md", 'w')
		file.write(d['summary'])
		file.close()

		# remove summary from diagnosis
		d.pop('summary')		

		# write remaining info to attributes.yml
		file = open( base_path + "/diagnoses/" + d['name'] + "/attributes.yml", 'w')
		file.write(yaml.dump(d, default_flow_style=False))
		file.close()

	# --- symptoms

	with open("../master-symptoms.yml") as stream:
	    try:
	        master_symptoms = (yaml.load(stream))
	    except yaml.YAMLError as exc:
	        print(exc)

	# make new folder
	os.system("mkdir " + base_path + "/symptoms")

	for d in master_symptoms.values():
		
		# make new folder
		os.system("mkdir " + base_path + "/symptoms/" + d['name'])

		# write summary to summary.md
		file = open( base_path + "/symptoms/" + d['name'] + "/summary.md", 'w')
		file.write(d['summary'])
		file.close()

		# remove summary from diagnosis
		d.pop('summary')		

		# write remaining info to attributes.yml
		stream = open(base_path + "/symptoms/" + d['name'] + "/attributes.yml", 'w')
		yaml.dump(d, stream, default_flow_style=False) 






if command == 'from_master':
	from_master()
elif command == 'to_master':
	print "to master"
else:
	print "cannot find command"








	# embed()
	# ddf = pd.DataFrame(master_diagnoses.values())
	# ddf.columns = [re.sub('-','_',c) for c in ddf.columns.values.tolist()]
	# for d in ddf.itertuples():
		# print yaml.dump(d)

