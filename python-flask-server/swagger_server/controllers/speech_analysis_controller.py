import connexion
import six

from swagger_server.models.five_divisions_result import FiveDivisionsResult  # noqa: E501
from swagger_server.models.score_analysis_result import ScoreAnalysisResult  # noqa: E501
from swagger_server.models.sentence import Sentence  # noqa: E501
from swagger_server.models.speech import Speech  # noqa: E501
from swagger_server import util



def speech_emotion_post(body):  # noqa: E501
    """

     # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: Sentence
    """
    if connexion.request.is_json:
        body = Speech.from_dict(connexion.request.get_json())  # noqa: E501

    return 'do some magic!',201,{'header': '123'}


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
