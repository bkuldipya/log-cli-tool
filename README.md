# Log Investigator CLI Tool

A command-line tool built in Python for investigating authentication logs, designed for **SOC Analysts** and **Threat Hunters**.  
Currently supports **SSH log analysis**, with **sudo log parsing** planned for future versions.

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
  - Save results to a file (JSON, text, etc.)

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
./main.py -h

# Parse a saved SSH log file
./main.py --mode file --path ssh_test.log

# Parse journald logs between time ranges
./main.py --mode journald-static --since "2025-08-23 14:40:00" --until "2025-08-23 15:00:00"

# Save output to a file
./main.py --mode file --path ssh_test.log --output extracted_iocs.json
```

---

## 📂 Project Structure  

```bash
log-investigator-cli/           # Repo root (GitHub Repo Name)
│
├── ligator/                    # Code directory (Python package) (all source code)
│   ├── main.py                 # CLI entry point 
│   ├── journald_fetcher.py  # Handles journald log fetching
│   ├── log_reader.py           # Reads and processes log data
│   ├── ioc_extractor.py        # Regex patterns to extract IOCs
│   └── output_handler.py       # Handles output (stdout, file, etc.)
│
├── docs/                       # Documentation
│   ├── main.md                 # Explanation of main.py and contains actual comments 
│   ├── journald_fetcher.md  # Explanation of journald_log_parser.py and contains actual comments
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
2. Sudo log parsing ⏳
3. Live journald streaming mode ⏳

---
 
 📌 Sample Extracted IOCs
 ```bash
{'service': 'sshd', 'username': 'admin', 'ip': '192.168.1.45', 'timestamp': 'Aug 23 14:42:11'}
{'service': 'sshd', 'username': 'root', 'ip': '203.0.113.55', 'timestamp': 'Aug 23 14:42:15'}
{'service': 'sshd', 'username': 'test', 'ip': '198.51.100.33', 'timestamp': 'Aug 23 14:42:25'}
```

---

## 👨‍💻 Author
**Bikash Kuldipya**  
Aspiring SOC Analyst & Threat Hunter, learning by building projects in Python and Linux to strengthen log analysis and investigation skills.


















