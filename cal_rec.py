#!/usr/bin/python
# coding: utf-8

# ./cal_rec.py -f filename -a answer
# get the recall value

import json, sys, codecs, re
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

def set_ans(a_lst):
    for i in xrange(len(a_lst)):
        a_lst[i] = re.sub("\(.*\)", "", a_lst[i]) # 対象が日本語の場合
    return a_lst

def get_fn(filename, a_lst):
    num = 0.
    dic = read_json(filename)
    for ans in a_lst:
        try:
            dic[ans]
            num += 1.
        except KeyError:
            pass
    return num

def get_tp(cand_tm, a_lst):
    tp = 0.
    if cand_tm[1] in a_lst:
        tp += 1.
        a_lst.remove(cand_tm[1]) # a_lst shrinks
    return tp, a_lst

def get_recall(options):
    rec_dic = {} # {term: recall}
    fn, count = 0. , 0.

    term_dic = read_json(options.filename)
    ans_dic  = read_json(options.a_filename)

    # precision = tp / tp + fp
    # recall    = tp / tp + fn
    for term, tm_lst in term_dic.iteritems():
        recall = 0.
        a_lst = set_ans(ans_dic[term])
        while tm_lst != []: # find it in a dic
            cand_tm = tm_lst.pop() # ans_term
            tp, a_lst = get_tp(cand_tm, a_lst)
        fn = get_fn(options.c_filename, a_lst)
        # MEMO: 残された正解リストにある単語のうち、
        #       コーパスから作成した名詞辞書(corpus_noun_dic.json)の単語の数がfn
        try:
            recall = tp / (tp + fn)
        except ZeroDivisionError:
            sys.stderr.write("!! Recall devided by Zero (%s) !! \n" % term)
            recall = 0.
        rec_dic[term] = recall # rec_dic = {term: recall} 追加
        count += recall
    write_json(options.r_filename, rec_dic)
    avr_recall = count / len(rec_dic) # recall平均値
    print "** average recall: %f" % avr_recall

def main():
    ## Option parameter setting
    (options, args) = parser.parser_set()
    get_recall(options)

if __name__ == "__main__":
    main()
