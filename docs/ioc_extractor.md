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
\# a.1 Compiling it first. When we import this module, python automatically runs the top-level code (executes variables, function definitions and regex compilation). In this case, the regex gets precompiled (python creates an internal regex object) and save it to memory to be used later by any program, thus saving the time.<br>
There are two ways a successul authentication can happen<br>
1. When the client provides the correct password (password-based authentication).<br>
2. When the client proves ownership of a private key that matches the server's authorized public key (key-based authentication).<br><br>

\# b.1 each log line is a string<br>
\# b.2 treat this as a local variable, so as to create a new empty dict everytime for each new log line<br>
\# b.3 matchobject.groupdict() returns a dictionary. Keys = the names of the named capturing groups in your regex. Values = the substrings actually matched by those groups. dictobject.items() returns a viewobject of the dictionary. When you iterate over this view object you get 2 element tuples of (key,value). Also I'm using dictionary comprehension, so that any named capturing group if it is not present in the match then that can be skipped (for sudo logs, specially) <br>
\# b.4 if dictionary object is not empty then execute (if dictionary is empty, then the condition becomes false and will not execute the code inside the if block)<br>
\# b.5 returns None, when there is no match<br>

---

       
  
