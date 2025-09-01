#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# **ioc_extractor module tasks:**
# Performs pattern matching and extraction of Indicators of Compromise (IOCs) from individual log lines.
# See "docs/ioc_extractor.md" for detailed explanations (comments)


# In[ ]:


import re

#(a) comments for patterns
ssh_pattern = re.compile(                                                                #a.1
    r"(?P<timestamp>[A-Z][a-z]{2}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+"                     # Timestamp (e.g., 'Jan 12 14:33:21')
    r"[a-zA-Z_][a-zA-Z0-9._-]{0,31}\s+"                                                  # Hostname (up to 32 chars, starts with letter/underscore)
    r"(?P<log_source>\w+)\[(?P<pid>[0-9]+)\]:\s*"                                        # Process name 'sshd' with PID in brackets
    r"(?P<auth_status>failed|accepted)\s+"                                               # Authentication status (failed/accepted)
    r"(?P<auth_methods>password|publickey)\s+"                                           # Authentication method (password/publickey)
    r"(?:for invalid user|for user|for)\s+"        
    r"(?P<username>[a-zA-Z_][a-zA-Z0-9._-]{0,31})\s+"                                    # Target Username
    r"from\s+"
    r"(?P<source_ip>\d+\.\d+\.\d+\.\d+)\s+"                                              # Source IP address
    r"port\s+(?P<port>\d+)\s+"                                                           # Port number used
    r"\w+", re.IGNORECASE                                                                # ssh version/protocol   
) 

sudo_pattern = re.compile(
    r"(?P<timestamp>[A-Z][a-z]{2}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+"                     # Timestamp (e.g., 'Jan 12 14:33:21')
    r"(?P<hostname>[a-zA-Z_][a-zA-Z0-9._-]{0,31})\s+"                                    # Hostname (up to 32 chars, starts with letter/underscore)
    r"sudo\[(?P<pid>[0-9]+)\]:\s*"                                                       # Process name 'sudo' with PID in brackets
    r"(?P<invoker>[a-zA-Z_][a-zA-Z0-9._-]{0,31})\s+:\s+"                                 # User who invoked sudo
    r"(?:(?P<failed_attempts>[0-9]+)\s+incorrect password attempt(?:s)?(?:\s+;\s+)?)?"   # Optional: failed sudo attempts count  
    r"(?:TTY=(?P<tty>[^ ]+)(?:\s+;\s+)?)?"                                               # Optional: controlling terminal
    r"(?:PWD=(?P<pwd>[^ ]+)(?:\s+;\s+)?)?"                                               # Optional: working directory from where sudo was run
    r"(?:USER=(?P<target_user>[a-zA-Z_][a-zA-Z0-9._-]{0,31}|[0-9]+)(?:\s+;\s+)?)?"       # Optional: target user for sudo (name or UID)
    r"(?:COMMAND=(?P<command>.*))?", re.IGNORECASE                                       # Optional: command executed with sudo
)


#(b) comments for function
def extract_iocs(log_line):                                                                     #b.1
    extracted_iocs = {}                                                                         #b.2
    match_ssh = ssh_pattern.search(log_line)
    match_sudo = sudo_pattern.search(log_line)

    if match_ssh:
        extracted_iocs = {k:v for k,v in match_ssh.groupdict().items()}                         #b.3

    if match_sudo:
        extracted_iocs = {k:v for k,v in match_sudo.groupdict().items() if v is not None}       #b.3



    if extracted_iocs:                                                                          #b.4
        return extracted_iocs
    else:                                                                                       #b.5
        return None


