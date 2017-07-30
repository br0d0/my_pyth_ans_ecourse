#!/usr/bin/env python
'''
Write a Python program that reads both the YAML file and the JSON file created
in exercise6 and pretty prints the data structure that is returned.
'''

import yaml
import json

from pprint import pprint



def output_format(my_list, my_str):

    print
    print '#' * 3
    print '#' * 3 + my_str
    print '#' * 3
    pprint(my_list)



def main():

    yaml_file = 'test.yml'
    json_file = 'test.json'

    with open(yaml_file) as f:
        yaml_list = yaml.load(f)

    with open(json_file) as f:
        json_list = json.load(f)

    output_format(yaml_list, ' YAML')
    output_format(json_list, ' JSON')
    print '\n'




if __name__ == "__main__":
    main()
