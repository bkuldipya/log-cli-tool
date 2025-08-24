 # main module<br>
 Acts as the command-line interface (CLI) controller.<br>
 1.Parses CLI arguments.<br>
 2.Selects the correct mode (file, journald-static, journald-live).<br>
 3.Coordinates flow by calling appropriate modules based on mode and user input.<br>
 4.Handles basic input validation and error messaging.<br>
 5.Manages the overall program execution.<br>

---

### Comments
\# Note : sys helps the programmer to use the variables and functions maintained by the interpreter<br>
\# Note : argparse helps the programmer to define the arguments needed for the program and also to parse the arguments given by the user<br><br>
\# 1.1Create an ArgumentParserObject<br>
\# 1.2 ArgumentParser class has two important methods - add_argument() and parse_args()<br> 
\# 1.3 parse_args() reads the arguments from the command line and parses them, 
it stores the value of the arguments in the attributes of the name space object. parse_args() takes a sequence of the cli args and returns
a namespace object, whose attributes has the same name as the argument name defined and they hold the value given to the argument in cli<br>
<br>
#### Error handling code. (#a) <br>
\# a.1 If file not present then print the error in the stderr stream and exit with a returncode(exitcode) 1 <br>
\# a.2 If user don't have permission to read or write files then print the error message and exit the program with returncode(exitcode) 1<br>
\# a.3 If there is a general error problem, then print error, and return 1.<br><br>
\# b.1 sys.stderr is a file object. File object is an object that represents an open file on the OS.
It acts as an interface b/w program and actual file<br>
\#b.2 By default, print() sends its output to sys.stdout. When the file parameter is used, the output is instead 
directed to the object provided. This object must have a write() method, as the print() function calls this method 
to write the data<br><br>

\# c.1 \# c.2 Read the log_reader module comments to know more. Here, the for loop automatically calls the next() function on the generator
object. next() function task is to run the code from the last yield to the next yield and fetch the value of this next yield. When the generator
exhaust, means there are no more values to yield then the generator object will raise an exception called StopIteration, but this is handled
by the for loop automatically, no need to manually handle it<br><br>

\#d.1 \#d.2 sys.argv is a list of command-line arguments. sys.argv[0] → always the script name or path to the script, sys.argv[1:] → the actual arguments passed by the user.<br>
<br>
\#e.1 taking it as a list for consistency across codes, also now if programmer wants to add new type of logs to extract iocs then they can do it easily<br>
\#e.2 unpacking the elements of this list, because if list is passed directly then any modification done inside the function will affect the original list.<br>
\#e.3 returns value is also a list. This is for scalability purposes.<br>

\#f.1 will implement in future<br>
