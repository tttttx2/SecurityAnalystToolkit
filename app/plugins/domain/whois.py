import json
import whois

def run(domain):
    w = whois.whois(domain)
    response = {'raw':'', 'pretty':''}
    response["pretty"]=w.text
    return json.dumps(response)
