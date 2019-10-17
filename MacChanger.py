import subprocess
import re
import sys
import optparse

parse = optparse.OptionParser()
parse.add_option('-i','--interface', dest = 'interface', help = "interface to change its MAC address")
parse.parse_args()

interface = input('Change mac address for: ')
new_mac_addr = input('type your new mac address: ')
print(new_mac_addr)

#subprocess.call('ifconfig '+ str(interface) + ' down', shell = True)
#subprocess.call('ifconfig '+str(interface)+ ' hw ether 01:5d:6c:e8:8d:b2', shell = True)
#subprocess.call('ifconfig '+ str(interface) + ' up', shell = True)
#subprocess.call('ifconfig', shell = True)

subprocess.call(['ifconfig', str(interface), 'down'])
subprocess.call(['ifconfig', str(interface), 'hw', 'ether', new_mac_addr])
subprocess.call(['ifconfig', str(interface), 'up'])
subprocess.call('ifconfig', shell = True)

