#181138
import re 
import time
import datetime
import calendar
import random
from datetime import datetime
import sys
import getopt
import argparse
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
for x in range(1,int(totalJobs) + 1):
    #Calculate whether this will be in 68 percent of data, 95, or 99.7
    #Standard Deviation Node: 57
    #Mean Nodes: 15
    #Standard Deviation Wallclock: 12597
    #Mean WallClock = 9276
	deviation = random.randrange(1, 100, 1)
	if deviation <= 68:
		randomNum = random.randrange(1,72,1)
		randomWallclock = random.randrange(1,21873,1)
	if deviation > 68 and deviation <= 95:
		randomNum = random.randrange(73, 129, 1)
		randomWallclock = random.randrange(21874, 34471, 1)
	if deviation > 95 and deviation <= 100:
		randomNum = random.randrange(130, 186, 1)
		randomWallclock = random.randrange(34472, 47069, 1)
	p = x*138
	myfile.write("		{")
	myfile.write("\n			\"id\": {},\n			\"profile\": \"Profile{}\",\n			\"res\": {},\n			\"subtime\":{},\n			\"walltime\": {}".format(x, randomWallclock,randomNum, p, randomWallclock+1))
	if x != int(totalJobs):
		myfile.write(" \n		},\n")
	else:
		myfile.write("\n		}\n")
#myfile.write("	],\n\n	\"profiles\": {\n		\"Profile1\": {\n			\"type\": \"parallel_homogeneous_total\",\n			\"cpu\": 50e10,\n			\"com\": 0\n		}\n	}\n}")	
myfile.write( "	],\n\n	\"profiles\": {\n		" )
#47070
for y in range(1,47070):
	if y != 47069:
		myfile.write("\"Profile{}\":".format(y))
		myfile.write("{\n			\"type\": \"parallel_homogeneous\",\n			\"cpu\":") 
		myfile.write("{}e9,\n			\"com\": 0".format(y,y))
		myfile.write("\n		},\n		")
	else:
		#myfile.write("\"Profile\"{}: {\n		\"type\": \"parallel_homogeneous_total\",\n			\"cpu\": {}e10,\n			\"com\")
		myfile.write("\"Profile{}\":".format(y))
		myfile.write("{\n		\"type\": \"parallel_homogeneous\",\n			\"cpu\":") 
		myfile.write("{}e9,\n			\"com\": 0".format(y,y))
		myfile.write("\n		}\n	}\n}")




myfile.close()	
