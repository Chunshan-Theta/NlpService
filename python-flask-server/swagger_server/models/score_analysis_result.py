# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.sentence import Sentence  # noqa: F401,E501
from swagger_server import util


class ScoreAnalysisResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, score: float=None, _pass: bool=None, source: Sentence=None):  # noqa: E501
        """ScoreAnalysisResult - a model defined in Swagger

        :param score: The score of this ScoreAnalysisResult.  # noqa: E501
        :type score: float
        :param _pass: The _pass of this ScoreAnalysisResult.  # noqa: E501
        :type _pass: bool
        :param source: The source of this ScoreAnalysisResult.  # noqa: E501
        :type source: Sentence
        """
        self.swagger_types = {
            'score': float,
            '_pass': bool,
            'source': Sentence
        }

        self.attribute_map = {
            'score': 'score',
            '_pass': 'pass',
            'source': 'source'
        }

        self._score = score
        self.__pass = _pass
        self._source = source

    @classmethod
    def from_dict(cls, dikt) -> 'ScoreAnalysisResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The scoreAnalysisResult of this ScoreAnalysisResult.  # noqa: E501
        :rtype: ScoreAnalysisResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def score(self) -> float:
        """Gets the score of this ScoreAnalysisResult.


        :return: The score of this ScoreAnalysisResult.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score: float):
        """Sets the score of this ScoreAnalysisResult.


        :param score: The score of this ScoreAnalysisResult.
        :type score: float
        """

        self._score = score

    @property
    def _pass(self) -> bool:
        """Gets the _pass of this ScoreAnalysisResult.


        :return: The _pass of this ScoreAnalysisResult.
        :rtype: bool
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass: bool):
        """Sets the _pass of this ScoreAnalysisResult.


        :param _pass: The _pass of this ScoreAnalysisResult.
        :type _pass: bool
        """

        self.__pass = _pass

    @property
    def source(self) -> Sentence:
        """Gets the source of this ScoreAnalysisResult.


        :return: The source of this ScoreAnalysisResult.
        :rtype: Sentence
        """
        return self._source

    @source.setter
    def source(self, source: Sentence):
        """Sets the source of this ScoreAnalysisResult.


        :param source: The source of this ScoreAnalysisResult.
        :type source: Sentence
        """

        self._source = source
