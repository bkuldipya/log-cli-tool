#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#**log_reader module tasks:**
# Reads raw logs from static sources and feeds them log_line-by-log_line for IOC extraction.
# See "docs/log_reader.md" for explanations (comments)


# In[ ]:


import sys
import ioc_extractor

def parse_logs_from_file(file_path):                                                   #1.1 #1.2         
    with open(file_path,'r') as f:                                               #E.1
        for lineno,log_line in enumerate(f.readlines(), start=1):                   #2.1    #changed #2.1.U     
            if len(log_line) == 0:                                                   #3.3
                continue
            try:
                extracted_iocs = ioc_extractor.extract_iocs(log_line)                    #2.2  #E.2
                if extracted_iocs is not None:
                    yield (lineno, extracted_iocs)                                     #changed 
            except TypeError as e:
                print(f"Line No: {lineno}","Error: this line is not of type str", f"Description:{e}", file=sys.stderr, sep="   ")
                continue


def parse_logs_static(log_data):                                                    #3.1 #3.2
    for lineno,log_line in enumerate(log_data.splitlines(), start=1):
        if len(log_line) == 0:                                                           #3.3
            continue
        else:
            extracted_iocs = ioc_extractor.extract_iocs(log_line)
            if extracted_iocs is not None:
                yield (lineno, extracted_iocs) 


