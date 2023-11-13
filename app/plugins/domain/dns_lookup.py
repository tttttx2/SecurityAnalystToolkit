import json
import dns.resolver,dns.reversename


def run(domain):
    response = {'raw':'raw text', 'pretty':'pretty text for gui'}

    try:
        dns_MX = '\n  '.join([i.to_text() for i in dns.resolver.resolve(domain, "MX")])
    except:
        dns_MX = "ERROR: MX LOOKUP FAILED"

    try:
        dns_TXT = '\n  '.join([i.to_text() for i in dns.resolver.resolve(domain, "txt")])
    except:
        dns_TXT = "ERROR: TXT LOOKUP FAILED"

    try:
        dns_SPF = '\n  '.join([i.to_text() for i in dns.resolver.resolve(domain, "txt") if 'spf' in i.to_text().lower()])
    except:
        dns_SPF = "ERROR: SPF LOOKUP FAILED"


    try:
        dns_A = '\n  '.join([i.to_text() for i in dns.resolver.resolve(domain, "A")])
    except:
        dns_A = "ERROR: A LOOKUP FAILED"

    try:
        dns_AAAA = '\n  '.join([i.to_text() for i in dns.resolver.resolve(domain, "AAAA")])
    except:
        dns_AAAA = "ERROR: AAA LOOKUP FAILED"

    try:
        dns_DMARC = '\n  '.join([i.to_text() for i in dns.resolver.resolve("_dmarc.{}".format(domain), "txt")])
    except:
        dns_DMARC = "ERROR: DMARC LOOKUP FAILED"

    try:
        dns_DKIM = '\n  '.join([i.to_text() for i in dns.resolver.resolve("dkim._domainkey.{}".format(domain), "txt")])
    except:
        dns_DKIM = "ERROR: DKIM LOOKUP FAILED (pretty much expected to fail)"

    try:
        dns_SOA = '\n  '.join([i.to_text() for i in dns.resolver.resolve(domain, "SOA")])
    except:
        dns_SOA = "ERROR: SOA LOOKUP FAILED"


    response["pretty"]=""
    response["pretty"]+="A (ipv4) Records:\n  {}\n\n".format(dns_A)
    response["pretty"]+="AAA (ipv6) Records:\n  {}\n\n".format(dns_AAAA)
    response["pretty"]+="MX (mailserver) Records:\n  {}\n\n".format(dns_MX)
    response["pretty"]+="DMARC (mail security) Records:\n  {}\n\n".format(dns_DMARC)
    response["pretty"]+="DKIM (mail security) Records:\n  {}\n\n".format(dns_DKIM)
    response["pretty"]+="SPF (mail security) Records:\n  {}\n\n".format(dns_SPF)
    response["pretty"]+="TXT (diverse) Records:\n  {}\n\n".format(dns_TXT)
    response["pretty"]+="SOA (nameserver) Records:\n  {}\n\n".format(dns_SOA)


    return json.dumps(response)
