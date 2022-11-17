#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...}
   using the dict.get() method"""

def main():
    switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

    print(switch)

    print(type(switch))

    print(switch['hostname'])
    print(switch['ip'])

    print( 'First test - .get()') 
    print(switch.get('lynx', 'not real'))
    print(switch.get('version'))
    
    print('fourth test -.keys()')
    print(switch.keys())

    print('fifth test -.values()')
    print(switch.values())



if __name__ == '__main__':
    main()


