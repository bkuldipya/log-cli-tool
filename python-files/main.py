#!/usr/bin/env python
# coding: utf-8

# **main module tasks:**<br>
# Acts as the command-line interface (CLI) controller.<br>
# 1.Parses CLI arguments.<br>
# 2.Selects the correct mode (file, journald-static, journald-live).<br>
# 3.Coordinates flow by calling appropriate modules based on mode and user input.<br>
# 4.Handles basic input validation and error messaging.<br>
# 5.Manages the overall program execution.<br>

# In[ ]:


import argparse
import log_reader
import output_handler
import journald_log_parser

parser = argparse.ArgumentParser(description="Log Investigator CLI Tool")


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
    help="choose where to save the extracted IOCS",
    type=str
)


args = parser.parse_args()



#checking mode and using the correct module

if args.mode == "file":

    if args.path is not None:
        for ioc in log_reader.parse_log_file(args.path): #generator object, you have to force evaluation
            output_handler.handle_output(ioc,args.output)

    else:
        print("Provide the path to the log file that you want to parse and extract the IOCs of ssh logs")


elif args.mode == "journald-static":

    #checking arguments manually to send to journald_log_parser
    if (args.since and args.until):
        result = journald_log_parser.parse_static("--since",args.since,"--until",args.until)

    elif args.since:
        result = journald_log_parser.parse_static("--since",args.since)

    elif args.until:
        result = journald_log_parser.parse_static("--until",args.until)  #result is dict if error


    if "Error" in result:
        output_handler.handle_errors(result,args.output)

    else:
        for ioc in log_reader.parse_log_static(result):
            output_handler.handle_output(ioc,args.output)   



elif args.mode == "journald-live":
    #run live parser
    pass



