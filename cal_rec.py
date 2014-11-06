#!/usr/bin/python
# coding: utf-8

# ./cal_rec.py -f filename -a answer
# get the recall value

import parser
import json


def get_recall(filename, a_filename):
    f  = open(filename,   'r')
    f2 = open(a_filename, 'r')
    f3 = open("./recall.json", 'w')

    term_dic = json.load(f)
    ans_dic  = json.load(f2)
    f.close()
    f2.close()

    rec_dic = {} # {term: recall}
    tp, fn = 0. , 0.

    # precision = tp / tp + fp
    # recall    = tp / tp + fn
    for term, tm_lst in term_dic.iteritems():
        recall = 0.
        a_lst = ans_dic[term]
        while tm_lst != []: # find it in a dic
            # print tm_lst
            cand_tm = tm_lst.pop() # ans_term
            if cand_tm in a_lst:
                tp += 1
                a_lst.remove(cand_tm) # a_lst shrinks
        fn = len(a_lst) # TODO: 正解の残り?, 多分、対象単語(all_word)でとれてきていない単語数(all_word-a_lst)にしないとだめ
        recall = tp /tp + fn 
        rec_dic[term] = recall # rec_dic = {term: recall} 追加
    json.dump(rec_dic, f3, indent = 2)
    f3.close()

def main():
    ## Option parameter setting
    (options, args) = parser.parser_set()
    get_recall(options.filename, options.a_filename)

if __name__ == "__main__":
    
    main()
