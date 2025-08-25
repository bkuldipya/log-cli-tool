#journald_log_parser module
---
### Comments <br>
\# subprocess is used to spawn(launch) new processes.<br><br>
\# a.1 To get arbitrary number of arguments. args(local variable) will collect all the arguments and store them in a tuple<br>
\# a.2 extend takes an iterable as an input and appends the elements of that iterable to the object in which the method is called upon.<br>
\#a.3 subprocess.run returns a CompletedProcessObject. Here, my program waits for other program to finish and then after the child process gets finished it returns a CompletedProcessObject. This object has attributes from which we can know the output of the child process and even errors, returncode too.<br>
\# Also, as the default argument text=True is set then the input/output for the child program is of type string not bytes.<br>
\#a.4 If the program ran successfully then the exit code is 0. If the exit code is something else then it prints the errors.<br>
<br>
\#b.1 args is tuple. *args can save any no. of inputs given to it and store them in a tuple.<br>
\#b.2 the result is of type string and is appended to the list. Useful for scalability purposes.<br>
