

# **output_handler module** 
# Manages output of extracted data or errors.
# See "docs/output_handler.md" for explanations (comments)



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
        print(f"Line No: {lineno}")
        for k,v in extracted_iocs.items():                                     #c.3
            print(f"    {k}: {v}")

    else:                                                                      #format is text-compact
        print(f'[{lineno}]',end=" ")
        for k,v in extracted_iocs.items():
            print(f"{k}={v}|",end="")
        print("")



#writes to a file 
def write_output(lineno,extracted_iocs,format,fh):                         
    if format=="ndjson":
        extracted_iocs["lineno"] = lineno
        fh.write(json.dumps(extracted_iocs)+"\n")                                #d.1

    elif format=="ndjson-pretty":
        extracted_iocs["lineno"] = lineno
        fh.write(json.dumps(extracted_iocs,indent=4)+"\n")

    elif format=="text":   
        fh.write(f"Line No: {lineno}\n")                                         #d.2
        for k,v in extracted_iocs.items():
            fh.write(f"    {k}: {v}\n")

    else:                                                                        #format is compact
        fh.write(f'[{lineno}] ')
        for k,v in extracted_iocs.items(): 
            fh.write(f"{k}={v}|")
        fh.write("\n")    



