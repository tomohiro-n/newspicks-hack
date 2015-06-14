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
import re
import csv

center_com = "わらべや日洋"

def run():
    companyfile = "c_names.pickle"
    tweetcsv = "allTweetWarabeya.csv"
    companies = getCompanies(companyfile)
    center_idx = companies.index(center_com)
    print "center_idx:%d"%(center_idx)
    comratedic = makeRateList(companies, tweetcsv, center_idx)
    print comratedic

    outDic = {}
    outDic["company"] = center_com
    outDic["trading"] = comratedic

def makeRateList(companies, tweetcsv, center_idx):
    countlist = [0]*len(companies)
    f = open(tweetcsv, 'r')
    reader = csv.reader(f)
    for row in reader:
        tweet = row[4]
        for i, com in enumerate(companies):
            if i == center_idx:
                continue
            ptn = re.compile(com)
            if ptn.search(tweet):
                countlist[i] += 1
    f.close()

    sum_c = float(sum(countlist))
    print "sum_c:%s"%(str(sum_c))
    rates = []
    for c in countlist:
        rates.append(c/sum_c)

    comratedic = {}
    for i,com in enumerate(companies):
        a_rate = rates[i]
        if a_rate > 0:
            comratedic[com] = a_rate

    return comratedic

def getCompanies(companyfile):
    f = open(companyfile, 'r')
    companies = pickle.load(f)
    f.close()
    return companies

if __name__ == "__main__":
    run()
