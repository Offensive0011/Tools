import os, sys
from platform import system
os.system('cls')

print('''
    [1] GRAB IPS BY DOMAINS

    [2] GRAB IPS USING API 
''')
choice = raw_input('\t[>] Choose Number - > ')

if choice == '1':
        if system() == 'Linux':
            os.system("cd IP_Grabbing/domain_to_ip && chmod +x domain_to_ip.py && python domain_to_ip.py")
        elif system() == 'Windows':
            os.system('cd IP_Grabbing/domain_to_ip && domain_to_ip.py')
        else:
            print('Unknown error :(')

elif choice == '2':
        if system() == 'Linux':
            os.system("cd IP_Grabbing/grabbing_by_api && chmod +x Api.py && python Api.py")
        elif system() == 'Windows':
            os.system('cd IP_Grabbing/grabbing_by_api && Api.py')
        else:
            print('Unknown error :(')