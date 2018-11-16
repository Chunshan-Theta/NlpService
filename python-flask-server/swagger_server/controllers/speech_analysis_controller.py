import connexion
import six

from swagger_server.models.five_divisions_result import FiveDivisionsResult  # noqa: E501
from swagger_server.models.score_analysis_result import ScoreAnalysisResult  # noqa: E501
from swagger_server.models.sentence import Sentence  # noqa: E501
from swagger_server.models.speech import Speech  # noqa: E501
from swagger_server import util


#local
from swagger_server.controllers.tool.WordDistance import Distance_word
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
        #source = "年底縣市長選舉進入倒數階段，這次高雄選情引人注目，國民黨候選人韓國瑜與民進黨候選人陳其邁戰況激烈。知名作家苦苓透露，上次質疑韓國瑜行騙，被一大票網友砲火猛攻，這回再度勇於發表評論，對於高雄勝負已定的說法，他表示「未必」，直指韓國瑜還有「 5 大隱憂」。 對於韓國瑜爆紅的原因，苦苓在《ETtoday東森新聞雲》雲論中，以老丁和老王兩人對話來分析。他認為，韓國瑜「冒充」素人，走台北市長柯文哲路線，自稱「賣菜的禿頭」，拉近了和民眾的距離，讓很多人都不知道他當過 2 屆立委、議員和副市長，根本是個不折不扣的政治人物。韓國瑜更故意發表一些有爭議的政見，例如「旗津開賭場」、「南海挖石油」，吸引媒體注目、提高能見度，更扮「弱者」說民進黨的權力比玉山高、金錢比台灣海峽還深，而他一人一隻孤鳥，什麼都沒有。 苦苓指出，韓國瑜知道自己在高雄沒有基層、組織、樁腳，所以就打「空戰」，三天兩頭往台北跑，就是為了網路上製造聲勢、嚇唬敵人，但他驍勇善戰、能接地氣、敢於創新，和傳統的國民黨政客大不相同，這也是他能吸引更多人的原因。 但面對高雄這一場選戰是否勝負已定的疑問，苦苓則直言「未必」，因為韓國瑜還有 5 大隱憂：第一、他說高雄「又老又舊」，傷了很多本地人的自尊心，覺得受侮辱，這一點他若無法彌補，會流失不少選票；第二、他當初說的那些「胡說」政見已深植人心，只要有讀點書的人都不以為然，覺得此人不可靠，他最好能花點時間解釋清楚那是玩笑話；第三、他在姊妹後援會上說：「來高雄投資，提供一千個工作機會，親一個，提供一萬個工作機會，陪睡一晚。」態度實在太輕浮了，對本性老實的高雄人，尤其老一輩來說，很難接受他。 第四點則是韓國瑜的聲勢雖然很大，但是「空氣」是否能化為選票，這一點千萬不能過於自滿。苦苓認為，高雄不是台北，「柯文哲模式」不能完全複製。除此之外，若他聲勢一來，國民黨中央想要乘勝追擊，黨內大咖都跑來站台的話就慘了！這正是韓國瑜的第 5 個隱憂：這些大咖都跑來只會提醒大家「韓國瑜是國民黨的」，很多人之所以支持他，就是因為他不像國民黨，一旦露出「真面目」也就前功盡棄。"
        word_array = []
        for word, flag in pseg.cut(source):
            #print('%s %s' % (word, flag))
            word_array.append(word)

        top10 = []
        for item in jieba.analyse.tfidf(source, topK=10, withWeight=True, allowPOS=('n','v','x')):
            #print item[0],item[1]
            top10.append(item[0])
        emotion = 0.0
        sentence =  Sentence(source, word_array, top10, emotion)
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
    return 'do some magic!'


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
