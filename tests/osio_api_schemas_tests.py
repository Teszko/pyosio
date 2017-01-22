# coding=utf-8

from pyosio.osio import OpenSensorsAPI
import types
import six
import unittest
import logging

logger = logging.getLogger(__name__)


class OSIOAPISchemasTests(unittest.TestCase):

    def setUp(self):
        # add your test case
        USER_ID, API_KEY = None, None
        self._api = OpenSensorsAPI(USER_ID, API_KEY)

    def test_get_schemas(self):
        # GET /v2/schemas
        logger.info('TEST: GET /v2/schemas')
        # add your test case
        TEST_ORG_ID = None
        self.assertNotEqual(self._api.get_schemas(TEST_ORG_ID), None)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
