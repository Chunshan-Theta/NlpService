# -*- coding:utf-8 -*-
#!usr/bin/env python

import json
import os
from os.path import dirname, realpath, sep, pardir

root = dirname(realpath(__file__)) + sep

print('loading Word vector Data .......')

Json_file = open(root+"outputWord2Vec(v300)(50000).txt","r")
Json_file = json.load(Json_file)
print('loading  Data done.')


def location(text):
    #uni_text=unicode(text,"utf-8")
    uni_text = text
    try:
        #print(Json_file[uni_text])
        if Json_file[uni_text] is not None:
            return Json_file[uni_text]
        else:
            return
    except KeyError :
        #print(uni_text)
        return
def Distance(t1,t2):
    try:
        assert len(t1) == len(t2)
        sum=0
        for i in range(len(t1)):
            sum+=((t1[i]-t2[i])**2)


        #x = t1[0]-t2[0]
        #y = t1[1]-t2[1]
        #return ((x**2+y**2)**0.5)*10000000000
        return (sum**0.5)*100
    except TypeError:
        return 1000

def Distance_word(w1,w2):
    #print(w1+','+w2)
    if location(w1) is not None and location(w2) is not None:
        return float(Distance(location(w1),location(w2)))
    else:
        return

'''
print('loading json Data .......')
Json_file = open("./output/outputWord2Vec(v300)(50000).txt","r")
Json_file = json.load(Json_file)

print(d)
print(d[u'\u5c07\u4e4b\u652c'])
print(u'\u5c07\u4e4b\u652c')


print('calculate distance .......')

Distance_word("害怕","恐懼")
Distance_word("害怕","畏懼")
Distance_word("害怕","喜歡")
Distance_word("害怕","安全")
'''


def Distance_word_list(w1_array,w2_array,type="Min"):
    if type == "Min":
        minDistance = 1000
        for w1 in w1_array:
            for w2 in w2_array:
                unitDistance = Distance_word(w1,w2)
                if unitDistance is not None:
                    if unitDistance < minDistance:
                        minDistance = unitDistance
                        
        return minDistance
    elif type == "Average":
        sumDistance = 0
        count = 0
        for w1 in w1_array:
            for w2 in w2_array:
                unitDistance = Distance_word(w1,w2)
                if unitDistance is not None:
                    sumDistance+=unitDistance
                    count+=1
        return sumDistance/count
    elif type == "Top3":
        t1,t2,t3 =1000,1000,1000
        for w1 in w1_array:
            for w2 in w2_array:
                unitDistance = Distance_word(w1,w2)
                if unitDistance is not None:
                    if t1 > unitDistance:
                        t1 = unitDistance
                    elif t2 > unitDistance:
                        t2 = unitDistance
                    elif t3 > unitDistance:
                        t3 = unitDistance
                    else:
                        pass
        #print(w1_array)
        #print(w2_array)
        return t1+t2+t3/3
    elif type == "Max":
       maxDistance = 0
       for w1 in w1_array:
           for w2 in w2_array:
               unitDistance = Distance_word(w1,w2)
               if unitDistance is not None:
                   if unitDistance > maxDistance:
                       maxDistance = unitDistance
       return maxDistance
    else:
        raise NameError('type not found')
