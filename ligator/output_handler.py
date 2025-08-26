#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# **output_handler module** 
# Manages output of extracted data or errors.
# See "docs/output_handler.md" for explanations (comments)


# In[ ]:


import json

def handle_output(lineno, extracted_iocs, output, format):                     #1.2

    if output is None:    #print in screen                                                     #1.3

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



    else:                #save to file                                                  #1.4

        with open(output,"a") as f:                                                     #z.1


            if format=="ndjson":
                extracted_iocs["lineno"] = lineno
                f.write(json.dumps(extracted_iocs))
                f.write("\n")

            elif format=="ndjson-pretty":
                extracted_iocs["lineno"] = lineno
                f.write(json.dumps(extracted_iocs,indent=4))
                f.write("\n")


            elif format=="text":   
                f.write(f"Line No: {lineno}\n")
                f.write(f'   auth_status: {extracted_iocs["auth_status"]}\n')
                f.write(f'   auth_methods: {extracted_iocs["auth_methods"]}\n') 
                f.write(f'   username: {extracted_iocs["username"]}\n')
                f.write(f'   ip: {extracted_iocs["ip"]}\n')
                f.write(f'   timestamp: {extracted_iocs["timestamp"]}\n')
                f.write(f'   log_source: {extracted_iocs["log_source"]}\n')




            else:                                                      #format is compact
                f.write(f'[{lineno}] '), 
                f.write(f'{extracted_iocs["timestamp"]} | ') 
                f.write(f'{extracted_iocs["log_source"]} | ')
                f.write(f'status={extracted_iocs["auth_status"]} | ')
                f.write(f'method={extracted_iocs["auth_methods"]} | ')
                f.write(f'user={extracted_iocs["username"]} | ')
                f.write(f'ip={extracted_iocs["ip"]}\n')


                                                                                #1.1

def handle_errors(string,output):
    if output is None:
        print(string)
    else:
        with open(output,"a") as f:
            f.write(string+"\n")




# \#1.2 if the user doesn't provides value for --output then output local variable is by default None<br>
# \#1.2 if the user doesn't provides value for format then by default the value of format is equal to compact
# \#1.3 the results will be shown in the terminal
# \#1.4 if output is not None means the user wants to save the output to some file, then this code will run<br>
# 
# \#z.1 Edge case: If you give the same file name for output then the next results gets appended to the previous.
