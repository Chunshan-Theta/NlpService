# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.server_status_respond import ServerStatusRespond  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCheckStatusController(BaseTestCase):
    """CheckStatusController integration test stubs"""

    def test_speech_emotion_options(self):
        """Test case for speech_emotion_options


        """
        response = self.client.open(
            '/NLP/speech/emotion',
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_speech_five_divisions_options(self):
        """Test case for speech_five_divisions_options


        """
        response = self.client.open(
            '/NLP/speech/fiveDivisions',
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_speech_score_options(self):
        """Test case for speech_score_options


        """
        response = self.client.open(
            '/NLP/speech/score',
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
