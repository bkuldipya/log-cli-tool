#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# **output_handler module** 
# Manages output of extracted data or errors.
# See "docs/output_handler.md" for explanations (comments)


# In[ ]:


import json

def handle_output(extracted_iocs,output):
    if output is None:
        print(extracted_iocs)

    else:
        with open(output,"a") as f:
            f.write(json.dumps(extracted_iocs)+"\n")                     #1.1

def handle_errors(string,output):
    if output is None:
        print(string)
    else:
        with open(output,"a") as f:
            f.write(string+"\n")



