#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# See "docs/journald_fetcher.md" for explanations (comments)

import subprocess                                                                                #a.1


def fetch_journal_logs(*target_source,since=None,until=None):                                    #b.1
    log_results = []
    for source in target_source:                                                                 #b.2
        cmd_list = ["journalctl"]    

        cmd_list.append(source)                                                                  #b.3

        if since and until :
            temp = ["--since",since,"--until",until]
            cmd_list.extend(temp)                                                                #b.3
        elif since:
            temp = ["--since",since]
            cmd_list.extend(temp)
        elif until:
            temp = ["--until",until]
            cmd_list.extend(temp)

        CPObject = subprocess.run(cmd_list,capture_output=True,text=True)                        #b.4

        if CPObject.returncode == 0:                                                             #b.4 #b.5
            log_results.append(CPObject.stdout)                                                  #b.6

        else:
            log_results.append("Error: "+CPObject.stderr)                                        #b.7

    return log_results



