#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# See "docs/journald_fetcher.md" for explanations (comments)

import subprocess                                                                     #1.1


def fetch_journal_logs(*target_source,since=None,until=None):                                        #a.1
    log_results = []
    for source in target_source:                                                                 #b.1
        cmd_list = ["journalctl"]    

        cmd_list.append(source)                                                               #a.2

        if since and until :
            temp = ["--since",since,"--until",until]
            cmd_list.extend(temp)
        elif since:
            temp = ["--since",since]
            cmd_list.extend(temp)
        elif until:
            temp = ["--until",until]
            cmd_list.extend(temp)

        CPObject = subprocess.run(cmd_list,capture_output=True,text=True)                    #a.3

        if CPObject.returncode == 0:                                                   #a.4
            log_results.append(CPObject.stdout)                                          #b.2

        else:
            log_results.append("Error: "+CPObject.stderr)

    return log_results



