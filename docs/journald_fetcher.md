#journald_log_parser module
---
### Comments <br>
\# a.1 subprocess is used to spawn(launch) new processes.<br><br>
\# b.1 To get arbitrary(any) number of arguments. Because, suppose the source of logs is more like user wants to know for ssh as well as sudo logs, target_source(local variable) will collect all the arguments and store them in a tuple.<br>
\# b.2 for each source in the tuple do the following task.<br>
\# b.3 append takes one argument as a input and adds this argument to the list from where it is called. extend takes a sequence as an argument, it adds all the elements of that sequence to the list from where it is called.<br>
\# b.4 subprocess.run returns a CompletedProcessObject. Here, my program waits for other program to finish and then after the child process gets finished it returns a CompletedProcessObject. This object has attributes from which we can know the output of the child process and even errors, returncode too. Also, as the default argument text=True is set then the input/output for the child program is of type string not bytes.<br>
\# b.5 If the program ran successfully then the exit code is 0. If the exit code is something else then it prints the errors.<br>
\# b.6 the output (string type) is appended to the list. This is for scalability purposes.<br>
\# b.7 if there are errors of the journalctl process then that error is first preponeded with "Error" so this can be processed differently in the main.py module.<br>
