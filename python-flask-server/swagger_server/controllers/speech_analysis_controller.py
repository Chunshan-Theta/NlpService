import connexion
import six
import math
from swagger_server.models.five_divisions_result import FiveDivisionsResult  # noqa: E501
from swagger_server.models.score_analysis_result import ScoreAnalysisResult  # noqa: E501
from swagger_server.models.sentence import Sentence  # noqa: E501
from swagger_server.models.speech import Speech  # noqa: E501
from swagger_server import util



#local
from swagger_server.controllers.tool import calculateWordVecDistance as WD
from swagger_server.controllers.tool.jieba_zn import jieba
#from swagger_server.controllers.tool.jieba_zn.jieba import posseg as pseg
from swagger_server.controllers.tool.jieba_zn.jieba import analyse
'''
import os
from os.path import dirname, realpath, sep, pardir
root = dirname(realpath(__file__)) + sep
jieba.load_userdict(root+'tool/dict.new.tw')
'''
def speech_emotion_post(body):  # noqa: E501
    """

     # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: Sentence
    """
    if connexion.request.is_json:
        body = Speech.from_dict(connexion.request.get_json())  # noqa: E501
        source = body.source
        topic = body.topic
        word_array=[]
        for item in jieba.analyse.tfidf(source, topK=None, withWeight=True, allowPOS=False):
            #print item[0],item[1]
            word_array.append(item[0])
        topKeyword = word_array[:10]

        name_division_keyWords=[["良好","優勢","正確","挑戰","貢獻","助於","鼓勵","成功"],["不幸","不良","失敗","錯誤","損失","傷","惡","遺憾","不安","造成","突然"]]
        score_division=[]
        for division in name_division_keyWords:
            assert type(division) is list
            assert type(topKeyword) is list
            score_division.append(WD.Distance_word_list(topKeyword,division))

        emotion = score_division[1]-score_division[0]
        sentence = Sentence(source, word_array, topKeyword, emotion)
        return sentence,200
    else:
        return 'bad request ',400


def speech_five_divisions_post(body):  # noqa: E501
    """

     # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: FiveDivisionsResult
    """
    if connexion.request.is_json:
        body = Speech.from_dict(connexion.request.get_json())  # noqa: E501
        source = body.source
        topic = body.topic

        # class sentence
        word_array=[]
        for word in jieba.cut(source,cut_all=False):
            #print('%s %s' % (word, flag))
            word_array.append(word)

        topKeyword = []
        for item in jieba.analyse.tfidf(source, topK=30, withWeight=True, allowPOS=False):
            #print item[0],item[1]
            topKeyword.append(item[0])
        emotion = 0.0
        sentence = Sentence(source, word_array, topKeyword, emotion)



        name_division=["民眾","政府","經濟","可行性","永續"]
        name_division_keyWords=[["民眾","大家","健康","安全","規定"],["政府","國家","法律","發展","事故"],["企業","成本","經濟","產品","營運"],["專家","技術","分析","資料","統計"],["環境","生態","污染","生物","危害"]]
        distanceTopAndDivision=[]
        for division in name_division_keyWords:
            assert type(division) is list
            assert type(topKeyword) is list
            distanceTopAndDivision.append(WD.Distance_word_list(topKeyword,division))
        high_to_low = []
        dictDistanceDiv = {}
        divisionLength = len(distanceTopAndDivision)
        maxDistance = int(max(distanceTopAndDivision))+1
        score_division = [None]*divisionLength
        for Distance_idx in range(divisionLength):
            unitDistance = distanceTopAndDivision[Distance_idx]
            dictDistanceDiv[Distance_idx] = unitDistance
            score_division[Distance_idx] = maxDistance-unitDistance

        # smooth score
        highestScore = max(score_division)
        lowestScore = min(score_division)
        while highestScore-lowestScore>=35:
            for idx in range(divisionLength):
                score_division[idx] = (score_division[idx]**0.5)*10
                # keep score under 100
                score_division[idx] = score_division[idx] if score_division[idx] <= 100 else 100
            highestScore = max(score_division)
            lowestScore = min(score_division)

        #level
        #assume complete discussion needs 50-time conversation, and each speech's length is 10 words.
        allWordsCount = 1000
        level = len(source)/allWordsCount if len(source)/allWordsCount<=1 else 1
        level = level if level>=0.1 else 0.1
        for idx in range(divisionLength):
            score_division[idx] = score_division[idx]*level


        sorted_by_value = sorted(dictDistanceDiv.items(), key=lambda kv: kv[1])
        for i in sorted_by_value:
            high_to_low.append(i[0])
        #print("sorted_by_value")
        #print(sorted_by_value)
        _pass = True
        DivResult =  FiveDivisionsResult(high_to_low, score_division, name_division, _pass, sentence)  # noqa: E501




        return DivResult,200
    else:
        return 'bad request ',400


def speech_score_post(body):  # noqa: E501
    """

     # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: ScoreAnalysisResult
    """
    if connexion.request.is_json:
        body = Speech.from_dict(connexion.request.get_json())  # noqa: E501
        source = body.source
        topic = body.topic

        # class sentence
        word_array=[]
        topKeyword = []


        for word,f in jieba.analyse.tfidf(source, topK=None, withWeight=True, allowPOS=False):
            #print item[0],item[1]
            word_array.append(word)
        topKeyword = word_array[:10]
        emotion = 0.0
        sentence = Sentence(source, word_array, topKeyword, emotion)

        topicWordArray=[]
        for word ,f in jieba.analyse.tfidf(topic, topK=None, withWeight=True, allowPOS=False):
            #print('%s %s' % (word, flag))
            topicWordArray.append(word)

        assert type(topicWordArray) is list
        assert type(topKeyword) is list
        score = 30 - WD.Distance_word_list(topKeyword,topicWordArray,"Min")


        _pass = False
        if score >= 0:
            _pass = True

        scoreResult = ScoreAnalysisResult(score, _pass, sentence)
        return scoreResult,200
    else:
        return 'bad request ',400
