#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# **ioc_extractor module tasks:**
# Performs pattern matching and extraction of Indicators of Compromise (IOCs) from individual log lines.
# See "docs/ioc_extractor.md" for explanations (comments)


# In[ ]:


import re

ssh_pattern = (r"([A-Z][a-z]{2}[ ]+\d+ \d+\:\d+\:\d+) "                                             #1.1
 r"\w+ "                                                                                            #1.2 
 r"(\w+)\[\d+\]\: "                                                                                 #1.3
 r"failed password (?:for invalid user|for user|for) (\w+) from (\d+\.\d+\.\d+\.\d+) port \d+ \w+"  #1.4
) 


def extracted_iocs(log_line):                                                                      #3.1
    d = {}                                                                                         #3.2
    match_ssh = re.search(ssh_pattern,log_line,flags=re.IGNORECASE)


    if match_ssh:
        d["service"] = str(match_ssh.group(2))
        d["username"] = str(match_ssh.group(3))                                                    #3.3
        d["ip"] = str(match_ssh.group(4))
        d["timestamp"] = str(match_ssh.group(1))

    if d:                                                                                          #3.4
        return d
    else:                                                                                          #3.5
        return None


