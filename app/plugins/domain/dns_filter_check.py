import json
import dns.resolver

res_local = dns.resolver.Resolver()

res_google = dns.resolver.Resolver()
res_google.nameservers = ['8.8.8.8']

res_cloudflare = dns.resolver.Resolver()
res_cloudflare.nameservers = ['8.8.8.8']

res_cloudflare_family = dns.resolver.Resolver()
res_cloudflare_family.nameservers = ['1.1.1.2']


def run(domain):
    response = {'raw':'', 'pretty':''}

    try:
        dns_local = '\n  '.join([i.to_text() for i in res_local.resolve(domain, "A")])
    except:
        dns_local = "ERROR: No connection to SYSTEM DNS"

    try:
        dns_google = '\n  '.join([i.to_text() for i in res_google.resolve(domain, "A")])
    except:
        dns_google = "ERROR: No connection to Google DNS"

    try:
        dns_cloudflare = '\n  '.join([i.to_text() for i in res_cloudflare.resolve(domain, "A")])
    except:
        dns_cloudflare = "ERROR: No connection to CloudFlare"

    try:
        dns_cloudflare_family = '\n  '.join([i.to_text() for i in res_cloudflare_family.resolve(domain, "A")])
    except:
        dns_cloudflare_family = "ERROR: No connection to CloudFlare (Family)"




    response["pretty"]+="A Record (System DNS):\n  {}\n\n".format("BLOCKED" if '0.0.0.0' in dns_local else dns_local)
    response["pretty"]+="A Record (Google):\n  {}\n\n".format("BLOCKED" if '0.0.0.0' in dns_google else dns_google)
    response["pretty"]+="A Record (CloudFlare):\n  {}\n\n".format("BLOCKED" if '0.0.0.0' in dns_cloudflare else dns_cloudflare)
    response["pretty"]+="A Record (CloudFlare Family):\n  {}\n\n".format("BLOCKED" if '0.0.0.0' in dns_cloudflare_family else dns_cloudflare_family)


    return json.dumps(response)
