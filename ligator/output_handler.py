#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# **output_handler module** 
# Manages output of extracted data or errors.
# See "docs/output_handler.md" for explanations (comments)


# In[ ]:


import json

def handle_output(ioc_dict,output):
    if output is None:
        print(ioc_dict)

    else:
        with open(output,"a") as f:
            f.write(json.dumps(ioc_dict)+"\n")                     #1.1

def handle_errors(string,output):
    if output is None:
        print(string)
    else:
        with open(output,"a") as f:
            f.write(string+"\n")



