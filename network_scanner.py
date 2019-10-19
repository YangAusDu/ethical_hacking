import scapy.all as scapy

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
    ip = "192.168.1.1/24"
    client_list = scan(ip)
    printResult(client_list)

main()