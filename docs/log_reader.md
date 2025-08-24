#log_reader module tasks:<br>
---

### Overview
1.Reads raw logs from static sources and feeds them line-by-line for IOC extraction.<br>
2.Reads from a log file line-by-line (parse_log_file).<br>
3.Reads from a string of logs (like journalctl output) line-by-line (parse_log_static).<br>
4.Does not analyze or extract IOCs itself, just prepares raw log lines.<br>
5.yields a ioc_dictionary if found from the ioc_extractor module<br>

---

### Behaviour of parse_log_file() function \[Generator\]<br>
\#1.1 Input: file_path (name or location of the file)<br>
\#1.2 output: dictionary one at a time (uses yield)<br>

---
### Comments<br>
\#2.1 each line is separated by a newline (\n)<br>
\#2.2 for each line it calls the function inside the ioc_extractor module<br>
\#3.1 from main() the result is given here (stored in stdout_str).<br>
\#3.2 splitlines() is used to get a list of all the lines that are separated by a newline<br>
\#3.3 to check if there are emptylines so no errors are raised in the extracted_iocs() function.<br>
\#E.1 Can raise FileNotFoundError which is a fatal error (means cannot be ignored) (hence needs to be caught in main.py)<br>
\#E.2 Can raise an error if the file does not contains string (can be ignored), thus using try/except here so that the program can #continue processing the next lines of the file.<br>

---
### parse_log_file explanation flow: (same for parse_log_static)
For each line the function extracted_iocs() in the ioc_extractor module gets run. This function returns a dictionary(ioc_dict) if match or 
None if no match. Suppose there is a match then the condition becomes True and yield ioc_dict gets run.<br>
Some theory: yield is a keyword used to make a function act as a generator. If a function has yield in it then the function 
acts as a generator. Whenever this function is called the code inside the function doesn't gets executed directly after you call 
instead it returns a generator object. This object can remember its state between calls.<br>
next() is a builtin function in python used to get the next value from the generator object. When you call next() on the generator object
it executes the code till the next yield and returns the value. Then when you again call next() on that generator object, for first time calling the code gets executed till the yield is encountered and when executing the yield then it returns the value. Then for all the subsequent times calling the code gets executed from the previous yield till the next yield gets executed and then the value gets returned. Basically, you get value only on demand.<br>
Suppose there is no match then we ignore it.
