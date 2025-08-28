#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#**log_reader module tasks:**
# Reads raw logs from static sources and feeds them log_line-by-log_line for IOC extraction.
# See "docs/log_reader.md" for explanations (comments)


# In[ ]:


import sys
import ioc_extractor

#(a) Comments for this function
def parse_logs_from_file(file_path):                                                   #a.1.1 #a.1.2         
    with open(file_path,'r') as f:                                                     #a.2.1
        for lineno,log_line in enumerate(f, start=1):                                  #a.3.1 #a.3.2   
            if len(log_line.strip()) == 0:                                             #a.3.3
                continue
            try:                                                                       #a.2.2
                extracted_iocs = ioc_extractor.extract_iocs(log_line.strip())          #a.3.4  
                if extracted_iocs is not None:
                    yield (lineno, extracted_iocs)                                     #a.3.5 
            except TypeError as e:
                print(f"Line No: {lineno}","Error: this line is not of type str", f"Description:{e}", file=sys.stderr, sep="   ")   #a.3.6
                continue 


#(b) Comments for this function
def parse_logs_static(log_data):                                                     #b.1.1 #b.1.2
    for lineno,log_line in enumerate(log_data.splitlines(), start=1):                #b.2.1
        if len(log_line) == 0:                                                       #b.2.2
            continue
        else:
            extracted_iocs = ioc_extractor.extract_iocs(log_line)                    #a.3.4
            if extracted_iocs is not None:
                yield (lineno, extracted_iocs)                                       #a.3.5


