 # main module<br>
 Acts as the command-line interface (CLI) controller.<br>
 1.Parses CLI arguments.<br>
 2.Selects the correct mode (file, journald-static, journald-live).<br>
 3.Coordinates flow by calling appropriate modules based on mode and user input.<br>
 4.Handles basic input validation and error messaging.<br>
 5.Manages the overall program execution.<br>

---

### Comments
\# Note : sys helps the programmer to use the variables and functions maintained by the interpreter.<br>
\# Note : argparse helps the programmer to define the arguments needed for the program and also to parse the arguments given by the user.<br><br>
\# a Create ArgumentParser object to define args for program and to parse them.<br>
\# a.1Create an ArgumentParserObject.<br>
\# a.2 ArgumentParser class has two important methods - add_argument() and parse_args().<br> 
\# a.3 By default argparse reformats "help" text (wraps lines, ignores indentation). So use the argument (formatter_class=argparse.RawTextHelpFormatter) in ArgumentParser to preserve your spaces and newlines exactly in the help text of each argument your program can take.<br>
\# a.4 parse_args() reads the arguments from the command line and parses them, 
it stores the value of the arguments in the attributes of the name space object. parse_args() takes a sequence of the cli args and returns
a namespace object, whose attributes has the same name as the argument name defined and they hold the value given to the argument in cli.<br><br>

\#b.1 sys.argv is a list of command-line arguments given. sys.argv[0] → always the script name or path to the script, sys.argv[1:] → the actual arguments passed by the user.<br>
<br>

\# c try-except-finally block to handle errors and file open/close.<br>
\# c.1 If file not present then print the error in the stderr stream and exit with a returncode(exitcode) 1. <br>
\# c.2 If user don't have permission to read or write files then print the error message and exit the program with returncode(exitcode) 1.<br>
\# c.3 Operation intended to perform on a file is attempted on a Directory, returncode=1.<br>
\# c.4 If there is a general error problem, then print error, and return 1.<br><br>

\# d code outside modes<br>
\# d.1 opening output file here if given by the user (opening manually so as to not to duplicate any code), also opening the file once so the efficiency of program gets improved<br><br>

\# e code inside modes<br>
\# e.1 Read the log_reader module comments to know more. Here, the for loop automatically calls the next() function on the generator
object. next() function task is to run the code from the last yield to the next yield and fetch the value of this next yield. When the generator gets
exhausted,i.e, there are no more values to yield then the generator object will raise an exception called StopIteration, but this is handled
by the for loop automatically, no need to manually handle it.<br>
\# e.2 passing file-like object, fh is the file handle (open file)<br>
\# e.3 sys.stderr is a file object. File object is an object that represents an open file on the OS.
It acts as an interface b/w program and actual file.<br>
\# e.4 By default, print() sends its output to sys.stdout. When the file parameter is used, the output is instead 
directed to the object provided. This object must have a write() method, as the print() function calls this method 
to write the data<br>
\#e.5 taking it as a list for consistency across codes, also now if programmer wants to add new type of logs to extract iocs then they can do it easily<br>
\# e.6 unpacking the elements of this list, because if list is passed directly then any modification done inside the function will affect the original list.<br>
\# e.7 returned value is also a list. This is for scalability purposes.<br>
\# e.8 iterate over the returned list; for each element(string) in the returned list, if the string startwith Error then send the string to output_handler.handle_errors() function.
Else send the string to log_reader.parse_logs_static() to get the extracted_iocs. And once you get it send it to ouput_handler.handle_output()<br><br>

\# f.1 will implement in future<br>
