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
import MeCab

center_coms = ["わらべや日洋","セブンイレブン"]
#center_coms = ["わらべや日洋"]
outfile = "data.json"


def run():
    companyfile = "c_names.csv"
    tweetcsvs = ["allTweetWarabeya.csv","allTweetSeven.csv"]
#    tweetcsvs = ["allTweetWarabeya.csv"]
    companies = getCompanies(companyfile)

    outDic = {}
    outDic["data"] = []
    for i,tweetcsv in enumerate(tweetcsvs):
#        if i+1 % 10 == 0:
#            print "count: %d"%(i+1)
        print "count: %d"%(i+1)
        center_com = center_coms[i]
        print center_com
        center_idx = companies.index(center_com)
        print "center_idx:%d"%(center_idx)
        formcomratedics,alltweets = makeRateList(companies, tweetcsv, center_idx)
#        print comratedic

        aDic = {}
        aDic["company"] = center_com
        aDic["trading"] = formcomratedics
        keywords = getKeywords(alltweets)
#        print "keywords"
#        print keywords
        aDic["keywords"] = keywords
        outDic["data"].append(aDic)

    #outfile
#    print outDic
    f = open(outfile, 'w')
#    json.dump(outDic,f,sort_keys=True,indent=4)
    text = json.dumps(outDic,sort_keys=True,ensure_ascii=False,indent=4)
    f.write(text.encode("utf-8"))
    f.close()

def getKeywords(alltweets):
    tagger = MeCab.Tagger("-Ochasen")
    ptn = re.compile("名詞-固有名詞")
    eptn = re.compile(r'^[0-9A-Za-z]+')
    namedentities = []
    print "getkeyword"
    for j, tweet in enumerate(alltweets):
#        print tweet
        if (j+1) % 1000 == 0:
            print j+1
        a = tagger.parse(tweet)
        ws = a.split('\t')
 
        for i,w in enumerate(ws):
            if ptn.search(w):
                new_w = ws[i-3].strip()
                if not eptn.match(new_w):
                    namedentities.append(new_w)
   
    keywords = countNEs(namedentities)

    return keywords

def countNEs(namedentities):
    vocab = sorted(list(set(namedentities)))
    vocabdic = {}
    for v in vocab:
        vocabdic[v] = 0
    for w in namedentities:
        vocabdic[w] += 1

    keywords = []
    for v in vocab:
        name = v
        size = vocabdic[v]
        adic = {}
        adic["name"] = name
        adic["size"] = size
        keywords.append(adic)
    return keywords

def makeRateList(companies, tweetcsv, center_idx):
    ptns = []
    for i, com in enumerate(companies):
        ptn = re.compile(com)
        ptns.append(ptn)

    countlist = [0]*len(companies)
    f = open(tweetcsv, 'r')
    reader = csv.reader(f)
    alltweets = []
    for j,row in enumerate(reader):
        if (j+1) % 1000 == 0:
            print j+1
        tweet = row[4]
        alltweets.append(tweet)
        for i, com in enumerate(companies):
 
            if i == center_idx:
                continue
#            ptn = re.compile(com)
            ptn = ptns[i]
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
            print com 
            print a_rate
            comratedic[com] = a_rate

    formcomratedics = []
    for akey in comratedic.keys():
        name = akey
        size = comratedic[name]
        adic = {}
        adic["name"] = name
        adic["size"] = size
        formcomratedics.append(adic)
    return formcomratedics, alltweets

def getCompanies(companyfile):
    f = open(companyfile, 'r')
    reader = csv.reader(f)
    companies = []
    for row in reader:
        companies.append(row[0])
#    companies = pickle.load(f)
    f.close()
    return companies

if __name__ == "__main__":
    run()
