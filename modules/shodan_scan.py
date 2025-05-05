import shodan

def scan_shodan(domain, api_key):
    try:
        api = shodan.Shodan(api_key)
        host = api.host(domain)

        result = f"IP: {host.get('ip_str')}\n"
        result += f"Organization: {host.get('org', 'N/A')}\n"
        result += f"Operating System: {host.get('os', 'N/A')}\n\n"
        result += "Open Ports and Services:\n"

        for item in host['data']:
            port = item.get('port')
            banner = item.get('data', '').strip().split('\n')[0]
            result += f"Port {port}: {banner}\n"

        return result

    except shodan.APIError as e:
        return f"Shodan API Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
