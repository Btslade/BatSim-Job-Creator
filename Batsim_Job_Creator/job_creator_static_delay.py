#181138
import re 
import time
import datetime
import calendar
import random
import sys
import getopt
import argparse
from datetime import datetime
random.seed(datetime.now())


if len(sys.argv) != 5:
    print("Usage: -j<job count> || --Jobs <job count> -o <output file name> || --File <output file name>")
    sys.exit(0)


argv = sys.argv[1:]
#print(argv)
try:
   opts, args = getopt.getopt(argv, "j:o:", ["Jobs=", "File=" ])
except getopt.GetoptError as err:
    print(err)
    print("Usage: -j<job count> || --Jobs <job count> -o <output file name> || --File <output file name>")
    opts = []
#print(opts)


for opt, arg in opts:
    if opt in ["-j", "--Jobs"]:
        jobCount = arg
    elif opt in ["-o", "--File"]:
        outputFileName = arg

#print(argv)


totalJobs = (re.search(r'\d+', jobCount).group())
myfile = open(outputFileName, 'w')
myfile.write("{\n	\"description\": \"Running first tests!\",\n	\"nb_res\": 10,\n	\"jobs\": [\n") 	
for x in range(1, int(totalJobs) +1):
	p = x*50
	myfile.write("		{")
	myfile.write("\n			\"id\": {},\n			\"profile\": \"Profile1\",\n			\"res\": 10,\n			\"subtime\":{},\n			\"walltime\": 51".format(x, p,))
	if x != int(totalJobs):
		myfile.write(" \n		},\n")
	else:
		myfile.write("\n		}\n")
myfile.write("	],\n\n	\"profiles\": {\n		\"Profile1\": {\n			\"type\": \"delay\",\n			\"delay\": 50\n				}\n	}\n}")	


myfile.close()	
