#!/usr/bin/env python
# coding: utf-8

# **log_reader module tasks:**<br>
# 1.Reads raw logs from static sources and feeds them line-by-line for IOC extraction.<br>
# 2.Reads from a log file line-by-line (parse_log_file).<br>
# 3.Reads from a string of logs (like journalctl output) line-by-line (parse_log_static).<br>
# 4.Does not analyze or extract IOCs itself, just prepares raw log lines.<br>
# 5.yields a ioc_dictionary if found from the ioc_extractor module<br>
# 
# 
# *#a* Behaviour of parse_log_file function<br>
# *#1.1* Input = file_path (name or location of the file)<br>
# *#1.2* #output = dictionary one at a time<br>
# *#2*<br>
# *#2.1* each line is separated by a newline (\n)<br>
# *#2.2* for each line it calls the function inside the ioc_extractor module<br><br>
# *#b* Behaviour of parse_log_static()<br>
# Input: string<br>
# Output: dictionary one at a time
# 
# 

# In[ ]:


import ioc_extractor

def parse_log_file(file_path):               #1.1 #1.2        
    with open(file_path,'r') as f:
        for line in f:                                        #2.1
            ioc_dict = ioc_extractor.extracted_iocs(line)                #2.2
            if ioc_dict is not None:
                yield ioc_dict        

def parse_log_static(stdout):
    for line in stdout.splitlines():
        ioc_dict = ioc_extractor.extracted_iocs(line)
        if ioc_dict is not None:
            yield ioc_dict                

