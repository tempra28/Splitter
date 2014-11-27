#!/usr/bin/python
# coding: utf-8

# $ ./make_bi-dic.py -f dic_file 
#  to make a bilingual dictionary; dic_file.json
# { "NP": "cat", "猫" 

import re, json, codecs
import parser

def write_json(file, dic):
    f = codecs.open(file, 'w', 'utf-8')
    json.dump(dic, f, indent = 2, ensure_ascii = False)
    f.close()    

def add_into_dic(pos, dic, term, term_lst, text_term):
    if pos in dic: # Find pos in dic
        if term in dic[pos]:
            dic[pos][term].extend(term_lst)
            dic[pos][term] = list(set(dic[pos][term])) # 重複削除
        else:
            dic[pos][term] = [text_term]
    else:
        dic[pos] = {}
        dic[pos][term] = [text_term]
    return dic

def set_term2(term, full_word):
    term2 = re.sub('"', "", full_word).decode("utf-8")      # 省略語に対する全単語表示
    if term2 == "":
        term2 = term
    return term2

def read_write_file(options):
    dic = {}
    prog  = re.compile("\|.*\|") # Match the Longest
    prog2 = re.compile("\|") 
    prog3 = re.compile("\.UTF8")

    f  = open(options.filename, 'r')

    for line in f:
        split_line = line.split("\t")
        a  = prog.search(line)        # re.search searches from everywhere

        if a: # Find matched pattern
            term  = re.sub("\[.*?\]", "", split_line[1]).decode("utf-8")
            term  = re.sub('"', "", term)
            term2 = set_term2(term, split_line[4])
            pos = split_line[2] # 品詞
            term_lst = []       # value_lst

            text = prog2.split(a.group(0)) 
            num = len(text) / 2
            for i in range(num):
                text_term = re.sub('"', "", text[2*i + 1]).decode("utf-8") ## 恐らく不要 20141127
                term_lst.append(text_term)
            if term == term2:
                add_into_dic(pos, dic, term, term_lst, text_term)
            else:
                add_into_dic(pos, dic, term,  term_lst, text_term)
                add_into_dic(pos, dic, term2, term_lst, text_term)
    write_json(options.w_filename, dic)
    f.close()

def main():
    ## Option parameter setting
    (options, args) = parser.parser_set()
    read_write_file(options)

if __name__ == "__main__":
    
    main()
