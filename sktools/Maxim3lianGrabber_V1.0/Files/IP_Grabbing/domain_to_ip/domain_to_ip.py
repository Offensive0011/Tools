#!/usr/bin/env python2
# Modified by: Noir_Tempest_001

import socket
import os


os.system('cls' if os.name == 'nt' else 'clear')

# function to get IP from a domain
def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print('IP - > ' + ip)
        with open('../../../IPs.txt', 'a') as f:
            f.write(ip + '\n')
    except Exception as e:
        print('Useless - > ' + domain + '. Error: ' + str(e))

# Get list of domains from user
try:
    domain_list_path = '../../../' + input('\t[>] Domain List: ')
    with open(domain_list_path, 'r') as file:
        domain_list = file.read().splitlines()
    for domain in domain_list:
        get_ip(domain)
except Exception as e:
    print('Failed to process domain list. Error: ' + str(e))