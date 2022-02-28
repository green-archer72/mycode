#!/usr/bin/env python3

import  netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try: #This is a new line, you also need to indent the code below this lin by 4 whitespaces
            print('MAC: ', end='') # this print statement will always print MAC without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # prints the MAC address
            print('IP: ', end='') # this print statement will always print IP without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['aadr']) # prints the IP address
        except:    # this is a new line
            print('Could not collect adapter information') # print an error message
