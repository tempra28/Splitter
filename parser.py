#!/usr/bin/python
# coding: utf-8

import optparse

def parser_set():
    parser = optparse.OptionParser()
    parser.add_option("-f", dest = "filename", default = "TEST/trans_dic.json", help = "translated resutlt pairs")
    parser.add_option("-r", dest = "r_filename", default = "TEST/recall.json", help = "recall filename")
    parser.add_option("-a", dest = "a_filename", default = "TEST/EJB_tr_dic.json", help = "answer_filename")
    parser.add_option("-c", dest = "c_filename", default = "TEST/corpus_jndic.json", help = "Corpus's noun dictionary filename")
    parser.add_option("--fe", dest = "e_dic", default = "TEST/EJB.DIC.UTF8.100", help = "read_edictionaryname")
    parser.add_option("--fj", dest = "j_dic", default = "TEST/JEB.DIC.UTF8.100", help = "read_j_dictionaryname")
    parser.add_option("--we", dest = "w_efilename", default = "TEST/EJB.DIC.100.json", help = "write_efilename")
    parser.add_option("--wj", dest = "w_jfilename", default = "TEST/JEB.DIC.100.json", help = "write_efilename")
    parser.add_option("--ne", dest = "e_filename", default = "TEST/EJB.enoun_dic.json", help = "write_enoun_dic_filename")
    parser.add_option("--nj", dest = "j_filename", default = "TEST/JEB.jnoun_dic.json", help = "write_jnoun_dic_filename")
    parser.add_option("--te", dest = "tr_efilename", default = "TEST/EJB.tr_dic.json", help = "write_tr_dic_filename")
    parser.add_option("--tj", dest = "tr_jfilename", default = "TEST/JEB.tr_dic.json", help = "write_tr_dic_filename")

    return parser.parse_args()

def main():
    ## Option parameter setting
    (options, args) = parser_set()

if __name__ == "__main__":
    
    main()
