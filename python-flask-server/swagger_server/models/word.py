# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Word(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, content: str=None, word2vec: float=None, emotion: float=None):  # noqa: E501
        """Word - a model defined in Swagger

        :param content: The content of this Word.  # noqa: E501
        :type content: str
        :param word2vec: The word2vec of this Word.  # noqa: E501
        :type word2vec: float
        :param emotion: The emotion of this Word.  # noqa: E501
        :type emotion: float
        """
        self.swagger_types = {
            'content': str,
            'word2vec': float,
            'emotion': float
        }

        self.attribute_map = {
            'content': 'content',
            'word2vec': 'word2vec',
            'emotion': 'emotion'
        }

        self._content = content
        self._word2vec = word2vec
        self._emotion = emotion

    @classmethod
    def from_dict(cls, dikt) -> 'Word':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The word of this Word.  # noqa: E501
        :rtype: Word
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content(self) -> str:
        """Gets the content of this Word.


        :return: The content of this Word.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content: str):
        """Sets the content of this Word.


        :param content: The content of this Word.
        :type content: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def word2vec(self) -> float:
        """Gets the word2vec of this Word.


        :return: The word2vec of this Word.
        :rtype: float
        """
        return self._word2vec

    @word2vec.setter
    def word2vec(self, word2vec: float):
        """Sets the word2vec of this Word.


        :param word2vec: The word2vec of this Word.
        :type word2vec: float
        """

        self._word2vec = word2vec

    @property
    def emotion(self) -> float:
        """Gets the emotion of this Word.


        :return: The emotion of this Word.
        :rtype: float
        """
        return self._emotion

    @emotion.setter
    def emotion(self, emotion: float):
        """Sets the emotion of this Word.


        :param emotion: The emotion of this Word.
        :type emotion: float
        """

        self._emotion = emotion
