# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.five_divisions_result import FiveDivisionsResult  # noqa: E501
from swagger_server.models.score_analysis_result import ScoreAnalysisResult  # noqa: E501
from swagger_server.models.sentence import Sentence  # noqa: E501
from swagger_server.models.speech import Speech  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSpeechAnalysisController(BaseTestCase):
    """SpeechAnalysisController integration test stubs"""

    def test_speech_emotion_post(self):
        """Test case for speech_emotion_post

        
        """
        body = Speech()
        response = self.client.open(
            '/NLP/speech/emotion',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_speech_five_divisions_post(self):
        """Test case for speech_five_divisions_post

        
        """
        body = Speech()
        response = self.client.open(
            '/NLP/speech/fiveDivisions',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_speech_score_post(self):
        """Test case for speech_score_post

        
        """
        body = Speech()
        response = self.client.open(
            '/NLP/speech/score',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
