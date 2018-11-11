import connexion
import six

from swagger_server.models.error_respond import ErrorRespond  # noqa: E501
from swagger_server.models.word_distance_result import WordDistanceResult  # noqa: E501
from swagger_server import util


def word2vec_word_distance_get(word):  # noqa: E501
    """getting data of member.

    usually for logining method or getting a member&#39;s data. # noqa: E501

    :param word: split by &#39;,&#39;
    :type word: str

    :rtype: WordDistanceResult
    """
    return 'do some magic!',404,{"headers":"helloworld"}
