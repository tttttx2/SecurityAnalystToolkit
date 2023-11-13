import json


def run(ip):
    response = {'raw':'raw text', 'pretty':'pretty text for gui'}
    response["pretty"]+=" from reverse_dns"
    return json.dumps(response)
