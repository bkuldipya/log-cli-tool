#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#**log_reader module tasks:**
# Reads raw logs from static sources and feeds them line-by-line for IOC extraction.
# See "docs/log_reader.md" for explanations (comments)


# In[ ]:


import sys
import ioc_extractor

def parse_log_file(file_path):                                                   #1.1 #1.2         
    with open(file_path,'r') as f:                                               #E.1
        for line in f:                                                           #2.1         
            if len(line) == 0:                                                   #3.3
                continue
            try:
                ioc_dict = ioc_extractor.extracted_iocs(line)                    #2.2  #E.2
                if ioc_dict is not None:
                    yield ioc_dict        
            except TypeError as e:
                print(f"Error: this line is not of type str", f"Description:{e}", file=sys.stderr, sep="    ")
                continue


def parse_log_static(stdout_str):                                                    #3.1 #3.2
    for line in stdout_str.splitlines():
        if len(line) == 0:                                                           #3.3
            continue
        else:
            ioc_dict = ioc_extractor.extracted_iocs(line)
            if ioc_dict is not None:
                yield ioc_dict 


