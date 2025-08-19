#!/usr/bin/env python
# coding: utf-8

# **output_handler module tasks:**<br>
# Manages output of extracted data or errors.<br>
# 1.Prints extracted IOC dictionaries or error messages to the console if no output file is specified.<br>
# 2.Appends the JSON-formatted data or errors to an output file if a filename is provided.<br>
# 3.Keeps output logic separate from parsing and extraction logic.<br>

# In[ ]:


import json
import ioc_extractor


def handle_output(ioc_dict,output):
    if output is None:
        print(ioc_dict)

    else:
        with open(output,"a") as f:
            f.write(json.dumps(ioc_dict)+"\n")

def handle_errors(string,output):
    if output is None:
        print(string)
    else:
        with open(output,"a") as f:
            f.write(string+"\n")


