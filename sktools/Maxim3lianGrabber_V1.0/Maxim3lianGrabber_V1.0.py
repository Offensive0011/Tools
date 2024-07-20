import os, sys
from platform import system
try:
    raw_input = input
except NameError:
    pass

print('''

  __  __            _           _____ _ _             
 |  \/  | __ ___  _(_)_ __ ___ |___ /| (_) __ _ _ __  
 | |\/| |/ _` \ \/ / | '_ ` _ \  |_ \| | |/ _` | '_ \ 
 | |  | | (_| |>  <| | | | | | |___) | | | (_| | | | |
 |_|  |_|\__,_/_/\_\_|_| |_| |_|____/|_|_|\__,_|_| |_|
                                                      
      Modified By: Noir_Tempest_001

    [>] WEBSITES GRABBER V1.0 <FREE>


    [1] - IPS OPTIONS {
                        [ 1.1: GRAB IPS BY DOMAINS]
                        [ 1.2: GRAB IPS USING API ]
                                                    }
    [2] - REVERSE IPS {
                        [ GRAB DOMAINS FROM IPS ]
                                                    }

''')
choice = raw_input('\t[>] Choose Number - > ')

if choice == '1':
        if system() == 'Linux':
            os.system("cd Files && chmod +x sys.py && python sys.py")
        elif system() == 'Windows':
            os.system('cd Files && sys.py')
        else:
            print('Unknown error :(')

elif choice == '2':
        if system() == 'Linux':
            os.system("cd Files/reverse_IP_lookup && chmod +x reverse_IP_lookup.py && python reverse_IP_lookup.py")
        elif system() == 'Windows':
            os.system('cd Files/reverse_IP_lookup && reverse_IP_lookup.py')
        else:
            print('Unknown error :(')