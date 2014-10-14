#!/usr/bin/python
# coding: utf-8

import re
import parser

def read_write_file(filename):
    f  = open(filename, 'r')
    f2 = open("ese_" + filename, 'w')
    f3 = open("esj_" + filename, 'w')
    prog  = re.compile("<E>.*</E>") # Match the Longest
    prog2 = re.compile("<J>.*</J>") # Match the Longest
    tag   = re.compile("<.*?>")
    for line in f:
        a  = prog.match(line)
        a2 = prog2.match(line)
        if a != None:
            sen = tag.sub("", line) # replace tag with ""
            f2.write(sen)
        elif a2 != None:
            sen = tag.sub("", line) # replace tag with ""
            f3.write(sen)
        else:
            pass
    f.close()
    f2.close()
    f3.close()

def main():
    ## Option parameter setting
    (options, args) = parser.parser_set()
    read_write_file(options.filename)

if __name__ == "__main__":
    
    main()
