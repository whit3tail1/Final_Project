# 🔎 Automated Reconnaissance Toolkit

## 📌 Overview

This project is a modular Python-based reconnaissance toolkit built to automate OSINT (Open Source Intelligence) tasks. Designed for cybersecurity analysts and ethical hackers, the tool performs a variety of recon techniques including DNS record lookup, WHOIS information gathering, subdomain enumeration, Shodan scanning, SSL certificate analysis, and email/social profile discovery using theHarvester.

It outputs clean, time-stamped reports in both `.txt` and `.json` formats for easy review or integration with other security workflows.

---

## 🚀 Features

- ✅ DNS Record Lookup (A, MX, TXT, CNAME, NS)
- ✅ WHOIS Information (for domains only)
- ✅ Shodan Port/Banner Scan (for IP addresses; API required)
- ✅ SSL Certificate Discovery via crt.sh
- ✅ Subdomain Enumeration via RapidDNS
- ✅ Email & Social Profile Discovery using theHarvester
- ✅ Exports readable TXT and structured JSON reports to `/reports/`

---

## 🛠 Requirements

- Python 3.11 or higher
- Required Python libraries:
  ```bash
  pip install -r requirements.txt
Internet access for API and OSINT queries

🔐 API Keys
Shodan scanning requires an API key.

Create a file at config/keys.json:
{
  "shodan_api_key": "your_actual_key_here"
}
Do NOT upload this file to GitHub. It's excluded via .gitignore.

📥 Setting Up theHarvester (for Email/Social Recon)
theHarvester is not bundled with this repository to avoid submodule conflicts.

Follow these steps:
Clone it into your project root:
git clone https://github.com/laramies/theHarvester.git

Install its requirements:
pip install -r theHarvester/requirements/base.txt
The tool will automatically call theHarvester via subprocess.


💻 How to Run
python recon_tool.py example.com
Use domain names like google.com, microsoft.com for full recon

IP addresses like 8.8.8.8 trigger Shodan scan only (WHOIS is skipped)


📁 Output
All results are stored in the reports/ directory. Files are named using a timestamp format.

Example output:
reports/
├── google.com_20250504_203812.txt
└── google.com_20250504_203812.json
📷 Example Screenshots (Recommended for Report)
Add these manually if required for submission:

Terminal output after running the tool

The contents of a TXT report

/reports/ folder contents with timestamps


🙋 Author
Gilberto Cruz
National University
Course: CYB333 – Security Automation
May 2025


📜 License
For academic and ethical use only.
Do not use this tool for unauthorized or malicious activity.

