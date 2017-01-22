# coding=utf-8

from pyosio.osio import OpenSensorsAPI
import types
import six
import unittest


class OSIOAPILoginTests(unittest.TestCase):

    def setUp(self):
        # add your test case
        USER_ID, API_KEY = None, None
        self._api = OpenSensorsAPI(USER_ID, API_KEY)

    # ---------------------------------------- #
    # login : Login and retreive a JWT
    # ---------------------------------------- #

    def test_who_am_i_v1(self):
        logger.info('TEST: GET /v1/whoami')
        # add your test case
        USER_ID = None
        self.assertEquals(self._api.who_am_i().get("username"), USER_ID)

    def test_who_am_i_v2(self):
        logger.info('TEST: GET /v2/whoami')
        self._api._set_version("v2")
        # add your test case
        USER_ID = None
        self.assertEquals(self._api.who_am_i().get("username"), USER_ID)

    def test_login(self):
        logger.info('TEST: POST /v2/login')
        self._api._set_version("v2")
        # add your test case
        USER_ID = None
        self.assertNotEquals(self._api.login(username=USER_ID), None)


if __name__ == '__main__':
    unittest.main()
