#!/usr/bin/python
# coding: utf-8

# $ ./make_bi-dic.py -f dic_file 
#  to make a bilingual dictionary; dic_file.json

import re,json
import parser

def read_write_file(filename):
    dic = {}
    prog  = re.compile("\|.*\|") # Match the Longest
    prog2 = re.compile("\|") 
    prog3 = re.compile("\.UTF8")

    f  = open(filename, 'r')
    w_filename = prog3.sub("", filename) + ".json"
    f2 = open(w_filename, 'w')

    for line in f:
        splitted_line = line.split("\t")
        a  = prog.search(line) # re.search searches from everywhere
        # a = prog.search(splittted_line[8])
        if a: # Find matched pattern
            term = re.sub("\[.*?\]", "", splitted_line[1]) #.decode("utf-8") ## 恐らく不要 20141127
            term = re.sub('"', "", term) #.decode("utf-8") ## 恐らく不要 20141127
            voca = {term:[]} # value: set

            text = prog2.split(a.group(0)) 
            num = len(text) / 2
            for i in range(num):
                text_term = re.sub('"', "", text[2*i + 1]) #.decode("utf-8") ## 恐らく不要 20141127
                voca[term].append(text_term)
            w_line = json.dumps(voca, sort_keys = True, ensure_ascii = False, indent = 2)
            f2.write(w_line)
    f.close()
    f2.close()

def main():
    ## Option parameter setting
    (options, args) = parser.parser_set()
    read_write_file(options.filename)

if __name__ == "__main__":
    
    main()
