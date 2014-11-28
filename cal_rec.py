#!/usr/bin/python
# coding: utf-8

# ./cal_rec.py -f filename -a answer
# get the recall value

import json, sys
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

def get_recall(options):
    rec_dic = {} # {term: recall}
    tp, fn, count = 0. , 0., 0.

    term_dic = read_json(options.filename)
    ans_dic  = read_json(options.filename)

    # precision = tp / tp + fp
    # recall    = tp / tp + fn
    for term, tm_lst in term_dic.iteritems():
        recall = 0.
        a_lst = ans_dic[term]
        while tm_lst != []: # find it in a dic
            # print tm_lst
            cand_tm = tm_lst.pop() # ans_term
            if cand_tm in a_lst:
                tp += 1.
                a_lst.remove(cand_tm) # a_lst shrinks
        fn = len(a_lst) # TODO: 正解の残り?, 多分、対象単語(all_word)でとれてきていない単語数(all_word-a_lst)にしないとだめ
        try:
            recall = tp / (tp + fn)
        except ZeroDivisionError:
            sys.stderr.write("!! devided by Zero (%s) !!", term)
            recall = 0
        rec_dic[term] = recall # rec_dic = {term: recall} 追加
        count += recall
    write_json(options.r_filename, rec_dic)

    avr_recall = count / len(rec_dic) # recall平均値
    print avr_r

def main():
    ## Option parameter setting
    (options, args) = parser.parser_set()
    get_recall(options)

if __name__ == "__main__":
    main()
