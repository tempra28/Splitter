#!/usr/bin/python
# coding: utf-8

import optparse

def parser_set():
    parser = optparse.OptionParser()
    parser.add_option("-f", dest = "filename", help = "read_filename")
    return parser.parse_args()

def main():
    ## Option parameter setting
    (options, args) = parser_set()

if __name__ == "__main__":
    
    main()
