# coding=utf-8

from pyosio.osio import OpenSensorsAPI
import types
import six
import unittest
import logging


logger = logging.getLogger(__name__)


class OSIOAPIDatasetsTests(unittest.TestCase):

    def setUp(self):
        # add your test case
        USER_ID, API_KEY = None, None
        self._api = OpenSensorsAPI(USER_ID, API_KEY)

    def test_get_dataset_meta(self):
        # GET /v2/datasets/{dataset-id}
        logger.info('TEST: GET /v2/datasets/{dataset-id}')
        self._api._set_version("v2")  # switch to v2
        # specifiy test object
        TEST_DATASET = None
        self.assertNotEqual(
            self._api.get_dataset_meta(dataset_id=TEST_DATASET), None)

    def test_get_pub_dataset_meta(self):
        # GET /v2/public/datasets/{dataset-id}
        logger.info('TEST: GET /v2/public/datasets/{dataset-id} ')
        self._api._set_version("v2")  # switch to v2
        # specifiy test object
        TEST_DATASET = None
        self.assertNotEqual(
            self._api.get_pub_dataset_meta(dataset_id=TEST_DATASET), None)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
