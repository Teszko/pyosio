# coding=utf-8

from pyosio.osio import OpenSensorsAPI
import types
import six
import unittest
import logging


logger = logging.getLogger(__name__)


class OSIOAPIUsersTests(unittest.TestCase):

    def setUp(self):
        # add your test case
        USER_ID, API_KEY = None, None
        self._api = OpenSensorsAPI(USER_ID, API_KEY)

    def test_get_pub_user_meta(self):
        # GET /v1/public/users/{user-id}
        logger.info('TEST: GET /v1/public/users/{user-id}')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_pub_user_meta(USER_ID), None)

    def test_update_user_meta(self):
        # PUT /v1/users/{user-id}
        logger.info('TEST: PUT /v1/users/{user-id}')
        # add your test case
        USER_ID, UpdateUserInput = None, None
        self.assertEquals(
            self._api.update_user_meta(USER_ID, UpdateUserInput), True)

    def test_get_user_meta(self):
        # GET /v1/users/{user-id}
        logger.info('TEST: GET /v1/users/{user-id}')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_user_meta(USER_ID), None)

    def test_get_api_key(self):
        # GET /v1/users/{user-id}/api-key
        logger.info('TEST: GET /v1/users/{user-id}/api-key')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_api_key(USER_ID), None)

    def test_generate_api_key(self):
        # Becareful when u run this one, it will generate new key and disconnect you from the last one
        # POST /v1/users/{user-id}/api-key
        logger.info('TEST: POST /v1/users/{user-id}/api-key')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.generate_api_key(USER_ID), None)

    def test_bookmark_topic(self):
        # PUT /v1/users/{user-id}/bookmark/{topic}
        logger.info('TEST: PUT /v1/users/{user-id}/bookmark/{topic}')
        #topic = '/users/yods/temperature'
        topic = '/users/taharz/test_topic'
        # add your test case
        USER_ID, TEST_TOPIC = None, None
        self.assertEquals(self._api.bookmark_topic(USER_ID, TEST_TOPIC), True)

    def test_delete_bookmarked_topic(self):
        # DELETE /v1/users/{user-id}/bookmark/{topic}
        logger.info('TEST: DELETE /v1/users/{user-id}/bookmark/{topic}')
        # add your test case
        USER_ID, TEST_TOPIC = None, None
        self.assertEquals(
            self._api.delete_bookmarked_topic(USER_ID, TEST_TOPIC), True)

    def test_get_user_bookmarks(self):
        # GET /v1/users/{user-id}/bookmarks
        logger.info('TEST: GET /v1/users/{user-id}/bookmarks')
        # add your test case
        USER_ID = None
        self.assertTrue(
            isinstance(self._api.get_user_bookmarks(USER_ID), list))

    def test_get_user_bookmarks_followers(self):
        # GET /v1/users/{user-id}/bookmarks/followers
        logger.info('TEST: GET /v1/users/{user-id}/bookmarks/followers')
        # add your test case
        USER_ID = None
        self.assertTrue(
            isinstance(self._api.get_user_bookmarks_followers(USER_ID), list))

    def link_device_user(self):
        # PUT /v1/users/{user-id}/claim-device/{client-id}
        logger.info('TEST: PUT /v1/users/{user-id}/claim-device/{client-id}')
        # add your test case
        USER_ID, TEST_TEST_DEVICE_ID = None, None
        self.assertNotEqual(
            self._api.link_device_user(USER_ID, TEST_TEST_DEVICE_ID), False)

    def test_get_user_device_errors(self):
        # GET /v1/users/{user-id}/device-errors
        logger.info('TEST: GET /v1/users/{user-id}/device-errors')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_user_device_errors(USER_ID), None)

    def test_set_device(self):
        # POST /v1/users/{user-id}/devices
        logger.info('TEST: POST /v1/users/{user-id}/devices')
        # add your test case
        USER_ID, create_device_input = None, None
        self.assertNotEqual(
            self._api.set_device(USER_ID, create_device_input), None)

    def test_get_user_devices(self):
        # GET /v1/users/{user-id}/devices
        logger.info('TEST: GET /v2/users/{user-id}/devices')
        self._api._set_version("v2")
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_user_devices(USER_ID), None)

    def test_get_device_meta(self):
        # GET /v1/users/{user-id}/devices/{client-id}
        logger.info('TEST: GET /v1/users/{user-id}/devices/{client-id}')
        # add your test case
        USER_ID, TEST_DEVICE_ID = None, None
        self.assertNotEqual(
            self._api.get_device_meta(USER_ID, TEST_DEVICE_ID), None)

    def test_update_device_meta(self):
        # [non-tested]
        # PUT /v1/users/{user-id}/devices/{client-id}
        logger.info('TEST: PUT /v1/users/{user-id}/devices/{client-id}')
        # add your test case
        USER_ID, update_device_input = None, None
        self.assertNotEqual(self._api.update_device_meta(
            USER_ID, update_device_input["client-id"], update_device_input), False)

    def test_delete_device(self):
        # DELETE /v1/users/{user-id}/devices/{client-id}
        logger.info('TEST: DELETE /v1/users/{user-id}/devices/{client-id}')
        # add your test case
        USER_ID, TEST_DEVICE_ID = None, None
        self.assertNotEqual(
            self._api.delete_device(USER_ID, TEST_DEVICE_ID), False)

    def test_reset_device_passw(self):
        # POST /v1/users/{user-id}/devices/{client-id}/reset-password
        logger.info(
            'TEST: POST /v1/users/{user-id}/devices/{client-id}/reset-password')
        # add your test case
        USER_ID, TEST_DEVICE_ID = None, None
        self.assertNotEqual(
            self._api.reset_device_passw(USER_ID, TEST_DEVICE_ID), None)

    def test_get_user_devices_info(self):
        # GET /v1/users/{user-id}/devices/bulk
        logger.info('TEST: GET /v1/users/{user-id}/devices/bulk')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_user_devices_info(
            USER_ID, queryparams={"all-devices": "true"}), None)

    def test_delete_user_devices(self):
        # DELETE /v1/users/{user-id}/devices/bulk
        logger.info('TEST: DELETE /v1/users/{user-id}/devices/bulk')
        # add your test case
        USER_ID, device_del = None, None
        self.assertNotEqual(
            self._api.delete_user_devices(USER_ID, device_del), None)

    def test_update_user_bulk_devices(self):
        # PUT /v1/users/{user-id}/devices/bulk
        logger.info('TEST: PUT /v1/users/{user-id}/devices/bulk')
        # add your test case
        USER_ID, bulk_update_params_input = None, None
        self.assertNotEqual(
            self._api.update_user_bulk_devices(USER_ID, bulk_update_params_input), False)

    def test_set_user_bulk_devices(self):
        # POST /v1/users/{user-id}/devices/bulk
        logger.info('TEST: POST /v1/users/{user-id}/devices/bulk')
        # add your test case
        USER_ID, new_device = None, None
        self.assertNotEqual(
            self._api.set_user_bulk_devices(USER_ID, new_device), False)

    def test_get_user_org_invits(self):
        # GET /v1/users/{user-id}/invitations
        logger.info('TEST: GET /v1/users/{user-id}/invitations')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_user_org_invits(USER_ID), None)

    def test_get_user_orgs(self):
        # GET /v1/users/{user-id}/orgs
        logger.info('TEST: GET /v1/users/{user-id}/orgs')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_user_orgs(USER_ID), None)

    def test_delete_user_org(self):
        # DELETE /v1/users/{user-id}/orgs/{org-id}
        logger.info('TEST: DELETE /v1/users/{user-id}/orgs/{org-id}')
        # add your test case
        USER_ID, TEST_ORG_ID = None, None
        self.assertNotEqual(
            self._api.delete_user_org(USER_ID, TEST_ORG_ID), None)

    def test_get_user_owned_orgs(self):
        # GET /v1/users/{user-id}/owned-orgs
        logger.info('TEST: GET /v1/users/{user-id}/owned-orgs')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_user_owned_orgs(USER_ID), None)

    def test_get_user_topics(self):
        # GET /v1/users/{user-id}/topics
        logger.info('TEST: GET /v1/users/{user-id}/topics')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_user_topics(USER_ID), None)

    def test_get_user_stats(self):
        # GET /v1/users/{user-id}/usage-stats
        logger.info('TEST: GET /v1/users/{user-id}/usage-stats')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_user_stats(USER_ID), None)

    def test_get_user_datasets(self):
        # GET /v2/users/{user-id}/datasets
        logger.info('TEST: GET /v2/users/{user-id}/datasets')
        self._api._set_version("v2")
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_user_datasets(USER_ID), None)

    def test_get_user_devices(self):
        # GET /v2/users/{user-id}/devices
        logger.info('TEST: GET /v2/users/{user-id}/devices')
        self._api._set_version("v2")
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_user_devices(USER_ID), None)

    def test_get_user_topics(self):
        # GET /v2/users/{user-id}/topics
        logger.info('TEST: GET /v2/users/{user-id}/topics')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.get_user_topics(USER_ID), None)

    def test_delete_user_bulk_topics(self):
        # DELETE /v2/users/{user-id}/topics/bulk
        logger.info('TEST: DELETE /v2/users/{user-id}/topics/bulk')
        # add your test case
        USER_ID = None
        self.assertNotEqual(self._api.delete_user_bulk_topics(USER_ID), False)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
