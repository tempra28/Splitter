#!/usr/bin/python
# coding: utf-8

# $ ./make_bi-dic.py -f dic_file 
#  to make a bilingual dictionary; dic_file.json
# { "NP": "cat", "猫" 

import re, json, codecs, sys
import parser
reload(sys)
sys.setdefaultencoding("utf-8")

def read_json(file):
    f = codecs.open(file, 'r', 'utf-8')
    dic = json.load(f)
    f.close()
    return dic

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

def set_term2(options, term, split_line, lang):
    if lang == "e":
        full_word = split_line[4]
        dic_name  = options.w_efilename
    elif lang == "j":
        full_word = split_line[5]
        dic_name  = options.w_jfilename
    else:
        sys.stderr.write("!! No Language for the dictionary !!")
        sys.exit(2)
    term2 = re.sub("\[.*?\]", "", full_word).decode("utf-8")
    term2 = re.sub('"', "", term2)      # 省略語に対する全単語表示
    if term2 == "":
        term2 = term
    return term2, dic_name

def make_dic(options, lang = "e"):
    dic = {}
    prog  = re.compile("\|.*\|") # Match the Longest
    prog2 = re.compile("\|") 
    prog3 = re.compile("\.UTF8")

    if lang == "e":
        f  = open(options.e_dic, 'r')
    elif lang == "j":
        f  = open(options.j_dic, 'r')

    for line in f:
        split_line = line.split("\t")
        a  = prog.search(line)        # re.search searches from everywhere

        if a: # Find matched pattern
            term  = re.sub("\[.*?\]", "", split_line[1]).decode("utf-8")
            term  = re.sub('"', "", term)
            term2, dic_name = set_term2(options, term, split_line, lang)
            pos = split_line[2] # 品詞
            term_lst = []       # value_lst

            text = prog2.split(a.group(0)) 
            num = len(text) / 2
            for i in range(num):
                text_term = re.sub('"', "", text[2*i + 1]).decode("utf-8")
                term_lst.append(text_term)
            for p in pos.split(";"):
                if term == term2:
                    add_into_dic(p, dic, term, term_lst, text_term)
                else:
                    add_into_dic(p, dic, term,  term_lst, text_term)
                    add_into_dic(p, dic, term2, term_lst, text_term)
    write_json(dic_name, dic)
    f.close()

def set_noun_dic(options, lang):
    if lang == "e":
        return ["EN1", "EN2", "EN3", "EN4", "EN5"], options.e_filename
               # 名詞, 固有名詞、基数詞、序数詞、助数詞(全て名詞区分)
    elif lang == "j":
        return ["JN1", "JN2", "JN3", "JN4", "JN7"], options.j_filename
               # 普通名詞, 固有名詞、数詞、時詞、形式名詞(全て名詞区分)        
    else:
        sys.stderr.write("!! No Language for the dictionary !!")
        sys.exit(2)

def make_noun_dic(options, lang = "e"):
    noun_dic = {}
    noun_lst, filename = set_noun_dic(options, lang)
    if lang == "e":
        dic = read_json(options.w_efilename)
    elif lang == "j":
        dic = read_json(options.w_jfilename)

    for noun in noun_lst:
        try:
            n_dic = dic[noun]
            for term in n_dic.keys():
                try:
                     noun_dic[term].append(noun)
                except KeyError: # 単語が未登録
                    noun_dic[term] = [noun]
        except KeyError:
            pass
    write_json(filename, noun_dic)

def main():
    ## Option parameter setting
    (options, args) = parser.parser_set()
    make_dic(options, "j")
    make_dic(options, "e")
    make_noun_dic(options, "j")
    make_noun_dic(options, "e")


if __name__ == "__main__":
    
    main()
