import requests
import re

def enumerate_subdomains(domain):
    try:
        url = f"https://rapiddns.io/subdomain/{domain}?full=1"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return f"Error fetching data: {response.status_code}"

        # Extract subdomains from the page using regex
        matches = re.findall(r'<td>([\w\.-]+\.' + re.escape(domain) + r')</td>', response.text)
        unique_subdomains = sorted(set(matches))

        if not unique_subdomains:
            return "No subdomains found."

        return "\n".join(unique_subdomains)

    except Exception as e:
        return f"Error during subdomain enumeration: {e}"
