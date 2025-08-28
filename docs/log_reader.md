#log_reader module tasks:<br>
---

### Overview
1.Reads raw logs from static sources and feeds them line-by-line for IOC extraction.<br>
2.Reads from a log file line-by-line (parse_logs_from_file).<br>
3.Reads from a string of logs (like journalctl output) line-by-line (parse_logs_static).<br>
4.Does not analyze or extract IOCs itself, just prepares raw log lines.<br>
5.yields a extracted_iocsionary if found from the ioc_extractor module<br>

---

### Comments for parse_logs_from_file() function \[Generator\]<br>
\ #a.1.1 Input: file_path (name or location of the file)<br>
\ #a.1.2 output: tuple one at a time (uses yield)<br><br>
\# a.2.1 Opening the input file here to read line by line; this code can raise FileNotFoundError (input file not found) which is a fatal error (means cannot be ignored) (hence needs to be caught in main.py)<br>
\# a.2.2 Can raise an error if the file does not contains string (can be ignored), thus using try/except here so that the program can continue processing the next lines of the file.<br><br>
\# a.3.1 f.readlines() reads the entire file into memory at once. It returns a list of strings. Each element in that list is one line from the file, including the trailing newline (\n) at the end (unless it’s the last line and the file doesn’t end with a newline). A “line” = the chunk of text up to the next newline character. A line here means: characters from the current position up to the next newline (\n), or EOF if there’s no newline. f.readlines() = list of those chunks. But the problem here is that f.readlines() will load the entire file into the memory, so if you have a large file then this is not good. So use f instead, here python will read lazily, means only on demand it will read the next line, as we're using for loop so we are forcefully evaluating.<br>
\# a.3.2 To show the line no. for each line of the file; enumerate() takes a sequence as an input and has a default argument called start. Once called it returns an iterator object (think iterator same as generator), means to get the output of this iterator you need to force evaluate. When you call next() function on this enumerate object you get a tuple of two elements (position,element). And as here, we are using for loop on the iterator object then for loop automatically calls the next() function on the enumerate object, also the for loop handles the StopIteration exception too. So here we are force evaluating enumerate, and as enumerate takes a sequence as an input, so f becomes that iterator, and enumerate() forces f to get the lines. In our case: for lineno, log_line in enumerate(f, start=1): gives us (line_number, line_text) for each line in the file.<br>
\# a.3.3 to check if there are emptylines so no errors are raised in the extract_iocs() function and also to skip it.<br>
\# a.3.4 for each line it calls the function inside the ioc_extractor module<br>
\# a.3.5 yields a tuple (lineno,extracted_iocs).<br>
\# a.3.6 If the line in the file is not of type string then there could be a TypeError. So handling it here.<br><br>


### Comments for parse_logs_static() function \[Generator\]<br>
\# b.1.1 Input: string (output of journalctl program) <br>
\# b.1.2 output: tuple one at a time (uses yield)<br><br>
\# b.2.1 splitlines() is used to get a list of all the lines that are separated by a newline, but each line doesn't have a trailing new line.<br>
\# b.2.2 as elements in the list doesn't have a trailing new line so we don't need to use strip() function here.<br><br>


---
### parse_logs_from_file/parse_logs_static explanation flow: 
For each line the function extract_iocs() in the ioc_extractor module gets run. This function returns a dictionary(extracted_iocs) if match or 
None if no match. Suppose there is a match then the condition becomes True and yield extracted_iocs gets run.<br>
Some theory: yield is a keyword used to make a function act as a generator. If a function has yield in it then the function 
acts as a generator. Whenever this function is called the code inside the function doesn't gets executed directly after you call 
instead it returns a generator object. This object can remember its state between calls.<br>
next() is a builtin function in python used to get the next value from the generator object. When you call next() on the generator object
it executes the code till the next yield and returns the value. Then when you again call next() on that generator object, for first time calling the code gets executed till the yield is encountered and when executing the yield then it returns the value. Then for all the subsequent times calling the code gets executed from the previous yield till the next yield gets executed and then the value gets returned. Basically, you get value only on demand.<br>
Suppose there is no match then we ignore it.
