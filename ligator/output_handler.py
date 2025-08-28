#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# **output_handler module** 
# Manages output of extracted data or errors.
# See "docs/output_handler.md" for explanations (comments)


# In[ ]:


import json

#handles normal output (wrapper function) (calls other function)
def handle_output(lineno,extracted_iocs,format,fh=None):                     #1.2

    if fh is None:    #print in screen                                                     #1.3
        print_output(lineno,extracted_iocs,format)

    else:
        write_output(lineno,extracted_iocs,format,fh)


#handles errors
def handle_errors(err_string,fh=None):
    if fh is None:
        print(err_string,file=sys.stderr)
    else:
        fh.write(err_string+"\n")


#prints to the screen/terminal
def print_output(lineno,extracted_iocs,format):
    if format=="ndjson":
        extracted_iocs["lineno"] = lineno        #placeholder (to change)?
        print(json.dumps(extracted_iocs))

    elif format=="ndjson-pretty":
        extracted_iocs["lineno"] = lineno
        print(json.dumps(extracted_iocs,indent=4))                                    #placeholder (to change)

    elif format=="text":   
        print(f"Line No: {lineno}\n",
             f'   auth_status: {extracted_iocs["auth_status"]}\n',
             f'   auth_methods: {extracted_iocs["auth_methods"]}\n', 
             f'   username: {extracted_iocs["username"]}\n',
             f'   ip: {extracted_iocs["ip"]}\n',
             f'   timestamp: {extracted_iocs["timestamp"]}\n',
             f'   log_source: {extracted_iocs["log_source"]}'
             )

    else:                                                          #format is text-compact
        print(f'[{lineno}]', 
              f'{extracted_iocs["timestamp"]} |', 
              f'{extracted_iocs["log_source"]} |',
              f'status={extracted_iocs["auth_status"]} |',
              f'method={extracted_iocs["auth_methods"]} |',
              f'user={extracted_iocs["username"]} |',
              f'ip={extracted_iocs["ip"]}',
              sep=' '
             )


#writes to a file 
def write_output(lineno,extracted_iocs,format,fh):                           #1.4
    if format=="ndjson":
        extracted_iocs["lineno"] = lineno
        fh.write(json.dumps(extracted_iocs)+"\n")                                #1.4.1

    elif format=="ndjson-pretty":
        extracted_iocs["lineno"] = lineno
        fh.write(json.dumps(extracted_iocs,indent=4)+"\n")

    elif format=="text":   
        fh.write((f"Line No: {lineno}\n"                                         #1.4.2
               f'   auth_status: {extracted_iocs["auth_status"]}\n'
               f'   auth_status: {extracted_iocs["auth_status"]}\n'
               f'   auth_status: {extracted_iocs["auth_status"]}\n'
               f'   auth_methods: {extracted_iocs["auth_methods"]}\n'
               f'   username: {extracted_iocs["username"]}\n'
               f'   ip: {extracted_iocs["ip"]}\n'
               f'   timestamp: {extracted_iocs["timestamp"]}\n'
               f'   log_source: {extracted_iocs["log_source"]}\n'))

    else:                                                      #format is compact
        fh.write((f'[{lineno}] '
               f'{extracted_iocs["timestamp"]} | '
               f'{extracted_iocs["log_source"]} | '
               f'status={extracted_iocs["auth_status"]} | '
               f'method={extracted_iocs["auth_methods"]} | '
               f'user={extracted_iocs["username"]} | '
               f'ip={extracted_iocs["ip"]}\n'))

                                                                                                    #1.1            


# \#1.2 if the user doesn't provides value for --output then output local variable is by default None<br>
# \#1.2 if the user doesn't provides value for format then by default the value of format is equal to compact
# \#1.3 the results will be shown in the terminal
# \#1.4 if output is not None means the user wants to save the output to some file, then this code will run<br>
# \#.1.4.1 In storage or transmission (like in a file or over a network), all JSON data is ultimately text, i.e., a string of characters.
# But conceptually and semantically, we distinguish types inside the JSON: json objects, array, string, number. Everything is text when written to a file, but JSON parsers know how to interpret that text and restore the correct type in memory.<br>
# \#1.4.2 Python automatically concatenates adjacent string literals inside parentheses, and this works for multi-line strings too. This is called implicit string concatenation. Note, that there are no commas between those strings.
# 
# 
# \#z.1 Edge case: If you give the same file name for output then the next results gets appended to the previous.
# 
