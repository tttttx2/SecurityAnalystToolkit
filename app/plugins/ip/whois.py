import json
import whois

def run(ip):
    w = whois.whois(ip)
    response = {'raw':'raw text', 'pretty':'pretty text for gui'}
    response["pretty"]=w.text
    return json.dumps(response)
