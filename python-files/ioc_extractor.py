#!/usr/bin/env python
# coding: utf-8

# **ioc_extractor module tasks:**<br>
# Performs pattern matching and extraction of Indicators of Compromise (IOCs) from individual log lines.<br>
# 1.Uses regex to detect and parse failed SSH login attempts from log lines.<br>
# 2.Extracts relevant fields: timestamp, service, username, IP address.<br>
# 3.Returns a dictionary with IOC details or None if no IOC found.<br>
# 4.Encapsulates all logic related to IOC identification.<br>

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

    if d:
        return d
    else:
        return None



#Extracts IOCs(ip,timestamp,username) from a given log line using regex

#Behavior of function (extracted_iocs)
#Input - string (one log line)
#Output - dictionary

#1.1timestamp
#1.2hostname(name of the computer)
#1.3service name and service id(pid) also capturing the service to know what type of log
#1.4log line


#2.1timestamp
#2.2hostname(name of the computer)

#3.1each log line is a string
#3.2treat this as a local variable, so as to create a new empty dict everytime for each new log line
#3.3converting to string so if want to convert to json then can do it
#3.4if d is not empty then do it (if empty then it means it is false)
#3.5 returns empty {} only when there is no match but not good for long lines where ssh/sudo not there
#test: 
extracted_iocs("Aug 12 19:00:01 server sshd[12345]: Accepted password for alice from 192.168.1.10 port 54321 ssh2")
extracted_iocs("Aug 12 19:05:15 server sshd[12346]: Failed password for invalid user bob from 10.0.0.5 port 2222 ssh2")

# In[ ]:


sudo_pattern = (r"([A-Z][a-z]{2}[ ]+\d+ \d+\:\d+\:\d+) "     #2.1
 r"\w+ "                                                     #2.2
 r"sudo\[\d+\]\:[ \t]"
 r"[^;]+\;[^;]+\;[^;]+\;[ \t]COMMAND=(.*)" 
)

match_sudo = re.search(sudo_pattern,log_line,flags=re.IGNORECASE)
 elif match_sudo:
        d["command"]=str(match_sudo.group(2))

