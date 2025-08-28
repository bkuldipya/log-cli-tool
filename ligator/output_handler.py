#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# **output_handler module** 
# Manages output of extracted data or errors.
# See "docs/output_handler.md" for explanations (comments)


# In[ ]:


import json

#(a) handles normal output (wrapper function) (calls other function)
def handle_output(lineno,extracted_iocs,format,fh=None):                     #a.1

    if fh is None:                                                           #print in screen                                          
        print_output(lineno,extracted_iocs,format)

    else:
        write_output(lineno,extracted_iocs,format,fh)                        #write to file


#(b) handles errors
def handle_errors(err_string,fh=None):                                       
    if fh is None:
        print(err_string,file=sys.stderr)
    else:
        fh.write(err_string+"\n")


#prints to the screen/terminal
def print_output(lineno,extracted_iocs,format):              
    if format=="ndjson":                                                        #c.1              
        extracted_iocs["lineno"] = lineno        
        print(json.dumps(extracted_iocs))                                       #c.2

    elif format=="ndjson-pretty":
        extracted_iocs["lineno"] = lineno
        print(json.dumps(extracted_iocs,indent=4))                                    

    elif format=="text":   
        print(f"Line No: {lineno}\n",
             f'   auth_status: {extracted_iocs["auth_status"]}\n',
             f'   auth_methods: {extracted_iocs["auth_methods"]}\n', 
             f'   username: {extracted_iocs["username"]}\n',
             f'   ip: {extracted_iocs["ip"]}\n',
             f'   timestamp: {extracted_iocs["timestamp"]}\n',
             f'   log_source: {extracted_iocs["log_source"]}'
             )

    else:                                                                      #format is text-compact
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
def write_output(lineno,extracted_iocs,format,fh):                         
    if format=="ndjson":
        extracted_iocs["lineno"] = lineno
        fh.write(json.dumps(extracted_iocs)+"\n")                                #d.1

    elif format=="ndjson-pretty":
        extracted_iocs["lineno"] = lineno
        fh.write(json.dumps(extracted_iocs,indent=4)+"\n")

    elif format=="text":   
        fh.write((f"Line No: {lineno}\n"                                         #d.2
               f'   auth_status: {extracted_iocs["auth_status"]}\n'
               f'   auth_status: {extracted_iocs["auth_status"]}\n'
               f'   auth_status: {extracted_iocs["auth_status"]}\n'
               f'   auth_methods: {extracted_iocs["auth_methods"]}\n'
               f'   username: {extracted_iocs["username"]}\n'
               f'   ip: {extracted_iocs["ip"]}\n'
               f'   timestamp: {extracted_iocs["timestamp"]}\n'
               f'   log_source: {extracted_iocs["log_source"]}\n'))

    else:                                                                        #format is compact
        fh.write((f'[{lineno}] '
               f'{extracted_iocs["timestamp"]} | '
               f'{extracted_iocs["log_source"]} | '
               f'status={extracted_iocs["auth_status"]} | '
               f'method={extracted_iocs["auth_methods"]} | '
               f'user={extracted_iocs["username"]} | '
               f'ip={extracted_iocs["ip"]}\n'))



