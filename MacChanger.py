import subprocess
import re
import sys
import optparse

def changeMac(interface, new_mac_addr):
    print('Changing Mac address for '+ interface + 'to' + new_mac_addr)
    subprocess.call(['ifconfig', str(interface), 'down'])
    subprocess.call(['ifconfig', str(interface), 'hw', 'ether', new_mac_addr])
    subprocess.call(['ifconfig', str(interface), 'up'])
    subprocess.call('ifconfig', shell = True)


parse = optparse.OptionParser()
parse.add_option('-i','--interface', dest = 'interface', help = "interface to change its MAC address")
parse.add_option('-m','--mac', dest = 'new_mac', help = "new mac address")

(opts, args) = parse.parse_args()

changeMac(opts.interface, opts.new_mac) 