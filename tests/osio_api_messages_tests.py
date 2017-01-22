# coding=utf-8

from pyosio.osio import OpenSensorsAPI
import types
import six
import unittest
import logging

logger = logging.getLogger(__name__)


class OSIOAPIMessagesTests(unittest.TestCase):

    def setUp(self):
        # add your test case
        USER_ID, API_KEY = None, None
        self._api = OpenSensorsAPI(USER_ID, API_KEY)

    def test_get_device_msgs(self):
        # GET /v1/messages/device/{client-id}
        logger.info('TEST: GET /v1/messages/device/{client-id}')
        # add your test case
        TEST_DEVICE_ID = None
        self.assertNotEqual(self._api.get_device_msgs(TEST_DEVICE_ID), None)

    def test_get_topic_msgs(self):
        # GET /v1/messages/topic/{topic}
        logger.info('TEST: GET /v1/messages/topic/{topic}')
        # add your test case
        TEST_TOPIC = None
        self.assertNotEqual(self._api.get_topic_msgs(TEST_TOPIC), None)

    def test_get_user_msgs(self):
        # GET /v1/messages/user/{user-id}
        logger.info('TEST: GET /v1/messages/user/{user-id}')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_user_msgs(USER_ID), None)

    def test_get_pub_dataset_msgs(self):
        # GET /v2/public/messages/dataset/{dataset-id}
        logger.info('TEST: GET /v2/public/messages/dataset/{dataset-id}')
        # add your test case
        TEST_DATASET = None
        self.assertNotEqual(self._api.get_pub_dataset_msgs(TEST_DATASET), None)

    def test_get_bulk_pub_dataset_msgs(self):
        # POST /v2/public/messages/dataset/bulk
        logger.info('TEST: POST /v2/public/messages/dataset/bulk')
        # add your test case
        bulk_msgs = None
        self.assertNotEqual(
            self._api.get_bulk_pub_dataset_msgs(bulk_msgs), None)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
