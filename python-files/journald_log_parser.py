#!/usr/bin/env python
# coding: utf-8

# **Parse Journald Logs**<br>
# **Subtasks:** <br>
# *1.* run journalctl command with the arguments given by the user using the subprocess module
# 

# In[ ]:


import subprocess


def parse_static(*args):                                                           #a.1
    li = ["journalctl"] 
    li.extend(args)                                                                #a.2
    CPObject = subprocess.run(li,capture_output=True,text=True)                    #a.3

    if CPObject.returncode == 0:                                                   #a.4
        return CPObject.stdout

    else:
        return "Error: "+CPObject.stderr

*#a.1* To get arbitrary number of arguments. args local variable will collect all the arguments and store them in a tuple<br>
*#a.2* extend takes an iterable as an input and appends the elements of that iterable to the object in which the method is called upon.
*#a.3* subprocess.run returns a CompletedProcessObject 
*#a.4* If the program ran successfully then the exit code is 0. If the exit code is something else then it prints the errors.