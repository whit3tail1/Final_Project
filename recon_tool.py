import argparse
import os
import json
from datetime import datetime
from modules import dns_lookup, shodan_scan, whois_lookup, ssl_scraper, subdomain_enum, email_harvester

# Create reports directory if it doesn't exist
if not os.path.exists("reports"):
    os.makedirs("reports")

def save_report(domain, data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    txt_file = f"reports/{domain}_{timestamp}.txt"
    json_file = f"reports/{domain}_{timestamp}.json"

    # Save as TXT
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(f"Recon Report for {domain}\n\n")
        for key, value in data.items():
            f.write(f"--- {key} ---\n{value}\n\n")

    # Save as JSON
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"\nReports saved as:\n  {txt_file}\n  {json_file}")

def main():
    parser = argparse.ArgumentParser(description="Automated Reconnaissance Tool")
    parser.add_argument("target", help="Domain or IP to scan")
    args = parser.parse_args()

    domain = args.target
    print(f"[+] Starting reconnaissance on: {domain}")

    #Load API keys
    with open("config/keys.json") as f:
        keys = json.load(f)
    shodan_key = keys["shodan_api_key"]

    report_data = {
        "Domain": domain,
        "Subdomains": subdomain_enum.enumerate_subdomains(domain),
        "DNS Records": dns_lookup.get_dns_records(domain),
        "WHOIS": whois_lookup.get_whois_info(domain),
        "Open Ports (Shodan)": shodan_scan.scan_shodan(domain, shodan_key),
        "Emails & Social": email_harvester.harvest_emails(domain),
        "SSL Cert Info": ssl_scraper.get_ssl_info(domain),
    }

    # Future modules will update report_data here, passing shodan_key as needed

    save_report(domain, report_data)

if __name__ == "__main__":
    main()
