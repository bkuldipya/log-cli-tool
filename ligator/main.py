
# **main module**<br>
# Acts as the command-line interface (CLI) controller.<br>
# See "docs/main.md" for explanations (comments)



import sys
import argparse
import log_reader
import output_handler
import journald_fetcher


#a Create ArgumentParser object to define args for program and to parse them
parser = argparse.ArgumentParser(description="Log Investigator CLI Tool",
                                formatter_class=argparse.RawTextHelpFormatter)                  #a.1  #a.2  #a.3


#Mode and input group (Specify the source)
source_group = parser.add_argument_group("Source Options")

source_group.add_argument(
    "--mode",
    choices=["file","journald-static","journald-live"],
    help=('mode selection: \n'
    '    "file" to parse a log file\n' 
    '    "journald-static" to parse stored journald logs\n'
    '    "journald-live" for live streaming logs'),    
    type=str
)
source_group.add_argument(
    "--path",
    help='path to the log file (required for "file" mode)',
    type=str
)


#Log filters
filter_group = parser.add_argument_group("Log Filtering Options","To be used only in the journald mode")

filter_group.add_argument(
    "--service",
    help=('Specify which service logs to analyze:\n'                                                 #a.3
    '    "ssh" for SSH login attempts\n'
    '    "sudo" for sudo command usage\n'
    '     Defaults to both if not provided'),
    choices=['ssh','sudo'],
    type=str
)        
filter_group.add_argument(
    "--since",
    help='start time filter (same format as journalctl, e.g. "YYYY-MM-DD HH:MM:SS"or "today" or "yesterday")',
    type=str
)
filter_group.add_argument(
    "--until",
    help='end time filter(same format as journalctl, e.g. "YYYY-MM-DD HH:MM:SS" or "today" or "yesterday")',
    type=str
)

#Output and Format group
output_group = parser.add_argument_group("Output Options")

output_group.add_argument(
    "--output",
    help="choose where to save the extracted IOCS (provide a filename)",
    type=str
)
output_group.add_argument(
    "--format",
    choices = ['ndjson','ndjson-pretty','text','text-compact'],
    default = 'ndjson',
    help=("Output format (default: %(default)s):\n"
    "    ndjson         - Newline-delimited JSON (1 json object per line) (best for machine parsing).\n"
    "    ndjson-pretty  - Newline-delimited JSON with indentation (human-readable).\n"
    "    text           - Multiline structured text, verbose (human-readable).\n"
    "    text-compact   - Single-line, log-style output, concise (human-readable)."),
    type = str
)


args = parser.parse_args()                                                   #a.4

if len(sys.argv) == 1:                                                       #b.1
    print(f"No options provided. Use -h or --help for usage information.")
    sys.exit(1)


#c try-except-finally block to handle errors and file open/close
try:                                                                         

    #d code outside modes
    #d.1 opening output file here if given by the user
    fh = None
    if args.output is not None:
        fh = open(args.output,"w")


    #e code inside modes
    #checking mode and using the correct module

    #If mode is file
    if args.mode == "file":
        if args.path is not None:
            for lineno,extracted_iocs in log_reader.parse_logs_from_file(args.path):  #e.1  generator object, you have to force evaluation
                output_handler.handle_output(lineno,extracted_iocs,args.format,fh)    #e.2 passing file-like object

        else:
            print("Provide the path to the log file that you want to parse and extract the IOCs of ssh logs",file=sys.stderr)   #e.3 #e.4

        sys.exit(0)                                                        #exit (program ran successfully)



    #mode is journald-static
    elif args.mode == "journald-static":

        #check for which service the user wants the iocs
        if args.service == "ssh" :
            target_source = ["_COMM=sshd"]                                            #e.5
        elif args.service == "sudo":
            target_source = ["_COMM=sudo"]
        else:
            target_source = ["_COMM=sshd","_COMM=sudo"]

        #get the logs first from the journald
        log_results = journald_fetcher.fetch_journal_logs(*target_source,since=args.since,until=args.until)       #e.6 #e.7

        for log_data in log_results:                                                         #e.8
            if log_data.startswith("Error"):
                output_handler.handle_errors(log_data,fh)

            #send logs to be read by log_reader and send one by one to ioc_extractor to get IOCs
            else:                                                               
                for lineno,extracted_iocs in log_reader.parse_logs_static(log_data):             #e.1 
                    output_handler.handle_output(lineno,extracted_iocs,args.format,fh)   


        sys.exit(0)                                                           #exit (program ran successfully)



    #mode is journald-live
    elif args.mode == "journald-live":                                #f.1
        #run live parser
        pass



#c Fatal Error handling

except FileNotFoundError as e:                                                                #c.1
    print("File not found",e,file=sys.stderr)
    sys.exit(1)
except PermissionError as e:                                                                  #c.2
    print("You don't have permission to read or create files",file=sys.stderr)
    sys.exit(1)
except IsADirectoryError:                                                                     #c.4
    print("Operation intended to perform on a file is attempted on a Directory",file=sys.stderr)
except OSError:                                                                               #c.4
    print("General file I/O Error",file=sys.stderr)
    sys.exit(1)

finally:                                                                                     
    if fh:                                                                         #d.2
        fh.close()


