# ioc_extractor module

---
### Overview

 Performs pattern matching and extraction of Indicators of Compromise (IOCs) from individual log lines.<br>
1. Uses regex to detect and parse failed SSH login attempts from log lines.
2. Extracts relevant fields: timestamp, service, username, IP address.
3. Returns a dictionary with IOC details or None if no IOC found.
4. Encapsulates all logic related to IOC identification.
---
### Behaviour
Extracts IOCs(ip,timestamp,username) from a given log line using regex

Behavior of function --> extracted_iocs()<br>
Input - string (one log line)<br>
Output - dictionary containing iocs<br>

---
### Comments
\# 1.1 timestamp<br>
\# 1.2 hostname(name of the computer)<br>
\# 1.3 service name and service id(pid) also capturing the service to know what type of log<br>
\# 1.4 log line<br>


\# 2.1 timestamp<br>
\# 2.2 hostname(name of the computer)<br>

\# 3.1 each log line is a string<br>
\# 3.2 treat this as a local variable, so as to create a new empty dict everytime for each new log line<br>
\# 3.3 converting to string so if want to convert to json then the syntax doesn't breaks, as for json key-value pair needed to be of type str<br>
\# 3.4 if d is not empty then execute (if it is empty means the condition becomes false)<br>
\# 3.5 returns None, when there is no match<br>

---
### Ignore <br>
\# later implementation, "ignore" for now<br>

\# sudo_pattern = (r"([A-Z][a-z]{2}[ ]+\d+ \d+\:\d+\:\d+) "     \#2.1 <br>
\#  r"\w+ "                                                     \#2.2 <br>
\#  r"sudo\[\d+\]\:[ \t]"                     <br>
\#  r"[^;]+\;[^;]+\;[^;]+\;[ \t]COMMAND=(.*)" <br> 
\# )                                          <br>

\# match_sudo = re.search(sudo_pattern,log_line,flags=re.IGNORECASE)<br>
\#  elif match_sudo:<br>
\#         d["command"]=str(match_sudo.group(2))<br>
       
  
