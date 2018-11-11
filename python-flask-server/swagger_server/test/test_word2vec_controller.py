# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_respond import ErrorRespond  # noqa: E501
from swagger_server.models.word_distance_result import WordDistanceResult  # noqa: E501
from swagger_server.test import BaseTestCase


class TestWord2vecController(BaseTestCase):
    """Word2vecController integration test stubs"""

    def test_word2vec_word_distance_get(self):
        """Test case for word2vec_word_distance_get

        getting data of member.
        """
        query_string = [('word', '英國,美國,台灣')]
        response = self.client.open(
            '/NLP/word2vec/wordDistance',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
