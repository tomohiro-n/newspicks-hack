#!/usr/local/bin/python
# -*- coding: utf-8 -*-

'''
Created on Nov 30, 2012

Search keywordsの更新

@author: user1
'''

import json
#import codecs
import datetime
import time
import urllib
import oauth2
import csv
from multiprocessing import Process
from threading import Thread

class TwitterKeywordCrawler():
            
    def __init__(self):
        self.twkeys = self.settwkeys()
        
        self.search_words = self.set_search_words()

#        self.save_files = self.get_file_names()
        
        self.clients = []
        for i in range(len(self.twkeys)):
            consumer = oauth2.Consumer(key=self.twkeys[i]["consumer_key"], secret=self.twkeys[i]["consumer_secret"])
            token = oauth2.Token(self.twkeys[i]["access_key"], self.twkeys[i]["access_secret"])
            client = oauth2.Client(consumer, token, timeout=20)
            self.clients.append(client)
        self.population = len(self.twkeys)
        
    def trans_tw_time_to_jpdtobj(self, tw_created_at):
        st = time.strptime(tw_created_at,'%a %b %d %H:%M:%S +0000 %Y')
        dt=datetime.datetime(st.tm_year,st.tm_mon,st.tm_mday,st.tm_hour,st.tm_min,st.tm_sec)
        jpdt = dt + datetime.timedelta(hours=9)
        return jpdt
    
    def trans_tw_time_to_jpdtdatestr(self, tw_created_at):
        jpdt = self.trans_tw_time_to_jpdtobj(tw_created_at)
        filedatestr = jpdt.strftime("%Y%m%d")
        return filedatestr
    
    def trans_tw_time_to_mysqldatetime_style(self, tw_created_at):
        jpdt = self.trans_tw_time_to_jpdtobj(tw_created_at)
        datetimestyle = jpdt.strftime("%Y-%m-%d %H:%M:%S")
        return datetimestyle
        
    def trans_unixsec_to_mysqldatetime_style(self, unixsec):
        dt=datetime.datetime.fromtimestamp(int(unixsec))
        datetimestyle = dt.strftime("%Y-%m-%d %H:%M:%S")
        return datetimestyle
        
    def get_file_names(self, tw_created_at, client_id):
#        fileheader = "../results/result_"
        filedatestr = self.trans_tw_time_to_jpdtdatestr(tw_created_at)

#        d = datetime.datetime.today()
#        filename = fileheader + filedatestr + "_" + str(client_id) + ".csv"
#        filename = "result.csv"
        filename = filedatestr
        return filename
        
        
    def settwkeys(self):
        consumer_key = "TMXMk9VUuRk8D4lOFZFeQ"
        consumer_secret = "l6lMxwN4XDxmQGdhZDNSLC5X98z31tnQkRLjcDvfMNg"
        
        twkeys = []
        
        twkeys0 = {
                        "screen_name":      "alife001",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "931101470-FkTVRx0j5X2bsQlAjfYh4nloX3dsmkPyZXHPnGol",
                        "access_secret":    "YjU7xP6YoCWUeaU4nGxNpi8il9OGlQEldfwEWUoQ"
                    }
        twkeys.append(twkeys0)
        
        twkeys1 = {
                        "screen_name":      "alife002",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "931104440-Lk9tu8p2kBnQPEAJLUzGDS4enrguQXaHzhQHfJa3",
                        "access_secret":    "63GfbEtYMrc5VCHTB8rey5FCCav67UArdMOVJN2c"
                    }
        twkeys.append(twkeys1)

        twkeys2 = {
                        "screen_name":      "alife003",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "951253765-Tsk7GTBNFWr3vcUgomj45q8Z6PGWcZp6yfgIhtDO",
                        "access_secret":    "75QV6e629WSOmdG9l5fdiwLXd773Z5oKjgYL0eQX9E"
                    }
        twkeys.append(twkeys2)

        twkeys3 = {
                        "screen_name":      "alife004",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "951295098-aq9RNT8yU6frLGJZ4moaaDzZ8Mp2WWuOCMGLCOHJ",
                        "access_secret":    "cbDuLKrLtrU0qasgalkqIJtafo4H2f3GVkO8qSXo0E"
                    }
        twkeys.append(twkeys3)
        
        twkeys4 = {
                        "screen_name":      "alife005",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "951296976-CzRYMrl1e0DqX4aOBBy2sebQXE2zNS7Bd52UhmBo",
                        "access_secret":    "qWyp790Zq87Ie6ewe9tkTiajPBs7PiFuSbsExJqrg"
                    }
        twkeys.append(twkeys4)

        twkeys5 = {
                        "screen_name":      "alife006",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "980241294-MN1wbUQIVpaN4qsj4smZtlWSE6Kna889s2COlErp",
                        "access_secret":    "VnSNrYVbk17iOUAxw1dC6p4tSe4AiwHwp0RoOOEwoyY"
                    }
        twkeys.append(twkeys5)

        twkeys6 = {
                        "screen_name":      "alife007007",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "980264930-7kmKsKKtCtdhSGpwM8fXMhQjYUOXdJ5tD4kLH1FP",
                        "access_secret":    "hHQMbBrgMLyY0QLZFs0chgGTklSQiU23kT8W28CbM"
                    }
        twkeys.append(twkeys6)

        twkeys7 = {
                        "screen_name":      "alife008",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "980259000-QLwM4wjlWoqGcfx0BrTQBnL8oV8xq7HPk0a9V3cC",
                        "access_secret":    "jCoARmaCdbogayPBkTsWoFJhu9f9CdWieDm1PcExnKI"
                    }
        twkeys.append(twkeys7)

        twkeys8 = {
                        "screen_name":      "alife0091",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "980278226-Pt31ecFLkXpTkjGvz9WrlCNiEVungPXb1QcB65jL",
                        "access_secret":    "oFZVbYDM45i7l2ZpXhebYlMHIFypb0pSr4oSbcx37CY"
                    }
        twkeys.append(twkeys8)

        twkeys9 = {
                        "screen_name":      "alife010",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "980271396-62yJU3V7Og0GwVd3vlvAQQxJlZbJudwDb9FBkgwX",
                        "access_secret":    "3XmJPxcB45mXRJPjXO31Xljh5AadzKnIEUq1YFTvw9Y"
                    }
        twkeys.append(twkeys9)

        twkeys10 = {
                        "screen_name":      "alife011",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "980275536-8EDJINN29pDxDqKGaXeQdpFn1KiWycWrAseKhoGr",
                        "access_secret":    "03ewA9gdXmGCN8NuVQ1k8LSUGXbgMZGcoebf4RkU"
                    }
        twkeys.append(twkeys10)

        twkeys11 = {
                        "screen_name":      "alife012",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "980294671-4FB3sPPOsQJ9xfrbc42tsuRSYMnlPC9pRggLE4",
                        "access_secret":    "h66ZNUJSoRvLvxDdEStKGEPNbJnLa8NNpudtojxHA"
                    }
        twkeys.append(twkeys11)

        twkeys12 = {
                        "screen_name":      "alife013",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "980292020-EMvZUpYJPhCCmysU0VU0lwPuARDuGclfwoAS2slc",
                        "access_secret":    "j5xKuxZduM722gi81Oi4z7YQ9UsUEUMuUOUnsC3D0"
                    }
        twkeys.append(twkeys12)

        twkeys13 = {
                        "screen_name":      "alife014",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "980440644-Ggzu8j5efFqRUZVw9OGwSy32PSEho03UhILInuzR",
                        "access_secret":    "iuAjWnK0WlQsY85a0xycrDrYtulRNBhvA0DVjyc"
                    }
        twkeys.append(twkeys13)

        twkeys14 = {
                        "screen_name":      "alife015",
                        "password":         "tj6769",
                        "consumer_key":     consumer_key,
                        "consumer_secret":  consumer_secret,
                        "access_key":       "980444766-ZxKvDxi0KN8KAJOARhKBqul0cPAR2utySLqv25Yh",
                        "access_secret":    "86T4nTVX5nAnmp52OG2YZCH20UiT1kl7havKR1ktk"
                    }
        twkeys.append(twkeys14)

        
        
        return twkeys
    
    def set_search_words(self):
        search_words = []
        for_client0 = [
                        "わらべや日洋"
                       ]

        for_client1 = [
                       ]
        for_client2 = [
                       ]
        for_client3 = [
                       ]
        for_client4 = [
                       ]
        for_client5 = [
                       ]
        for_client6 = [
                       ]
        for_client7 = [
                       ]
        for_client8 = [
                       ]
        for_client9 = [
                       ]
        for_client10 = [
                        ]
        for_client11 = [
                        ]
        for_client12 = [
                        ]
        for_client13 = [
                        ]
        for_client14 = [
#                        "わらべや日洋", "セブンイレブン", "セブンアイ", "セブン&アイ・ホールディングス"
                        "わらべや日洋", "セブンイレブン", "セブンアイ"
                        ]

        search_words.append(for_client0)
        search_words.append(for_client1)
        search_words.append(for_client2)
        search_words.append(for_client3)
        search_words.append(for_client4)
        search_words.append(for_client5)
        search_words.append(for_client6)
        search_words.append(for_client7)
        search_words.append(for_client8)
        search_words.append(for_client9)
        search_words.append(for_client10)
        search_words.append(for_client11)
        search_words.append(for_client12)
        search_words.append(for_client13)
        search_words.append(for_client14)
        
        return search_words
    
    def search_keyword(self, client_id, remaining, reset_time, since_tw_id, keywords):
        client = self.clients[client_id]
        qstring = "+OR+".join(keywords)
#        print len(qstring)
#        print qstring
        uri = "https://api.twitter.com/1.1/search/tweets.json"
        param_str = "?" + "q=" + qstring + "&lang=" + "ja" + "&result_type=" + "recent" + "&count=" + "100"
#        param_str = "?" + "q=" + qstring + "&lang=" + "ja" + "&result_type=" + "mixed" + "&count=" + "100"

#        res_tuple = self.get_virtual_res("990")
        try:
            res_tuple = client.request(uri+param_str, "GET")
            content_dic = json.loads(res_tuple[1])
        except Exception as e:
            print '=== エラー内容(Exception Error!!) ==='
            print 'type:' + str(type(e))
            print 'args:' + str(e.args)
            print 'message:' + e.message
            print 'e自身:' + str(e)
            res_tuple = self.get_virtual_res("992")
            content_dic = json.loads(res_tuple[1])

#        res_tuple = client.request(uri+param_str, "GET")

#        content_dic = json.loads(res_tuple[1])
        
        if str(res_tuple[0]["status"]) == "200":
#            print status_dic
            tw_ids = self.write_tweet_to_csv(content_dic, client_id)
            if len(tw_ids) > 0:
                min_tw_id = min(tw_ids)
            
                if "x-rate-limit-remaining" in res_tuple[0].keys():
                    remaining = int(res_tuple[0]["x-rate-limit-remaining"])
                else:
                    remaining -= 1
#                print search_api_rate_remaining
                if "x-rate-limit-reset" in res_tuple[0].keys():
                    reset_time = int(res_tuple[0]["x-rate-limit-reset"])
            
                num_tw_ids = len(tw_ids)
                max_tw_id = min_tw_id # search upper bount id
                while( num_tw_ids > 0 and max_tw_id > since_tw_id):
                    if remaining > 0:
#                        pass
#                        res_tuple = None
                        max_tw_id, num_tw_ids, remaining = self.get_next_results_search_api(
                                                                                            client_id   = client_id, 
                                                                                            max_tw_id   = max_tw_id, 
                                                                                            since_tw_id = since_tw_id, 
                                                                                            remaining   = remaining, 
                                                                                            reset_time  = reset_time, 
                                                                                            keywords    = keywords
                                                                                            )
#                        max_tw_id, num_tw_ids, remaining = self.get_next_results_search_api(client_id=client_id, max_tw_id=max_tw_id, since_tw_id=269454761911271425, remaining=remaining, reset_time=reset_time, keywords=keywords)
#                        self.get_next_results_search_api(client_id=client_id, max_tw_id=min_tw_id, since_tw_id=269454761900000000, content_dic=content_dic, remaining=remaining, reset_time=reset_time, keywords=keywords)
                    else:
                        now_time = int(time.time())
                        wait_sec = reset_time - now_time
                        if wait_sec < 0:
                            wait_sec = 0
                        reset_datetime = self.trans_unixsec_to_mysqldatetime_style(reset_time+2)
                        print "Client ID " + str(client_id) + ": " + "api limit expired, wait " + str(wait_sec) + " second. start at " + reset_datetime
                        time.sleep(wait_sec + 2)
                        remaining, reset_time = self.get_search_api_rate_remaining(client_id)
#                        res_tuple = None
                next_since_tw_id = max(tw_ids)
                return next_since_tw_id
            else:
                return since_tw_id
        else:
            return since_tw_id

    def get_next_results_search_api(self, client_id, max_tw_id, since_tw_id, remaining, reset_time, keywords):
        client = self.clients[client_id]
        qstring = " OR ".join(keywords)

        uri = "https://api.twitter.com/1.1/search/tweets.json"
        param_str = "?" + "q=" + qstring + "&max_id=" + str(int(max_tw_id) - 1) + "&since_id=" + str(int(since_tw_id) + 1) + "&lang=" + "ja" + "&result_type=" + "recent" + "&count=" + "100"
#        param_str = "?" + "q=" + qstring + "&max_id=" + str(int(max_tw_id) - 1) + "&since_id=" + str(int(since_tw_id) + 1) + "&lang=" + "ja" + "&result_type=" + "mixed" + "&count=" + "100"

#        res_tuple = self.get_virtual_res("990")
        try:
            res_tuple = client.request(uri+param_str, "GET")
            content_dic = json.loads(res_tuple[1])
        except Exception as e:
            print '=== エラー内容(Exception Error!!) ==='
            print 'type:' + str(type(e))
            print 'args:' + str(e.args)
            print 'message:' + e.message
            print 'e自身:' + str(e)
            res_tuple = self.get_virtual_res("993")
            content_dic = json.loads(res_tuple[1])
#        res_tuple = client.request(uri+param_str, "GET")
        
#        content_dic = json.loads(res_tuple[1])
        if str(res_tuple[0]["status"]) == "200":
            tw_ids = self.write_tweet_to_csv(content_dic, client_id)
            # exit hantei
            if len(tw_ids) > 0:
                min_tw_id = min(tw_ids)
            
                if "x-rate-limit-remaining" in res_tuple[0].keys():
                    remaining = int(res_tuple[0]["x-rate-limit-remaining"])
                else:
                    remaining -= 1
                
                if "x-rate-limit-reset" in res_tuple[0].keys():
                    reset_time = int(res_tuple[0]["x-rate-limit-reset"])
            
                if remaining > 0:
                    print "Client ID " + str(client_id) + ": " + "Result: " + "min_tw_id: " + str(min_tw_id) + ", since_tw_id: " + str(since_tw_id)

                else:
                    now_time = int(time.time()) + 1
                    wait_sec = reset_time - now_time
                    if wait_sec < 0:
                        wait_sec = 0
                    reset_datetime = self.trans_unixsec_to_mysqldatetime_style(reset_time+2)
                    print "Client ID " + str(client_id) + ": " + "api limit expired, wait " + str(wait_sec) + " second. start at " + reset_datetime

                    time.sleep(wait_sec + 2)
                    remaining, reset_time = self.get_search_api_rate_remaining(client_id)
                
                return min_tw_id, len(tw_ids), remaining

            else:
                return 0, len(tw_ids), remaining

        else:
            # for error
            status = str(res_tuple[0]["status"])
            message_dic = json.loads(res_tuple[1])
            message = message_dic["errors"][0]["message"]
            print status + ": " + message
            print "sleep 10 sec"
            time.sleep(300)
            
            if "x-rate-limit-remaining" in res_tuple[0].keys():
                remaining = int(res_tuple[0]["x-rate-limit-remaining"])
            else:
                remaining -= 1
            return max_tw_id, 1000000, remaining

    def write_tweet_to_csv(self, content_dic, client_id):
        all_tweets = content_dic["statuses"]
        tw_ids = []

        for i, a_tw in enumerate(all_tweets):
#            print a_tw["created_at"]
#            print a_tw["id"]
#            print a_tw["source"]
#            print a_tw["text"]
#            print a_tw["user"]["id"]
#            print a_tw["user"]["screen_name"]
            tw_ids.append(int(a_tw["id"]))
            tweet = a_tw["text"].replace("\r\n", "")
            tweet = tweet.replace("\n", "")
            mysqldatetimestyle = self.trans_tw_time_to_mysqldatetime_style(a_tw["created_at"])
            savefile = self.get_file_names(a_tw["created_at"], client_id)
#            a_tw_data = [ a_tw["id"], a_tw["created_at"], a_tw["user"]["id"], a_tw["user"]["screen_name"], tweet, a_tw["source"] ]
            a_tw_data = [ a_tw["id"], mysqldatetimestyle, a_tw["user"]["id"], a_tw["user"]["screen_name"], tweet, a_tw["source"] ]

#            fh = codecs.open(savefile, "a","utf-8")
            fh = open(savefile, "a")
            writer = csv.writer(fh, delimiter=',', quotechar='"', lineterminator="\n", quoting=csv.QUOTE_ALL)            
            writer.writerow(a_tw_data)
            fh.close()

        return tw_ids
    
    def run_multi_process(self):
        jobs = []
        for i in range(len(self.twkeys)):
#        for i in range(2):
            client_id = i
            p = Process( target=self.run, args=(client_id,) )
            jobs.append(p)
            p.start()
            
    def run_multi_thread(self):
        jobs = []
        for i in range(len(self.twkeys)):
#        for i in range(2,4):
            client_id = i
            t = Thread(target=self.run, args=(client_id,))
            jobs.append(t)
#            t.daemon = True
            t.start()

    
    def run(self, client_id):
        """
        
        """
#        client = self.clients[4]
#        client_id = 4
#        remaining, reset_time = self.get_search_api_rate_remaining(client_id)

        strat_time = int(time.time())
        passed_time = 0
#        crawl_period = 300
        crawl_period = 5 
        
        remaining = 0
#        remaining = 1
#        remaining = 2
        reset_time = 0
        
        since_tw_id = 269454761911271425 # 2012 / 11 / 16　の23:59あたりのツイートID
#        since_tw_id = 286834243169054720
        i = 0
        while(True):
            i += 1        
            if remaining == 0:
                wait_sec = reset_time - int(time.time())
                if wait_sec < 0:
                    wait_sec = 0
                reset_datetime = self.trans_unixsec_to_mysqldatetime_style(reset_time+2)
                print "Client ID " + str(client_id) + ": " + "api limit expired, wait " + str(wait_sec) + " second. start at " + reset_datetime

                time.sleep( wait_sec + 2)
                remaining, reset_time = self.get_search_api_rate_remaining(client_id)
        
            start_time = int(time.time())
            
            since_tw_id = self.search_keyword(client_id, remaining, reset_time, since_tw_id, self.search_words[client_id])
            print "Client " + str(client_id) + ": " + str(i) + "-th crawl is complete!!"
        
            end_time = int(time.time())
            passed_time = end_time - start_time
            sleep_time = crawl_period - passed_time
            if sleep_time > 0:
                start_datetime = int(time.time()) + sleep_time + 2
                start_datetime_dtstyle = self.trans_unixsec_to_mysqldatetime_style(start_datetime)
                print "Client " + str(client_id) + ": " + "sleep to next crawl at " + start_datetime_dtstyle
                time.sleep(sleep_time + 2)
            remaining, reset_time = self.get_search_api_rate_remaining(client_id)

    def get_search_api_rate_remaining(self, client_id):
        client = self.clients[client_id]
        res_dic = self.check_api_limit(client_id)
#        print res_dic["resources"]

        remaining = res_dic["resources"]["search"]["/search/tweets"]["remaining"]
        reset_time = res_dic["resources"]["search"]["/search/tweets"]["reset"]
        return remaining, reset_time

    def get_virtual_res(self, status_code):
        # 999は架空のエラー（例外処理に利用)
        virtual_message_dic = {"errors": [{"message": "Virtual Exception Message desu."},]}
        virtual_message_dic_str = json.dumps(virtual_message_dic)

        virtual_res = [{"status":str(status_code)}, virtual_message_dic_str]

        return virtual_res

    def check_api_limit(self, client_id):
        client = self.clients[client_id]
        uri = "https://api.twitter.com/1.1/application/rate_limit_status.json?"
        resources_l = "resources=account,application,blocks,direct_messages,followers,friends,friendships,geo,help,lists,saved_searches,search,statuses,trends,users"

        ret = self.get_virtual_res("990")

        while( str(ret[0]["status"]) != "200" ):
            try:
                ret = client.request(uri+resources_l, "GET")
            except Exception as e:
                print '=== エラー内容(Exception Error!!) ==='
                print 'type:' + str(type(e))
                print 'args:' + str(e.args)
                print 'message:' + e.message
                print 'e自身:' + str(e)
                ret = self.get_virtual_res("991")

            if str(ret[0]["status"]) != "200":
                print "Client " + str(client_id) + ": Value Exception !!: " + str(ret)
                print "sleep 10 sec."
                time.sleep(10)

        ret_dic = json.loads(ret[1])
        return ret_dic

    def deepdic_print(self, ret_dic, layer=0):
        space = "    " * layer
#        print type(ret_dic)
        if isinstance(ret_dic, tuple) or isinstance(ret_dic, list):
            space = "    " * layer
            print space + "["
            layer += 1
            for ele in ret_dic:
                self.deepdic_print(ele, layer)
            layer -= 1
            space = "    " * layer
            print space + "]"
        elif isinstance(ret_dic, str):
            new_dic = json.loads(ret_dic)
            self.deepdic_print(new_dic, layer)
        elif isinstance(ret_dic, dict):
            space = "    " * layer
            print space + "{"
            layer += 1
            space = "    " * layer
            for key in sorted( ret_dic.keys() ):
#                print type(ret_dic[key])
                if isinstance(ret_dic[key], dict):
                    print space + key + ":"
                    seconddic = ret_dic[key]
                    layer += 1
                    self.deepdic_print(seconddic, layer)
                    layer -= 1

                elif isinstance(ret_dic[key], tuple) or isinstance(ret_dic[key], list):
                    print space + key + ":"
                    for ele in ret_dic[key]:
                        layer += 1
                        self.deepdic_print(ele, layer)
                        layer -= 1

                else:
                    print space + key + ": " + str(ret_dic[key])
            layer -= 1
            space = "    " * layer
            print space + "}"

if __name__ == '__main__':
    obj = TwitterKeywordCrawler()
    obj.run(14)
#    obj.run_multi_process()
#    obj.run_multi_thread()
    
    pass
