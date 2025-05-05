import requests

def get_ssl_info(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return f"Error fetching data from crt.sh: Status code {response.status_code}"

        certs = response.json()

        seen = set()
        results = []

        for cert in certs:
            name = cert.get("common_name") or cert.get("name_value")
            if name and name not in seen:
                seen.add(name)
                results.append(name)

        if not results:
            return "No certificates found."

        return "\n".join(results)

    except Exception as e:
        return f"Error retrieving SSL certificate info: {e}"
