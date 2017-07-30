#!/usr/bin/env python
'''
Write a Python program that creates a list. One of the elements of the list
should be a dictionary with at least two keys. Write this list out to a file
using both YAML and JSON formats. The YAML file should be in the expanded form.
'''

import yaml
import json

def main():

    my_dict = {
        'ip_addr': '10.1.1.1',
        'platform': 'cisco_ios',
        'vendor': 'cisco',
        'model': '3800'
    }

    my_list = [
        "string",
        1,
        2,
        3,
        my_dict,
        "string2"
    ]

    with open('test.yml', "w") as f:
        f.write( yaml.dump(my_list, default_flow_style=False) )

    with open('test.json', "w") as f:
       json.dump(my_list, f) 



if __name__ == "__main__":
    main()

