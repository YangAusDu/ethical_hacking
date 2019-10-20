import scapy.all as scapy
import re
import sys
import optparse

def get_arg():
    parse = optparse.OptionParser()    
    parse.add_option('-t','--target', dest = 'target', help = "range of your targeting ip")
    (opts, args) = parse.parse_args()
    if not opts.target:
        parse.error('target incorrect')
    else:
        return opts

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    #arp_request.show()
    broad_cast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    #broad_cast.show()
    arp_request_broad_cast = broad_cast/arp_request
    #arp_request_broad_cast.show()
    answered, unanswered = scapy.srp(arp_request_broad_cast, timeout = 1)
    print(answered.summary())
    
    client_list =[]
    for each in answered:
        client_dict = {'ip': each[1].psrc, 'mac': each[1].hwsrc}
        client_list.append(client_dict)
    return client_list
    
def printResult(client_list):
    print('IP\t\t\tMac Address----------------------------------')
    for client in client_list:
        print(client['ip']+'\t\t'+client['mac'])
    
def main():
    opts = get_arg()
    ip = opts.target
    client_list = scan(ip)
    printResult(client_list)

main()