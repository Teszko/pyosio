# coding=utf-8

from pyosio.osio import OpenSensorsAPI
import types
import six
import unittest
import logging

logger = logging.getLogger(__name__)


class OSIORealtimeAPITests(unittest.TestCase):

    def setUp(self):
        # add your test case
        USER_ID, API_KEY = None, None
        self._api = OpenSensorsAPI(USER_ID, API_KEY)

    # ---------------------------------------- #
    # [v2] events : SSE streams for device & dataset event
    # ---------------------------------------- #

    def test_get_device_sd(self):
        # GET /v2/debug-events/{client-id}
        logger.info('TEST: GET /v2/debug-events/{client-id}')
        self._api._set_version("v2")
        # add your test case
        TEST_DEVICE_ID = None
        for item in self._api.get_device_sd(TEST_DEVICE_ID):
            self.assertTrue(True)
            return
        self.assertTrue(False)

    def test_get_pub_sd(self):
        # GET /v2/debug-events/{client-id}
        logger.info('TEST: GET /v2/debug-events/{client-id}')
        self._api._set_version("v2")
        # add your test case
        TEST_DEVICE_ID = None
        for item in self._api.get_pub_sd(TEST_DEVICE_ID):
            self.assertTrue(True)
            return
        self.assertTrue(False)

    # ---------------------------------------- #
    # events : SSE streams for device & message event
    # ---------------------------------------- #

    def test_get_org_topics_sd(self):
        # GET /v1/events/orgs/{org-id}/topics
        logger.info('TEST: GET /v1/events/orgs/{org-id}/topics')

        # add your test case
        TEST_ORG_ID = None
        for item in self._api.get_org_topics_sd(TEST_ORG_ID):
            self.assertTrue(True)
            return
        self.assertTrue(False)

    def test_get_topics_sd(self):
        # GET /v1/events/topics/{topic}
        logger.info('TEST: GET /v1/events/topics/{topic}')
        # add your test case
        TEST_TOPIC = None
        for item in self._api.get_topics_sd(TEST_TOPIC):
            self.assertTrue(True)
            return
        self.assertTrue(False)

    def test_get_user_bookmarked_topics_sd(self):
        # GET /v1/events/users/{user-id}/bookmarks
        logger.info('TEST: GET /v1/events/users/{user-id}/bookmarks')
        # add your test case
        USER_ID = None
        for item in self._api.get_user_bookmarked_topics_sd(USER_ID):
            self.assertTrue(True)
            return
        self.assertTrue(False)

    def test_get_user_topics_sd(self):
        # GET /v1/events/users/{user-id}/topics
        logger.info('TEST: GET /v1/events/users/{user-id}/topics')
        # add your test case
        USER_ID = None
        for item in self._api.get_user_topics_sd(USER_ID):
            self.assertTrue(True)
            return

        self.assertTrue(False)

    def test_get_pub_org_topics_sd(self):
        # GET /v1/public/events/orgs/{org-id}/topics
        logger.info('TEST: GET /v1/public/events/orgs/{org-id}/topics')
        # add your test case
        TEST_ORG_ID = None
        for item in self._api.get_pub_org_topics_sd(TEST_ORG_ID):
            print item
            # self.assertTrue(True)
            # return
        self.assertTrue(False)

    def test_get_pub_topic_sd(self):
        # GET /v1/public/events/topics/{topic}
        logger.info('TEST: GET /v1/public/events/topics/{topic}')
        # add your test case
        TEST_TOPIC = None
        for item in self._api.get_pub_topic_sd(TEST_TOPIC):

            self.assertTrue(True)
            return
        self.assertTrue(False)

    def test_get_pub_user_topics(self):
        # GET /v1/public/events/users/{user-id}/topics
        logger.info('TEST: GET /v1/public/events/users/{user-id}/topics')
        # add your test case
        TEST_TOPIC = None
        for item in self._api.get_pub_user_topics(TEST_TOPIC):
            self.assertTrue(True)
            return
        self.assertTrue(False)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
