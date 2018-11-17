import connexion
import six

from swagger_server.models.five_divisions_result import FiveDivisionsResult  # noqa: E501
from swagger_server.models.score_analysis_result import ScoreAnalysisResult  # noqa: E501
from swagger_server.models.sentence import Sentence  # noqa: E501
from swagger_server.models.speech import Speech  # noqa: E501
from swagger_server import util


#local
from swagger_server.controllers.tool import WordDistance as WD
from swagger_server.controllers.tool.jieba_zn import jieba
from swagger_server.controllers.tool.jieba_zn.jieba import posseg as pseg
from swagger_server.controllers.tool.jieba_zn.jieba import analyse


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
        for word, flag in pseg.cut(source):
            #print('%s %s' % (word, flag))
            word_array.append(word)

        top10 = []
        for item in jieba.analyse.tfidf(source, topK=10, withWeight=True, allowPOS=('n','v','x')):
            #print item[0],item[1]
            top10.append(item[0])
        emotion = 0.0
        sentence = Sentence(source, word_array, top10, emotion)
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
        word_array=[]
        for word, flag in pseg.cut(source):
            #print('%s %s' % (word, flag))
            word_array.append(word)

        top10 = []
        for item in jieba.analyse.tfidf(source, topK=10, withWeight=True, allowPOS=('n','v','x')):
            #print item[0],item[1]
            top10.append(item[0])
        emotion = 0.0
        sentence = Sentence(source, word_array, top10, emotion)
        name_division=["民眾","政府","企業","專家","環境"]
        name_division_keyWords=[["民眾","人民","人","安全"],["政府","國家","法律","發展"],["企業","成本","經濟","產品"],["專家","技術","分析"],["環境","生態","污染"]]
        score_division=[]
        for division in name_division_keyWords:
            assert type(division) is list
            assert type(top10) is list
            score_division.append(WD.Distance_word_list(top10,division))
        high_to_low = []
        dictDistanceDiv = {}
        for Distance_idx in range(len(score_division)):
            Distance =score_division[Distance_idx]
            dictDistanceDiv[Distance_idx] = Distance
        sorted_by_value = sorted(dictDistanceDiv.items(), key=lambda kv: kv[1])
        for i in sorted_by_value:
            high_to_low.append(i[0])
        print("sorted_by_value")
        print(sorted_by_value)
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
    return 'do some magic!'
