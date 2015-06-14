#!/usr/local/bin/python
# -*- coding: utf-8 -*-

'''
Created on Jun 13, 2015

上場企業名の取得

@author: ochi
'''

import os
import json
import pickle
import csv

def run():
    companyfile = "companies.json"
#    outfile = "c_names.pickle"
    outfile = "c_names.csv"
    f = open(companyfile, 'r')
    allDic = json.load(f)
    f.close()
#    print allDic.keys()
    objlist = allDic["hits"]["hits"]
    companies = []
    for obj in objlist:
        c_name =  obj["_source"]["company_name"]
        companies.append(c_name)

    print "len(companies):%d"%(len(companies))
    g = open(outfile, 'w')
    writer = csv.writer(g)
    for c_name in companies:
        writer.writerow([c_name])
#    pickle.dump(companies, g)
    g.close()
 


if __name__ == "__main__":
    run()
