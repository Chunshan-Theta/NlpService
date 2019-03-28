import tensorflow as tf
import numpy as np
from os import listdir
from os.path import isfile, join
import re
import json
import random
from random import randint
import sys
sys.path.append('./jieba_zn/')
import jieba
from jieba import posseg as pseg
import jieba.analyse
from os import environ
environ['TF_CPP_MIN_LOG_LEVEL']='2' #silence waring logs
import json
import os
from os.path import dirname, realpath, sep, pardir

root = dirname(realpath(__file__)) + sep


def SentencesCuter(source):
    source = source.replace(" ", "") #remove space
    #clear special character:only chinese
    source_list = jieba.lcut(source, cut_all=False)
    source = "".join(source_list)
    source = re.sub("[^\u4e00-\u9fff]", "", source)
    words = pseg.cut(source)
    re_lcut=[]
    allowedtype=["n","v","vd","vn","ns","a","d","ad","an","x"]
    for word, flag in words:

        if flag in allowedtype:
            re_lcut.append(word)
        else:
            pass#print(word,flag)

    #print("".join(re_lcut))
    return re_lcut

#Step 1.1: load word embeddings data


print("loading idxWord")
wordsList = list(np.load(root+'idxWord.npy'))
print(wordsList[0])

wordVectors=[]
print("loading idxWordVectors")
wordVectors = np.load(root+'idxWordVectors.npy')



finWord = int(len(wordsList))
assert type(wordVectors.shape) is tuple




#Step3.2: defind config for training
batchSize = 24
lstmUnits = 64
numClasses = 2
iterations = 100000
maxSeqLength = 35
numDimensions = 300



# delete the current graph
tf.reset_default_graph()




sess = tf.Session()
# import the graph from the file
saver = tf.train.import_meta_graph(root+'models/pretrained_lstm.ckpt-100000.meta')
# restore the saved vairable
saver.restore(sess, tf.train.latest_checkpoint(root+'models'))
graph = tf.get_default_graph()


accuracy = tf.get_collection("accuracy")[0]
input_data = tf.get_collection("input_data")[0]
labels = tf.get_collection("labels")[0]
prediction = tf.get_collection("prediction")[0]
PredResult = tf.get_collection("PredResult")[0]
ModelAccuracy = 0

#StepPredResult = sess.run([PredResult], {input_data: nextBatch})
#print(StepPredResult,nextBatchLabels)



#Step5.2: testing the model by string
def testingSpeech(source):


    source_list = SentencesCuter(source)
    Sentence = np.zeros((maxSeqLength), dtype='int32')
    idx = 0
    for i in source_list:
        try:
            Sentence[idx] = wordsList.index(i)

        except:
            pass#Sentence[idx] =0
        idx+=1

        #break the process if the sentence too long
        if idx>=maxSeqLength:break
    #print(source_list)


    #input_data_Sentence,input_data_Ans = getTestBatch()
    #input_data_Sentence[0] = Sentence

    input_data_Sentence=[Sentence for i in range(24)]
    p_result,p_value = sess.run([PredResult,prediction], {input_data: input_data_Sentence})


    prediction_rate = p_value[0][:]
    prediction_answer = p_result[0]


    diff = prediction_rate[0]-prediction_rate[1]
    diff2 = sum([i[0]-i[1]for i in p_value])/24
    #print(p_result,diff2)
    #print(prediction_answer,diff)
    #print('----')
    return prediction_answer,diff



'''
testingSpeech('房間糟透了 早餐也很難吃')
testingSpeech('房間很好 早餐好吃')
testingSpeech('服務員很親切 房間採光很好很舒適')
testingSpeech('服務員態度很糟糕 房間很小')
'''
p1=["我同意",
  "你說的沒錯",
  "很好"]
p2=[
  "我認為我們的共識是正確的",
  "妳的論述很合理",
  "我認同你的論點",
  "你說的很好"]
p3=[
  "我認為你的推論很正確有很多證據可以證明你的論點",
  "我相信妳的推論聽起來很有道理",
  "你說的是正確的的確證據是顯示出這樣的情況",
  "妳的說法還有一些漏洞但我大致上認同你的論述",
  "妳說的怪怪的但大致上你的論述還算合理"]

n1 = ["我不同意",
  "你說的並不正確",
  "我不同意你的看法"]
n2 = [
  "我們目前還沒有共識",
  "你說的部分有點問題",
  "妳的論述並不合理",
  "我沒辦法認同你的論點"]
n3 = [
  "我認為你的推論很不正確除非我有看到更多的證據來判斷",
  "我沒辦法相信妳的推論除非妳有更多的證據可以證明",
  "你說的是錯誤的的確證據並沒有顯示出這樣的情況",
  "你說的聽起來很有道理但我們應該要拿出證據說話",
  "我能夠體會妳的想法但我認為其中有些問題"]
'''
count = 0
for i in p1+p2+p3:
    _,diff = testingSpeech(i)
    print(diff)
    count = count+1 if diff >-0.5 else count
print(count/len(p1+p2+p3))

count = 0
for i in n1+n2+n3:
    _,diff = testingSpeech(i)
    print(diff)
    count = count+1 if 0.5>diff  else count
print(count/len(n1+n2+n3))
'''
