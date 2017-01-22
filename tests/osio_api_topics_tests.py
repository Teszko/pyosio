# coding=utf-8

from pyosio.osio import OpenSensorsAPI
import types
import six
import unittest
import logging


logger = logging.getLogger(__name__)


class OSIOAPITopicsTests(unittest.TestCase):

    def setUp(self):
        # add your test case
        USER_ID, API_KEY = None, None
        self._api = OpenSensorsAPI(USER_ID, API_KEY)

    def test_get_pub_topic_info(self):
        # GET /v1/public/topics/{topic}
        logger.info('TEST: GET /v1/public/topics/{topic} ')
        # add your test case
        TEST_TOPIC = None
        self.assertNotEqual(self._api.get_pub_topic_info(TEST_TOPIC),  None)

    def test_search_pub_topic_info(self):
        # GET /v1/search/topics/{term}
        logger.info('TEST: GET /v1/search/topics/{term}')
        # add your test case
        TEST_TERM_TOPIC = None
        self.assertNotEqual(
            self._api.search_pub_topic_info(TEST_TERM_TOPIC), None)

    def test_set_topic(self):
        # POST /v1/topics
        logger.info('TEST: POST /v1/topics')
        # add your test case
        new_topic_input = None
        self.assertNotEqual(self._api.set_topic(new_topic_input),  None)

    def test_delete_topic(self):
        # DELETE /v1/topics/{topic}
        logger.info('TEST: DELETE /v1/topics/{topic}')
        # add your test case
        TEST_TOPIC = None
        self.assertNotEqual(self._api.delete_topic(TEST_TOPIC), None)

    def test_get_topic_meta(self):
        # GET /v1/topics/{topic}
        logger.info('TEST: GET /v1/topics/{topic}')
        # add your test case
        TEST_TOPIC = None
        self.assertNotEqual(self._api.get_topic_meta(TEST_TOPIC), None)

    def test_update_topic_meta(self):
        # PUT /v1/topics/{topic}
        logger.info('TEST: PUT /v1/topics/{topic}')
        # add your test case
        TEST_TOPIC, topic_input = None, None
        self.assertNotEqual(
            self._api.update_topic_meta(TEST_TOPIC, topic_input), False)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
