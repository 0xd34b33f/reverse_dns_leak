from dns import reversename, resolver
import ipaddress
import sys


def name_finder(ip_inner):
    try:
        rev_name = reversename.from_address(str(ip_inner))
        reversed_dns = str(resolver.query(rev_name, 'PTR')[0])
        print(ip_inner, " ", reversed_dns)
    except:
        print(ip_inner, ' dead')


if __name__ == '__main__':
    resolver.default_resolver = resolver.Resolver(configure=False)
    if len(sys.argv) != 3:
        print('Usage: <nameserver ip> <ip-address/network_mask>')
    resolver.default_resolver.nameservers = [sys.argv[1]]
    resolver.timeout = 1
    resolver.lifetime = 1
    for ip in ipaddress.IPv4Network(sys.argv[2]):
        name_finder(ip)
