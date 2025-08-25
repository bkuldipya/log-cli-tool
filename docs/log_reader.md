#log_reader module tasks:<br>
---

### Overview
1.Reads raw logs from static sources and feeds them line-by-line for IOC extraction.<br>
2.Reads from a log file line-by-line (parse_logs_from_file).<br>
3.Reads from a string of logs (like journalctl output) line-by-line (parse_logs_static).<br>
4.Does not analyze or extract IOCs itself, just prepares raw log lines.<br>
5.yields a extracted_iocsionary if found from the ioc_extractor module<br>

---

### Behaviour of parse_logs_from_file() function \[Generator\]<br>
\#1.1 Input: file_path (name or location of the file)<br>
\#1.2 output: dictionary one at a time (uses yield)<br>

---
### Comments<br>
\#2.1 each line is separated by a newline (\n)<br>
\#2.1.U Updated this line. To show the line no. for each extracted IOCs or If there's an error in the log line. <br>
\#f.readlines() returns a list of strings, where each string represent line.
\#enumerate takes a sequence as an input and has a default argument called start. Once called it returns an iterator object (think iterator same as generator), means to get the output of this iterator you need to force evaluate. When you call next() function on this enumerate object you get a tuple of two elements (position,element). And as here, we are using for loop on the iterator object then for loop automatically calls the next() function on the enumerate object, also the for loop handles the StopIteration exception too. <br>

\#2.2 for each line it calls the function inside the ioc_extractor module<br>
\#3.1 from main() the result is given here (stored in log_data).<br>
\#3.2 splitlines() is used to get a list of all the lines that are separated by a newline<br>
\#3.3 to check if there are emptylines so no errors are raised in the extract_iocss() function.<br>
\#E.1 Can raise FileNotFoundError which is a fatal error (means cannot be ignored) (hence needs to be caught in main.py)<br>
\#E.2 Can raise an error if the file does not contains string (can be ignored), thus using try/except here so that the program can #continue processing the next lines of the file.<br>

---
### parse_logs_from_file explanation flow: (same for parse_logs_static)
For each line the function extract_iocs() in the ioc_extractor module gets run. This function returns a dictionary(extracted_iocs) if match or 
None if no match. Suppose there is a match then the condition becomes True and yield extracted_iocs gets run.<br>
Some theory: yield is a keyword used to make a function act as a generator. If a function has yield in it then the function 
acts as a generator. Whenever this function is called the code inside the function doesn't gets executed directly after you call 
instead it returns a generator object. This object can remember its state between calls.<br>
next() is a builtin function in python used to get the next value from the generator object. When you call next() on the generator object
it executes the code till the next yield and returns the value. Then when you again call next() on that generator object, for first time calling the code gets executed till the yield is encountered and when executing the yield then it returns the value. Then for all the subsequent times calling the code gets executed from the previous yield till the next yield gets executed and then the value gets returned. Basically, you get value only on demand.<br>
Suppose there is no match then we ignore it.
