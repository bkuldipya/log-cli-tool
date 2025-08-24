#!/usr/bin/env python
# coding: utf-8

# 
#  **main module tasks:**<br>
#  Acts as the command-line interface (CLI) controller.<br>
#  1.Parses CLI arguments.<br>
#  2.Selects the correct mode (file, journald-static, journald-live).<br>
#  3.Coordinates flow by calling appropriate modules based on mode and user input.<br>
#  4.Handles basic input validation and error messaging.<br>
#  5.Manages the overall program execution.<br>

# In[ ]:


import sys
import argparse
import log_reader
import output_handler
import journald_log_parser


parser = argparse.ArgumentParser(description="Log Investigator CLI Tool")                  #1.1  #1.2


parser.add_argument(
    "--mode",
    choices=["file","journald-static","journald-live"],
    help='mode selection: "file" to parse a log file, "journald-static" to parse stored journald logs, "journald-live" for live streaming logs',
    type=str
)
parser.add_argument(
    "--path",
    help='path to the log file (required for "file" mode)',
    type=str
)
parser.add_argument(
    "--since",
    help='start time filter (same format as journalctl, e.g. "YYYY-MM-DD HH:MM:SS"or "today" or "yesterday")',
    type=str
)
parser.add_argument(
    "--until",
    help='end time filter(same format as journalctl, e.g. "YYYY-MM-DD HH:MM:SS" or "today" or "yesterday")',
    type=str
)
parser.add_argument(
    "--output",
    help="choose where to save the extracted IOCS (provide a filename)",
    type=str
)


args = parser.parse_args()                                                   #1.3

if len(sys.argv) == 1:                                                       #d.1 #d.2
    print(f"No options provided. Use -h or --help for usage information.")
    sys.exit(1)


try:                                                                         #a.1
#checking mode and using the correct module

    if args.mode == "file":
        if args.path is not None:
            for ioc in log_reader.parse_log_file(args.path):             #c.1  #generator object, you have to force evaluation
                output_handler.handle_output(ioc,args.output)
        else:
            print("Provide the path to the log file that you want to parse and extract the IOCs of ssh logs",file=sys.stderr)   #b.1 #b.2


    elif args.mode == "journald-static":

        #checking arguments manually to send to journald_log_parser
        if (args.since and args.until):
            result = journald_log_parser.parse_static("--since",args.since,"--until",args.until)

        elif args.since:
            result = journald_log_parser.parse_static("--since",args.since)

        elif args.until:
            result = journald_log_parser.parse_static("--until",args.until)          #result is of type str


        if result.startswith("Error"):
            output_handler.handle_errors(result,args.output)

        else:
            for ioc in log_reader.parse_log_static(result):             #c.2 
                output_handler.handle_output(ioc,args.output)   



    elif args.mode == "journald-live":                                #e.1
        #run live parser
        pass



#Fatal Error handling

except FileNotFoundError as e:                                                                #a.1
    print("File not found",e,file=sys.stderr)
    sys.exit(1)
except PermissionError as e:                                                                  #a.2
    print("you don't have permission to read or create files",file=sys.stderr)
    sys.exit(1)
except OSError:                                                                               #a.3
    print("General file I/O Error",file=sys.stderr)
    sys.exit(1)


# In[ ]:


#Note : sys helps the programmer to use the variables and functions maintained by the interpreter
#Note : argparse helps the programmer to define the arguments needed for the program and also to parse the arguments given by the user
#1.1Create an ArgumentParserObject
#1.2 ArgumentParser class has two important methods - add_argument() and parse_args() 
'''#1.3 parse_args() reads the arguments from the command line and parses them, 
it stores the value of the arguments in the attributes of the name space object. parse_args() takes a sequence of the cli args and returns
a namespace object, whose attributes has the same name as the argument name defined and they hold the value given to the argument in cli'''

#a Error handling code. 
#a.1 If file not present then print the error in the stderr stream and exit with a returncode(exitcode) 1
#a.2 If user don't have permission to read or write files then print the error message and exit the program with rc 1
#a.3 If there is a general error problem, then print error, and return 1.
'''#b.1 sys.stderr is a file object. File object is an object that represents an open file on the OS. 
It acts as an interface b/w program and actual file'''
'''#b.2 By default, print() sends its output to sys.stdout. When the file parameter is used, the output is instead 
directed to the object provided. This object must have a write() method, as the print() function calls this method 
to write the data'''

'''#c.1 #c.2 Read the log_reader module comments to know more. Here, the for loop automatically calls the next() function on the generator
object. next() function task is to run the code from the last yield to the next yield and fetch the value of this next yield. When the generator
exhaust, means there are no more values to yield then the generator object will raise an exception called StopIteration, but this is handled
by the for loop automatically, no need to manually handle it'''

'''#d.1 #d.2
sys.argv is a list of command-line arguments. sys.argv[0] → always the script name or path to the script, 
sys.argv[1:] → the actual arguments passed by the user.'''

#e.1 will implement in future

