import subprocess
import re
import sys

interface = input('Change mac address for: ')
new_mac_addr = input('type your new mac address: ')
print(new_mac_addr)

subprocess.call('ifconfig '+ str(interface) + ' down', shell = True)
subprocess.call('ifconfig '+str(interface)+ ' hw ether 01:5d:6c:e8:8d:b2', shell = True)
subprocess.call('ifconfig '+ str(interface) + ' up', shell = True)
subprocess.call('ifconfig', shell = True)
