import whois

def get_whois_info(domain):
    try:
        w = whois.whois(domain)

        result = ""
        result += f"Domain Name: {w.domain_name}\n"
        result += f"Registrar: {w.registrar}\n"
        result += f"Creation Date: {w.creation_date}\n"
        result += f"Expiration Date: {w.expiration_date}\n"
        result += f"Name Servers: {w.name_servers}\n"
        result += f"Emails: {w.emails}\n"

        return result

    except Exception as e:
        return f"WHOIS lookup failed: {e}"

