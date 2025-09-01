# Log Investigator CLI Tool

A Python CLI tool that parses SSH and Sudo authentication logs, extracts IOCs, and outputs results in multiple formats (text, text-compact, ndjson, ndjson-pretty)., designed for **SOC Analysts** and **Threat Hunters**.  
Currently supports **SSH and Sudo log analysis**.

---

## ✨ Features
- Extracts **Indicators of Compromise (IOCs)** such as:
  - Source IP addresses
  - Usernames
  - Timestamps
- Detects **failed SSH login attempts** and brute-force patterns.
- Supports multiple modes:
  - **File mode**: Parse saved log files.
  - **Journald (static)**: Analyze stored journald logs (`journalctl`).
  - **Journald (live)**: *(planned)* Stream logs in real time.
- Output options:
  - Print extracted IOCs to screen
  - Save results to a file 

---

## 📦 Installation
Clone the repo:
```bash
git clone https://github.com/bkuldipya/log-investigator-cli.git
cd log-investigator-cli/ligator
```

---

## 🚀 Usage

```bash
# General help
python3 main.py -h

# Parse a saved SSH log file
python3 main.py --mode file --path ssh_test.log

# Parse a saved SSH log file and save the output to a file
python3 main.py --mode file --path ssh_test.log --output extracted_iocs.json 

# Parse SSH journald logs between time ranges 
python3 main.py --mode journald-static --service ssh --since "2025-08-23 14:40:00" --until "2025-08-23 15:00:00"

# Parse SUDO journald logs between time ranges 
python3 main.py --mode journald-static --service sudo --since "2025-08-23 14:40:00" --until "2025-08-23 15:00:00"

# Pase SSH and SUDO journald logs and get the output in any format 
python3 main.py --mode journald-static --since "2025-08-23 14:40:00" --until "2025-08-23 15:00:00" --format ndjson
python3 main.py --mode journald-static --since "2025-08-23 14:40:00" --until "2025-08-23 15:00:00" --format ndjson-pretty
python3 main.py --mode journald-static --since "2025-08-23 14:40:00" --until "2025-08-23 15:00:00" --format text
python3 main.py --mode journald-static --since "2025-08-23 14:40:00" --until "2025-08-23 15:00:00" --format text-compact

# Save output to a file
python3 main.py --mode file --path ssh_test.log --output extracted_iocs.json
```

---

## 📂 Project Structure  

```bash
log-investigator-cli/           # Repo root (GitHub Repo Name)
│
├── ligator/                    # Code directory (Python package) (all source code)
│   ├── main.py                 # CLI entry point 
│   ├── journald_fetcher.py     # Handles journald log fetching
│   ├── log_reader.py           # Reads and processes log data
│   ├── ioc_extractor.py        # Regex patterns to extract IOCs
│   └── output_handler.py       # Handles output (stdout, file, etc.)
│
├── docs/                       # Documentation
│   ├── main.md                 # Explanation of main.py and contains actual comments 
│   ├── journald_fetcher.md     # Explanation of journald_fetcher.py and contains actual comments
│   ├── log_reader.md           # Explanation of log_reader.py and contains actual comments
│   ├── ioc_extractor.md        # Explanation of ioc_extractor.py and contains actual comments
│   └── output_handler.md       # Explanation of output_handler.py and contains actual comments
│
└── README.md


```

---

## 🛠️ Requirements

- Linux OS with **systemd** as the init system (required for journald modes).
- `journalctl` available in PATH.
- Python **3.8+**

---

## 🔮 Roadmap
1. SSH failed login IOC extraction ✅ 
2. Sudo log parsing ✅
3. Live journald streaming mode ⏳

---
 
 ## 📖 Usage Examples 

 🖥️ Example - 1  [ndjson format and sudo logs] (from the journald service logs)
```bash
python3 main.py --mode journald-static --service sudo --since "Aug 28 16:00:00" --until "Aug 28 16:13:00" --format ndjson    
```
 📌 Sample Output 
 ```bash
{"timestamp": "Aug 28 16:07:24", "hostname": "kali", "pid": "67851", "invoker": "pete", "failed_attempts": "1", "tty": "pts/1", "pwd": "/home/pete/Work/log-cli-tool/jupyter-files/Debugging", "target_user": "root", "command": "/usr/bin/apt", "lineno": 4}
{"timestamp": "Aug 28 16:10:11", "hostname": "kali", "pid": "69532", "invoker": "pete", "failed_attempts": "1", "tty": "pts/1", "pwd": "/home/pete/Work/log-cli-tool/jupyter-files/Debugging", "target_user": "root", "command": "/usr/bin/apt", "lineno": 8}
{"timestamp": "Aug 28 16:10:59", "hostname": "kali", "pid": "69978", "invoker": "pete", "failed_attempts": "2", "tty": "pts/1", "pwd": "/home/pete/Work/log-cli-tool/jupyter-files/Debugging", "target_user": "root", "command": "/usr/bin/apt", "lineno": 12}
{"timestamp": "Aug 28 16:12:24", "hostname": "kali", "pid": "70736", "invoker": "pete", "failed_attempts": "3", "tty": "pts/1", "pwd": "/home/pete/Work/log-cli-tool/jupyter-files/Debugging", "target_user": "root", "command": "/usr/bin/apt", "lineno": 14}
{"timestamp": "Aug 28 16:12:39", "hostname": "kali", "pid": "70883", "invoker": "pete", "failed_attempts": "3", "tty": "pts/1", "pwd": "/home/pete/Work/log-cli-tool/jupyter-files/Debugging", "target_user": "root", "command": "/usr/bin/apt", "lineno": 16}
```
<br>

 🖥️ Example - 2 [ndjson-pretty format and sudo logs] (from the journald service logs)
```bash
python3 main.py --mode journald-static --service sudo --since "Aug 28 16:00:00" --until "Aug 28 16:13:00" --format ndjson-pretty
```
📌 Sample Output (small snippet of actual output)
```bash
{
    "timestamp": "Aug 28 16:07:24",
    "hostname": "kali",
    "pid": "67851",
    "invoker": "pete",
    "failed_attempts": "1",
    "tty": "pts/1",
    "pwd": "/home/pete/Work/log-cli-tool/jupyter-files/Debugging",
    "target_user": "root",
    "command": "/usr/bin/apt",
    "lineno": 4
}
{
    "timestamp": "Aug 28 16:10:11",
    "hostname": "kali",
    "pid": "69532",
    "invoker": "pete",
    "failed_attempts": "1",
    "tty": "pts/1",
    "pwd": "/home/pete/Work/log-cli-tool/jupyter-files/Debugging",
    "target_user": "root",
    "command": "/usr/bin/apt",
    "lineno": 8
}
```
<br>

🖥️ Example - 3 [text format and ssh logs] (Filtering logs that are stored in file)
```bash
python3 main.py --mode file --path sshlog.txt --format text  
```
📌 Sample Output  (small snippet of the actual output)
```bash
Line No: 12
    timestamp: Aug 24 08:44:15
    log_source: sshd
    pid: 3227
    auth_status: Failed
    auth_methods: password
    username: root
    source_ip: 45.33.22.11
    port: 60012
Line No: 15
    timestamp: Aug 24 08:46:12
    log_source: sshd
    pid: 3238
    auth_status: Accepted
    auth_methods: publickey
    username: deploy
    source_ip: 198.51.100.12
    port: 51232
```
<br>

🖥️ Example - 4 [text-compact format and ssh logs] (Filtering logs that are stored in file)
```bash
python3 main.py --mode file --path sshlog.txt --format text-compact
```
📌 Sample Output
```bash
[1] timestamp=Aug 24 08:42:11|log_source=sshd|pid=3214|auth_status=Failed|auth_methods=password|username=admin|source_ip=203.0.113.45|port=50314|
[2] timestamp=Aug 24 08:42:14|log_source=sshd|pid=3214|auth_status=Failed|auth_methods=password|username=admin|source_ip=203.0.113.45|port=50314|
[3] timestamp=Aug 24 08:42:18|log_source=sshd|pid=3214|auth_status=Failed|auth_methods=password|username=root|source_ip=203.0.113.45|port=50314|
[4] timestamp=Aug 24 08:43:02|log_source=sshd|pid=3221|auth_status=Accepted|auth_methods=password|username=john|source_ip=192.168.1.101|port=42211|
[10] timestamp=Aug 24 08:44:12|log_source=sshd|pid=3227|auth_status=Failed|auth_methods=password|username=test|source_ip=45.33.22.11|port=60012|
[11] timestamp=Aug 24 08:44:14|log_source=sshd|pid=3227|auth_status=Failed|auth_methods=password|username=oracle|source_ip=45.33.22.11|port=60012|
[12] timestamp=Aug 24 08:44:15|log_source=sshd|pid=3227|auth_status=Failed|auth_methods=password|username=root|source_ip=45.33.22.11|port=60012|
[15] timestamp=Aug 24 08:46:12|log_source=sshd|pid=3238|auth_status=Accepted|auth_methods=publickey|username=deploy|source_ip=198.51.100.12|port=51232|
```
---

## 👨‍💻 Author
**Bikash Kuldipya**  
Aspiring SOC Analyst & Threat Hunter, learning by building projects in Python and Linux to strengthen log analysis and investigation skills.


















