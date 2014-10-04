#!/usr/bin/python
# coding: utf-8

import subprocess as sp
import parser


def read_write_file(filename):
    f = open(filename, 'r')
    f2 = open("wk_" + filename, 'w')
    for line in f:
        p1 = sp.Popen(["echo", line], stdout = sp.PIPE)
        p2 = sp.Popen(["mecab", "-Owakati", "-b", "81920"], stdin = p1.stdout, stdout = sp.PIPE) # '-b size' buff_size (default 8192)
        p1.stdout.close()
        output = p2.communicate()[0]
        p2.stdout.close()
        f2.write(output.rstrip() + "\n") # 文末の"\n"を削除
    f.close()
    f2.close()
    
def main():
    ## Option parameter setting
    (options, args) = parser.parser_set()
    read_write_file(options.filename)

if __name__ == "__main__":
    main()

