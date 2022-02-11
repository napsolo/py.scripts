#!/usr/bin/python3

import sys, argparse, pprint, re, json
 
# Dealing with arguments 
# Initialize parser
parser = argparse.ArgumentParser(description='To get JSON objects having certain pattern in specified key from JSONL file in stdin.')
 
# Adding arguments
parser.add_argument("-r", "--regex", help = "Regex to look in value of defined key.", required=True )
parser.add_argument("-k", "--key", help = "Key to look for pattern in JSON object.", required=True )
 
# Read arguments from command line
args = parser.parse_args()

# Reading stdin a
for obj in sys.stdin:
    try:
        # Converting JSON Object to Python object
        line = json.loads(obj)
        # Using if statement to select a regex(args.regex) from specific key(args.key) in python object 
        if re.match(args.regex, str(line[args.key])):
            # Using pprint library to pretty print output for increased readability
            pprint.pprint(line, indent=1)
            # Printing empty line as separator
            print ()
    # Handling KeyError exception for objects with no key(args.key) provided
    except KeyError:
        continue

