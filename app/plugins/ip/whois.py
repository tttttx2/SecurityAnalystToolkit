import json
import whois

def run(ip):
    w = whois.whois(ip)
    response = {'raw':'', 'pretty':''}
    response["pretty"]=w.text
    return json.dumps(response)
