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
import journald_fetcher


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
            for lineno,extracted_iocs in log_reader.parse_logs_from_file(args.path):             #c.1  #generator object, you have to force evaluation
                output_handler.handle_output(lineno,extracted_iocs,args.output)    #changed
        else:
            print("Provide the path to the log file that you want to parse and extract the IOCs of ssh logs",file=sys.stderr)   #b.1 #b.2

        sys.exit(0)                                                        #exit (program ran successfully)


    #mode is journald-static
    elif args.mode == "journald-static":

        #check for which service the user wants the iocs
        if args.service == "ssh" :
            target_source = ["_COMM=sshd"]                                            #e.1
        elif args.service == "sudo":
            target_source = ["_COMM=sudo"]
        else:
            target_source = ["_COMM=sshd","_COMM=sudo"]


        #get the logs first from the journald
        log_results = journald_fetcher.fetch_journal_logs(*target_source,since=args.since,until=args.until)       #e.2 #e.3


        for log_data in log_results:

            if log_data.startswith("Error"):
                output_handler.handle_errors(log_data,args.output)

            #send logs to be read by log_reader and send one by one to ioc_extractor to get IOCs
            else:
                for lineno,extracted_iocs in log_reader.parse_logs_static(log_data):             #c.2 
                    output_handler.handle_output(lineno,extracted_iocs,args.output)   


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




