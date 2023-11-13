import json
import dns.resolver,dns.reversename


def run(ip):
    response = {'raw':'raw text', 'pretty':'pretty text for gui'}

    try:
        reverse_dns = '  \n'.join([str(i) for i in dns.resolver.resolve(dns.reversename.from_address(ip), "PTR")])
    except:
        reverse_dns = "ERROR: LOOKUP FAILED"

    response["pretty"]="PTR Records:\n  {}".format(reverse_dns)
    return json.dumps(response)
