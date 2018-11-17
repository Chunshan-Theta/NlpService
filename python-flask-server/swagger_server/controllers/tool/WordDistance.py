# -*- coding:utf-8 -*-
#!usr/bin/env python
import json
import os
from os.path import dirname, realpath, sep, pardir

root = dirname(realpath(__file__)) + sep

Json_file = open(root+"word2vecJson.txt","r")
Json_file = json.load(Json_file)

def location(text):
    #uni_text=unicode(text,"utf-8")
    uni_text = text
    try:
        #print(Json_file[uni_text])
        return Json_file[uni_text]
    except KeyError :
        #print(uni_text)
        return
def Distance(t1,t2):
    x = t1[0]-t2[0]
    y = t1[1]-t2[1]
    return ((x**2+y**2)**0.5)*10000000000

def Distance_word(w1,w2):
    #print(w1+','+w2)
    return Distance(location(w1),location(w2))

def Distance_word_list(w1_array,w2_array,type="top"):
    if type == "top":
        minDistance = 1000
        for w1 in w1_array:
            for w2 in w2_array:
                unitDistance = Distance_word(w1,w2)
                if unitDistance < minDistance:
                    minDistance = unitDistance
        return minDistance
    else:
        raise NameError('type not found')


'''
Distance_word("害怕","恐懼")
Distance_word("害怕","畏懼")
Distance_word("害怕","喜歡")
Distance_word("害怕","安全")
'''
