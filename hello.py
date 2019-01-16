#!/usr/bin/python3

import sys

def get_name():
    name = str(raw_input("Hello. What is your name? "))
    print("Hello {}".format(name))

if __name__ == '__main__':
    get_name()
