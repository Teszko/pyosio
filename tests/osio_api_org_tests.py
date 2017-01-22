# coding=utf-8

from pyosio.osio import OpenSensorsAPI
import types
import six
import unittest
import logging

logger = logging.getLogger(__name__)


class OSIOAPIOrgTests(unittest.TestCase):

    def setUp(self):
        # add your test case
        USER_ID, API_KEY = None, None
        self._api = OpenSensorsAPI(USER_ID, API_KEY)

    def test_create_org(self):
        # POST /v1/orgs
        logger.info('TEST: POST /v1/orgs')
        # add your test case
    create_org_input = None
        self.assertNotEquals(self._api.create_org(create_org_input), None)

    def test_update_org(self):
        # PUT /v1/orgs/{org-id}
        logger.info('TEST: PUT /v1/orgs/{org-id}')
        # add your test case
        TEST_ORG_ID = None
        self.assertNotEquals(self._api.update_org(TEST_ORG_ID), False)

    def test_delete_org(self):
        # DELETE /v1/orgs/{org-id}
        logger.info('TEST: DELETE /v1/orgs/{org-id}')
        # add your test case
        TEST_ORG_ID = None
        self.assertNotEquals(self._api.delete_org(TEST_ORG_ID), False)

    def test_get_org_meta(self):
        # GET /v1/orgs/{org-id}
        logger.info('TEST: GET /v1/orgs/{org-id}')
        # add your test case
        TEST_ORG_ID = None
        self.assertNotEquals(self._api.get_org_meta(TEST_ORG_ID), None)

    def test_accept_org_invit(self):
        # PUT /v1/orgs/{org-id}/confirm-membership/{token}
        logger.info('TEST: PUT /v1/orgs/{org-id}/confirm-membership/{token}')
        # add your test case
        TEST_ORG_ID, TOKENS = None, None
        self.assertNotEquals(
            self._api.accept_org_invit(TEST_ORG_ID, TOKENS), None)

    def test_get_org_devices(self):
        # GET /v1/orgs/{org-id}/devices
        logger.info('TEST: GET /v1/orgs/{org-id}/devices')
        # add your test case
        TEST_ORG_ID = None
        self.assertNotEquals(self._api.get_org_devices(TEST_ORG_ID), None)

    def test_get_filtered_org_devices(self):
        # GET /v1/orgs/{org-id}/devices/{batch}/{type}
        logger.info('TEST: GET /v1/orgs/{org-id}/devices/{batch}/{type}')
        # add your test case
        TEST_ORG_ID, d_batch, d_type = None, None, None
        self.assertNotEquals(
            self._api.get_filtered_org_devices(TEST_ORG_ID, d_batch, d_type), None)

    def test_get_org_device_meta(self):
        # GET /v1/orgs/{org-id}/devices/{client-id}
        logger.info('TEST: GET /v1/orgs/{org-id}/devices/{client-id} ')
        # add your test case
        TEST_ORG_ID, TEST_DEVICE_ID = None, None
        self.assertNotEquals(
            self._api.get_org_device_meta(TEST_ORG_ID, TEST_DEVICE_ID), None)

    def test_delete_org_device(self):
        # DELETE /v1/orgs/{org-id}/devices/{client-id}
        logger.info('TEST: DELETE /v1/orgs/{org-id}/devices/{client-id}')
        # add your test case
        TEST_ORG_ID, TEST_DEVICE_ID = None, None
        self.assertNotEquals(
            self._api.delete_org_device(TEST_ORG_ID, TEST_DEVICE_ID), None)

    def test_delete_org_device(self):
        # PUT /v1/orgs/{org-id}/devices/{client-id}
        logger.info('TEST: PUT /v1/orgs/{org-id}/devices/{client-id} ')
        # add your test case
        TEST_ORG_ID, TEST_DEVICE_ID, update_device_input = None, None, None
        self.assertNotEquals(self._api.delete_org_device(
            TEST_ORG_ID, TEST_DEVICE_ID, update_device_input), None)

    def test_get_org_device_errors(self):
        # GET /v1/orgs/{org-id}/errors
        logger.info('TEST: GET /v1/orgs/{org-id}/errors')
        self.assertNotEquals(self._api.get_org_device_errors(), None)

    def test_get_org_pending_invits(self):
        # GET /v1/orgs/{org-id}/invitations
        logger.info('TEST: GET /v1/orgs/{org-id}/invitations')
        self.assertNotEquals(self._api.get_org_pending_invits(), None)

    def test_get_org_members(self):
        # GET /v1/orgs/{org-id}/members
        logger.info('TEST: GET /v1/orgs/{org-id}/members')
        self.assertNotEquals(self._api.get_org_members(), None)

    def test_invite_user_to_org(self):
        # POST /v1/orgs/{org-id}/members/{user-id}
        logger.info('TEST: POST /v1/orgs/{org-id}/members/{user-id}')
        # add your test case
        TEST_ORG_ID, USER_ID = None, None
        self.assertNotEquals(
            self._api.invite_user_to_org(TEST_ORG_ID, USER_ID), None)

    def test_delete_user_from_org(self):
        # DELETE /v1/orgs/{org-id}/members/{user-id}
        logger.info('TEST: DELETE /v1/orgs/{org-id}/members/{user-id} ')
        # add your test case
        TEST_ORG_ID, USER_ID = None, None
        self.assertNotEquals(
            self._api.delete_user_from_org(TEST_ORG_ID, USER_ID), None)

    def test_reinvite_user_to_org(self):
        # POST /v1/orgs/{org-id}/members/invitation-data/{user-id}
        logger.info(
            'TEST: POST /v1/orgs/{org-id}/members/invitation-data/{user-id}')
        self.assertNotEquals(self._api.reinvite_user_to_org(), None)

    def test_get_invit_status(self):
        # GET /v1/orgs/{org-id}/members/invitation-data/{user-id}
        logger.info(
            'TEST: GET /v1/orgs/{org-id}/members/invitation-data/{user-id} ')
        self.assertNotEquals(self._api.get_invit_status(), None)

    def test_get_org_topics(self):
        # GET /v1/orgs/{org-id}/topics
        logger.info('TEST: GET /v1/orgs/{org-id}/topics ')
        self.assertNotEquals(self._api.get_org_topics(), None)

    def test_get_org_stats(self):
        # GET /v1/orgs/{org-id}/usage-stats
        logger.info('TEST: GET /v1/orgs/{org-id}/usage-stats')
        self.assertNotEquals(self._api.get_org_stats(), None)

    def test_get_pub_org_meta(self):
        # GET /v1/public/orgs/{org-id}
        logger.info('TEST: GET /v1/public/orgs/{org-id}')
        # add your test case
        TEST_ORG_ID = None
        self.assertNotEquals(self._api.get_pub_org_meta(TEST_ORG_ID), None)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
