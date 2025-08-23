#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess                                                                  #1.1


def parse_static(*args):                                                           #a.1
    li = ["journalctl"] 
    li.extend(args)                                                                #a.2
    CPObject = subprocess.run(li,capture_output=True,text=True)                    #a.3

    if CPObject.returncode == 0:                                                   #a.4
        return CPObject.stdout

    else:
        return "Error: "+CPObject.stderr


# In[ ]:


#subprocess is used to spawn(launch) new processes.
#a.1 To get arbitrary number of arguments. args(local variable) will collect all the arguments and store them in a tuple<br>
#a.2 extend takes an iterable as an input and appends the elements of that iterable to the object in which the method is called upon.
#a.3 subprocess.run returns a CompletedProcessObject. Here, my program waits for other program to finish and then after the child process gets
#finished it returns a CompletedProcessObject. This object has attributes from which we can know the output of the child process and even errors, returncode too.
#Also, as the default argument text=True is set then the input/output for the child program is of type string not bytes.
#a.4 If the program ran successfully then the exit code is 0. If the exit code is something else then it prints the errors.

