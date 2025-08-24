#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# **main module**<br>
# Acts as the command-line interface (CLI) controller.<br>
# See "docs/main.md" for explanations (comments)


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
    "--service",
    help='Specify which service logs to analyze: "ssh" for SSH login attempts, "sudo" for sudo command usage. Defaults to both if not provided.',
    choices=['ssh','sudo'],
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

    #mode is file
    if args.mode == "file":
        if args.path is not None:
            for ioc in log_reader.parse_log_file(args.path):             #c.1  #generator object, you have to force evaluation
                output_handler.handle_output(ioc,args.output)
        else:
            print("Provide the path to the log file that you want to parse and extract the IOCs of ssh logs",file=sys.stderr)   #b.1 #b.2

        sys.exit(0)                                                        #exit (program ran successfully)


    #mode is journald-static
    elif args.mode == "journald-static":

        #check for which service the user wants the iocs
        if args.service == "ssh" :
            filter_comm = ["_COMM=sshd"]                                            #e.1
        elif args.service == "sudo":
            filter_comm = ["_COMM=sudo"]
        else:
            filter_comm = ["_COMM=sshd","_COMM=sudo"]


        #get the logs first from the journald
        logs_output = journald_log_parser.parse_static(*filter_comm,since=args.since,until=args.until)       #e.2 #e.3


        for result in logs_output:
            #send logs to be parsed and get IOCs
            if result.startswith("Error"):
                output_handler.handle_errors(result,args.output)
            else:
                for ioc in log_reader.parse_log_static(result):             #c.2 
                    output_handler.handle_output(ioc,args.output)   

        sys.exit(0)                                                           #exit (program ran successfully)


    #mode is journald-live
    elif args.mode == "journald-live":                                #f.1
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




