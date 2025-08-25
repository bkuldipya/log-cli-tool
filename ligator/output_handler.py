#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# **output_handler module** 
# Manages output of extracted data or errors.
# See "docs/output_handler.md" for explanations (comments)


# In[ ]:


import json

def handle_output(lineno,extracted_iocs,output):
    if output is None:
        print(f"Line No: {lineno}",extracted_iocs,sep="   ")                                    #changed

    else:
        with open(output,"a") as f:
            f.write(json.dumps(extracted_iocs)+"\n")                     #1.1

def handle_errors(string,output):
    if output is None:
        print(string)
    else:
        with open(output,"a") as f:
            f.write(string+"\n")




# In[ ]:


#two types of output - pp and single line compact

