#!/usr/bin/python
# coding: utf-8

import subprocess as sp
import optparse

def parser_set():
    parser = optparse.OptionParser()
    parser.add_option("-f", dest = "filename", help = "read_filename")
    parser.add_option("-w", dest = "w_filename", help = "write_filename")
    return parser.parse_args()

def read_write_file(filename, w_filename):
    f = open(filename, 'r')
    f2 = open(w_filename, 'w')
    for line in f:
        p1 = sp.Popen(["echo", line], stdout = sp.PIPE)
        p2 = sp.Popen(["mecab", "-Owakati", "-b", "81920"], stdin = p1.stdout, stdout = sp.PIPE) # '-b size' buff_size (default 8192)
        # p2 = sp.Popen(["/nfs/dlocal/mecab/mecab-0.996/bin/mecab", "-Owakati", "-b", "81920"], stdin = p1.stdout, stdout = sp.PIPE) # '-b size' buff_size (default 8192)
        p1.stdout.close()
        output = p2.communicate()[0]
        p2.stdout.close()
        f2.write(output.rstrip() + "\n") # 文末の"\n"を削除
    f.close()
    f2.close()
    
def main():
    ## Option parameter setting
    (options, args) = parser_set()
    read_write_file(options.filename, options.w_filename)

if __name__ == "__main__":
    main()

