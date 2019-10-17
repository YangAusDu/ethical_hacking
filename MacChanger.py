import subprocess
import re
import sys
import optparse

def changeMac(interface, new_mac_addr):
    print('[+]Changing Mac address for '+ interface + 'to' + new_mac_addr)
    print('...')
    subprocess.call(['ifconfig', str(interface), 'down'])
    subprocess.call(['ifconfig', str(interface), 'hw', 'ether', new_mac_addr])
    subprocess.call(['ifconfig', str(interface), 'up'])
    subprocess.call('ifconfig', shell = True)

def get_arg():
    parse = optparse.OptionParser()
    parse.add_option('-i','--interface', dest = 'interface', help = "interface to change its MAC address")
    parse.add_option('-m','--mac', dest = 'new_mac', help = "new mac address")
    (opts, args) = parse.parse_args()
    if not opts.interface:
        parse.error('interface incorrect')
    elif not opts.new_mac:
        parse.error('wrong mac address')
    else:
        return opts

def getCurrentMac(interface):
    result = subprocess.check_output(['ifconfig',interface])
    print(result)
    #return
    mac_addr = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))
    if mac_addr:
        return mac_addr.group(0)
    else:
        print('[-]Sorry mac address not found!')

opts = get_arg()
current_mac_address = getCurrentMac(opts.interface)
print('[+] Your current address =: '+ str(current_mac_address))
changeMac(opts.interface, opts.new_mac) 
current_mac_address = getCurrentMac(opts.interface)
if current_mac_address == opts.new_mac:
    print('[+] mac address being changed sucessfully')
else:
    print('[-]Failure')