#!/usr/bin/env python
# coding: utf-8

# **Program to check if ssh.service is there or sshd.service is there in the system**<br>
# *#a.1*  running `systemctl list-units --all` and sending the output of this command to the file. <br>
# *#a.1.1* save all units whether they are inactive/active managed by systemd to a file.<br>
# *#a.2*  check if 'ssh.service' exists in the file(output of the above command).<br>
# *#a.2.1* if a line is selected then the grep command will show the line, if no line is selected then it will output nothing, but we are sending the output of this command to devnull (which just suppresses/ignores whatever comes to it).<br>
# *#a.3* But the grep program exit code (returncode) is 0 if a line is selected (a pattern is found) and 1 if a line is not selected (no pattern found) but the program ran successfully and 2 if the program fails.<br>
# *#a.3.1* Decide which service to use in this system.
# 

# In[ ]:


import subprocess

with open("sytemd-units.txt","w") as s:                                        #a.1
    subprocess.run(["systemctl","list-units","--all"],stdout=s,text=True)      #a.1.1          


temp_process_object = subprocess.run(["grep","-i","ssh.service","sytemd-units.txt"],stdout=subprocess.DEVNULL)  #a.2 

#a.2.1

if temp_process_object.returncode==0:                    #a.3 #a.3.1                                                   
    service = "ssh.service"
if temp_process_object.returncode==1:
    service = "sshd.service"

