# 🔎 Automated Reconnaissance Toolkit

## 📌 Overview
This project is a modular Python-based reconnaissance toolkit designed to automate OSINT data collection. It supports multiple recon functions such as DNS lookup, WHOIS queries, subdomain enumeration, Shodan scanning, SSL cert scraping, and social/email discovery via theHarvester.

It outputs structured reports in both `.txt` and `.json` formats for easy reference and integration.

---

## 🚀 Features

- ✅ DNS Record Lookup (A, MX, TXT, etc.)
- ✅ WHOIS Information (for domains only)
- ✅ Shodan Scan for IPs (requires API key)
- ✅ SSL Certificate Lookup via crt.sh
- ✅ Subdomain Enumeration via RapidDNS
- ✅ Email & Social Discovery via theHarvester
- ✅ Exports TXT and JSON reports to `/reports/` folder

---

## 🛠 Requirements

- Python 3.11+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
