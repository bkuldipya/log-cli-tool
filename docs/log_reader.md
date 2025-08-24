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
