# modules/dns_lookup.py

import dns.resolver

def get_dns_records(domain):
    records = {}
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            records[rtype] = [str(rdata) for rdata in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            records[rtype] = []
        except Exception as e:
            records[rtype] = [f"Error: {e}"]

    result = ""
    for rtype, values in records.items():
        result += f"{rtype} Records:\n"
        if values:
            result += "\n".join(values)
        else:
            result += "None found."
        result += "\n\n"

    return result
