#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# See "docs/journald_log_parser.md" for explanations (comments)

import subprocess                                                                     #1.1


def parse_static(*args,since=None,until=None):                                        #a.1
    result_li = []
    for flag in args:                                                                 #b.1
        li = ["journalctl"]    

        li.append(flag)                                                               #a.2

        if since and until :
            temp = ["--since",since,"--until",until]
            li.extend(temp)
        elif since:
            temp = ["--since",since]
            li.extend(temp)
        elif until:
            temp = ["--until",until]
            li.extend(temp)

        CPObject = subprocess.run(li,capture_output=True,text=True)                    #a.3

        if CPObject.returncode == 0:                                                   #a.4
            result_li.append(CPObject.stdout)                                          #b.2

        else:
            result_li.append("Error: "+CPObject.stderr)

    return result_li



