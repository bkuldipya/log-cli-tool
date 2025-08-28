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
\#(a) comments for patterns
\# a.1 timestamp<br>
\# a.2 hostname(name of the computer)<br>
\# a.3 service name and service id(pid) also capturing the service to know what type of log<br>
\# a.4 log line<br>
\# a.5 Extracting Sucessful Login attempts too. <br> 
There are two ways a successul authentication can happen<br>
1. When the client provides the correct password (password-based authentication).<br>
2. When the client proves ownership of a private key that matches the server's authorized public key (key-based authentication).<br><br>

\# b.1 each log line is a string<br>
\# b.2 treat this as a local variable, so as to create a new empty dict everytime for each new log line<br>
\# b.3 converting to string so when the dictionary object gets converted to json then the syntax doesn't breaksbecause json key-value pairs needed to be of type str<br>
\# b.4 if dictionary object is not empty then execute (if dictionary is empty, then the condition becomes false and will not execute the code inside the if block)<br>
\# b.5 returns None, when there is no match<br>

---
### Ignore <br>
\# later implementation, "ignore" for now<br>

\# 2.1 timestamp<br>
\# 2.2 hostname(name of the computer)<br>

\# sudo_pattern = (r"([A-Z][a-z]{2}[ ]+\d+ \d+\:\d+\:\d+) "     \#2.1 <br>
\#  r"\w+ "                                                     \#2.2 <br>
\#  r"sudo\[\d+\]\:[ \t]"                     <br>
\#  r"[^;]+\;[^;]+\;[^;]+\;[ \t]COMMAND=(.*)" <br> 
\# )                                          <br>

\# match_sudo = re.search(sudo_pattern,log_line,flags=re.IGNORECASE)<br>
\#  elif match_sudo:<br>
\#         d["command"]=str(match_sudo.group(2))<br>
       
  
