import requests
import logging
import json
import getpass
from errors import *
from sseclient import SSEClient

# Handle library reorganisation Python 2 > Python 3.
try:
    from urllib.parse import urljoin
    from urllib.parse import urlencode
except ImportError:
    from urlparse import urljoin
    from urllib import urlencode


class OpenSensorsAPI():

    """
        OpenSensorsAPI class to communicate with OpenSensors Real-Time/REST API
        
        Documentation:
        - OpenSensors REST API
        https://api.opensensors.io/index.html

        - OpenSensors Real-Time API
        https://realtime.opensensors.io/index.html

        - OpenSensors Open Data community
        https://www.opensensors.io/community

        - OpenSensors Knowledge base
        http://support.opensensors.io/support/home

    """
    DEFAULT_DEBUG = True
    DEFAULT_TIMEOUT = 10
    DEFAULT_API_BASE_URL = 'https://api.opensensors.io/'
    DEFAULT_REALTIME_API_URL = 'https://realtime.opensensors.io/'
    DEFAULT_VERSIONS = ['v1', 'v2']

    def __init__(self, user_id, api_key, version='v1'):
        """
                Initialize the class with you user_id and secret_key.

                :param user_id: OpenSensors user id
                :type user_id: :py:class:`str`

                :param api_key: OpenSensors secret key
                :type api_key: :py:class:`str`

                :param version: Version of Open Sensors API
                :type version: :py:class:`str`

                """

        self.user_id = user_id
        self.api_key = api_key
        self.version = version
        self.base_url = self.DEFAULT_API_BASE_URL
        self.realtime_base_url = self.DEFAULT_REALTIME_API_URL
        self._headers = {"Content-Type": "application/json", "Accept": "application/json",
                         'Authorization': 'api-key ' + self.api_key,
                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
        self.logger = logging.getLogger(__name__).setLevel(logging.INFO)

    # ---------------------------------------- #
    # SETers/GETers
    # ---------------------------------------- #

    def _set_version(self, version):
        """
                Set the used version

                :param version: Version of the API.
                :type version: :py:class:`str`

                """
        if version in self.DEFAULT_VERSIONS:
            self.version = version
        else:
            self.logger.warn('Invalid API version')

    # ---------------------------------------- #
    # CRUD Handlers: GET, POST, DELETE, PUT
    # ---------------------------------------- #

    def _get(self, url, supported_versions, **queryparams):
        """
                Handle authenticated GET requests

                :param url: The url for the endpoint including path parameters
                :type url: :py:class:`str`

                :param supported_versions: list of supported versions through this API endpoint.
                :type supported_versions: :py:class:`list`

                :param queryparams: The query string parameters
                :returns: The Reponse from the API
                """

        if self.version in supported_versions:
            url = urljoin(self.base_url, url)
            try:
                response = requests.get(
                    url, headers=self._headers, params=queryparams)

                return response

            except requests.exceptions.RequestException as e:
                raise OSIOClientApiError(
                    'Invalid API server response.\n%s' % response)

        else:
            raise OSIOClientApiError(
                'Version %s is not supported. \n' % self.version)

        return None

    def _get_pub(self, url, supported_versions, **queryparams):
        """
                Handle public GET requests

                :param url: The url for the endpoint including path parameters
                :type url: :py:class:`str`

                :param supported_versions: list of supported versions through this API endpoint.
                :type supported_versions: :py:class:`list`

                :param queryparams: The query string parameters
                :returns: The Reponse from the API
                """
        if self.version in supported_versions:
            url = urljoin(self.base_url, url)
            try:
                response = requests.get(url, params=queryparams)

                return response

            except requests.exceptions.RequestException as e:
                raise OSIOClientApiError(
                    'Invalid API server response.\n%s' % response)

        else:
            raise OSIOClientApiError(
                'Version %s is not supported. \n' % self.version)

        return None

    def _get_stream_data(self, url, supported_versions, **queryparams):
        """
                Handle authenticated GET requests to get streams of data

                :param url: The url for the endpoint including path parameters
                :type url: :py:class:`str`

                :param supported_versions: list of supported versions through this API endpoint.
                :type supported_versions: :py:class:`list`

                :param queryparams: The query string parameters

                :returns: The Reponse from the API
                """

        if self.version in supported_versions:
            url = urljoin(self.realtime_base_url, url)
            try:
                response = requests.get(
                    url, headers=self._headers, params=queryparams, stream=True)

                for line in response:
                    print line
                    if line:
                        try:
                            yield json.loads(line.decode('utf8'))
                        except ValueError as e:
                            pass
            except requests.exceptions.RequestException as e:
                raise OSIOClientApiError(
                    'Invalid API server response.\n%s' % response)

        else:
            raise OSIOClientApiError(
                'Version %s is not supported. \n' % self.version)

    def _get_stream_events(self, url, supported_versions, **queryparams):
        """
                Handle authenticated GET requests to get streams of events using SSEClient

                :param url: The url for the endpoint including path parameters
                :type url: :py:class:`str`

                :param supported_versions: list of supported versions through this API endpoint.
                :type supported_versions: :py:class:`list`

                :param queryparams: The query string parameters

                :returns: The Reponse from the API
                """

        if self.version in supported_versions:
            url = urljoin(self.realtime_base_url, url)
            try:
                # add key to parameters
                queryparams['api-key'] = self.api_key
                response = requests.get(
                    url, headers=self._headers, params=queryparams, stream=True)

                for item in SSEClient(response.url):
                    yield json.loads(str(item.data).encode('utf-8'))

            except requests.exceptions.RequestException as e:
                raise OSIOClientApiError(
                    'Invalid API server response.\n%s' % response)

        else:
            raise OSIOClientApiError(
                'Version %s is not supported. \n' % self.version)

    def _post(self, url, supported_versions, data=None):
        """
                Handle authenticated POST requests

                :param url: The url for the endpoint including path parameters
                :type url: :py:class:`str`

                :param supported_versions: list of supported versions through this API endpoint.
                :type supported_versions: :py:class:`list`

                :param data: The request body parameters
                :type data: :py:data:`none` or :py:class:`dict`

                :returns: The Reponse from the API or an error message
                """
        if self.version in supported_versions:
            url = urljoin(self.base_url, url)
            try:

                if data != None:
                    response = requests.post(
                        url, headers=self._headers, json=data)

                else:
                    response = requests.post(url, headers=self._headers)

                return response

            except requests.exceptions.RequestException as e:
                raise OSIOClientApiError(
                    'Invalid API server response.\n%s' % response)
        else:
            raise OSIOClientApiError(
                'Version %s is not supported. \n' % self.version)

        return None

    def _delete(self, url, supported_versions, data=None):
        """
                Handle authenticated DELETE requests

                :param url: The url for the endpoint including path parameters
                :type url: :py:class:`str`

                :param supported_versions: list of supported versions through this API endpoint.
                :type supported_versions: :py:class:`list`

                :returns: The Reponse from the API
                """
        if self.version in supported_versions:
            url = urljoin(self.base_url, url)
            try:

                if data != None:
                    response = requests.delete(
                        url, headers=self._headers, json=data)
                else:
                    response = requests.delete(url, headers=self._headers)

                return response

            except requests.exceptions.RequestException as e:
                raise OSIOClientApiError(
                    'Invalid API server response.\n%s' % response)
        else:
            raise OSIOClientApiError(
                'Version %s is not supported. \n' % self.version)

        return None

    def _patch(self, url, supported_versions, data=None):
        """
                Handle authenticated PATCH requests

                :param url: The url for the endpoint including path parameters
                :type url: :py:class:`str`

                :param supported_versions: list of supported versions through this API endpoint.
                :type supported_versions: :py:class:`list`

                :param data: The request body parameters
                :type data: :py:data:`none` or :py:class:`dict`

                :returns: The Reponse from the API
                """
        if self.version in supported_versions:
            url = urljoin(self.base_url, url)
            try:
                response = requests.patch(
                    url, headers=self._headers, json=data)
                return response
            except requests.exceptions.RequestException as e:
                raise OSIOClientApiError(
                    'Invalid API server response.\n%s' % response)
        else:
            raise OSIOClientApiError(
                'Version %s is not supported. \n' % self.version)

        return None

    def _put(self, url, supported_versions, data=None):
        """
                Handle authenticated PUT requests

                :param url: The url for the endpoint including path parameters
                :type url: :py:class:`str`

                :param supported_versions: list of supported versions through this API endpoint.
                :type supported_versions: :py:class:`list`

                :param data: The request body parameters
                :type data: :py:data:`none` or :py:class:`dict`

                :returns: The Reponse from the API
                """
        if self.version in supported_versions:
            url = urljoin(self.base_url, url)
            try:

                response = requests.put(url, headers=self._headers, json=data)

                return response

            # if response.status_code in [200,204,422]:
            #   return True
            # else:
            #   return False

            except requests.exceptions.RequestException as e:
                raise OSIOClientApiError(
                    'Invalid API server response.\n%s' % response.text)
        else:
            raise OSIOClientApiError(
                'Version %s is not supported. \n' % self.version)

    def _get_json(self, response):
        """
                :param response: Requests response

                :returns: The json file
                """
        if response.status_code in [200, 204, 422, 500]:
            return response.json()
        else:
            return None

    # ---------------------------------------- #
    # OpenSensors REST API
    # api.opensensors.io
    # ---------------------------------------- #

    # ---------------------------------------- #
    # [v2] datasets : Datasets operations
    # ---------------------------------------- #

    def get_dataset_meta(self, dataset_id):
        """
                Get dataset metadata
                GET /v2/datasets/{dataset-id}

                :param dataset_id: The unique id for the dataset.
                :type dataset_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/datasets/{}".format(self.version, dataset_id)
        response = self._get(url, ["v2"])

        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_pub_dataset_meta(self, dataset_id):
        """
                Get public dataset information [NO-AUTH]
                GET /v2/public/datasets/{dataset-id}

                :param dataset_id: The unique id for the dataset.
                :type dataset_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/datasets/{}".format(self.version, dataset_id)
        response = self._get(url, ["v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    # ---------------------------------------- #
    # [v1/v2] login : Login and retreive a JWT
    # ---------------------------------------- #

    def who_am_i(self):
        """
                Returns the user id associated with the API key or JWT token
                GET /v*/whoami

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/whoami".format(self.version)
        response = self._get(url, ["v1", "v2"]).text

        if self.version == "v1":
            return {"username": response}
        else:
            return json.JSONDecoder().decode(response)

    def login(self, user_id, password=None):
        """
                Login and retrieve a JWT token [NO-AUTH]
                POST /v2/login

                :param user_id: The unique id for the user.
                :type user_id: :py:class:`str`

                :param password: password, this will be entered through getpass package.
                :type password: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        if not password:
            password = getpass.getpass(
                "Enter your password to login into OpenSensorIO: ")  # use getpass to get passwd without echoing it back

        credentials_input = {"username": user_id, "password": password}
        url = "/{}/login".format(self.version)
        response = self._post(url, ["v1", "v2"], data=credentials_input)
        if self.version == "v1":
            return response.json()
        else:
            return response.json()

    # ---------------------------------------- #
    # [v1/v2] messages : Stored messages
    # ---------------------------------------- #

    def get_device_msgs(self, client_id, queryparams={}):
        """
                Get messages for a given device
                GET /v1/messages/device/{client-id}

                :param client_id: The unique id for the device.
                :type client_id: :py:class:`str`

                :param queryparams: The query string parameters
                queryparams = { user-id: string,
                                                radius: long,
                                                postcode: string,
                                                tags: string,
                                                end-date: string,
                                                zip: string,
                                                lat: double,
                                                start-date: string,
                                                elevation: double,
                                                lon: double,
                                                dur: double }

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/messages/device/{}".format(self.version, client_id)
        response = self._get(url, ["v1"], **queryparams)
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_topic_msgs(self, topic, queryparams={}):
        """
                Get messages for a given topic
                GET /v1/messages/topic/{topic}

                :param topic: The unique id for the interest topic.
                :type topic: :py:class:`str`

                :param queryparams: The query string parameters
                queryparams = { user-id: string,
                                                radius: long,
                                                postcode: string,
                                                tags: string,
                                                end-date: string,
                                                zip: string,
                                                lat: double,
                                                start-date: string,
                                                elevation: double,
                                                lon: double,
                                                dur: double }

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/messages/topic/{}".format(self.version, topic)
        response = self._get(url, ["v1"], **queryparams)
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_user_msgs(self, user_id, queryparams={}):
        """
                Get messages for a given user
                GET /v1/messages/user/{user-id}

                :param user_id: User id
                :type user_id: :py:class:`str`

                :param queryparams: The query string parameters
                queryparams = { user-id: string,
                                                radius: long,
                                                postcode: string,
                                                tags: string,
                                                end-date: string,
                                                zip: string,
                                                lat: double,
                                                start-date: string,
                                                elevation: double,
                                                lon: double,
                                                dur: double }

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/messages/user/{}".format(self.version, user_id)
        response = self._get(url, ["v1"], **queryparams)

        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_pub_dataset_msgs(self, dataset_id, queryparams={}):
        """
                Get messages for a given public dataset [NO-AUTH]
                GET /v2/public/messages/dataset/{dataset-id}

                :param dataset_id: The unique id for the dataset.
                :type dataset_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/messages/dataset/{}".format(self.version, dataset_id)
        response = self._get(url, ["v1", "v2"], **queryparams)
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_bulk_pub_dataset_msgs(self, dataset_msgs_bulk_input):
        """
                Get messages for a given public dataset [NO-AUTH]
                POST /v2/public/messages/dataset/bulk

                :param dataset_msgs_bulk_input: bulk input
                :type dataset_msgs_bulk_input: :py:class:`dict`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/messages/dataset/{}".format(self.version, bulk)
        response = self._post(url, ["v2"], dataset_msgs_bulk_input)
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    # ---------------------------------------- #
    # [v1/v2] users : User operations
    # ---------------------------------------- #

    def get_pub_user_meta(self, user_id):
        """
                Get public user metadata including topics [NO-AUTH]
                GET /v1/public/users/{user-id}

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/public/users/{}".format(self.version, user_id)
        response = self._get_pub(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def update_user_meta(self, user_id, data):
        """
                Update user metadata
                PUT /v1/users/{user-id}

                :param user_id: User id
                :type user_id: :py:class:`str`

                param data: metadata
                :type data: :py:class:`dict`
                data = {
                          "name": "string*",
                          "email": "string*",
                          "password": "string*"
                        }

                :returns: The JSON output from the API or an error message
                """

        url = "/{}/users/{}".format(self.version, user_id)
        response = self._put(url, ["v1"], data)
        return True if response.status_code in [200, 204, 422] else False

    def get_user_meta(self, user_id):
        """
                Get user metadata
                GET /v1/users/{user-id}

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}".format(self.version, user_id)
        response = self._get(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_api_key(self, user_id):
        """
                Get API key
                GET /v1/users/{user-id}/api-key

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/api-key".format(self.version, user_id)
        response = self._get(url, ["v1"])
        return response.text if response else response

    def generate_api_key(self, user_id):
        """
                Generate a new API key
                POST /v1/users/{user-id}/api-key

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """

        url = "/{}/users/{}/api-key".format(self.version, user_id)
        response = self._post(url, ["v1"])
        return response.text if response else response

    def bookmark_topic(self, user_id, topic):
        """
                Create a bookmark for a given user and topic
                PUT /v1/users/{user-id}/bookmark/{topic}

                :param user_id: User id
                :type user_id: :py:class:`str`

                :param topic: The unique id for the interest topic.
                :type topic: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """

        url = "/{}/users/{}/bookmark/{}".format(self.version, user_id, topic)
        response = self._put(url, ["v1"])

        return True if response.status_code in [200, 204, 422] else False

    def delete_bookmarked_topic(self, user_id, topic):
        """
                Delete a bookmark for a given user and topic
                DELETE /v1/users/{user-id}/bookmark/{topic}

                :param user_id: User id
                :type user_id: :py:class:`str`

                :param topic: The unique id for the interest topic.
                :type topic: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/bookmark/{}".format(self.version, user_id, topic)
        response = self._delete(url, ["v1"])
        return True if response.status_code in [200, 204, 422] else False

    def get_user_bookmarks(self, user_id):
        """
                Get bookmarks associated with a user
                GET /v1/users/{user-id}/bookmarks

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/bookmarks".format(self.version, user_id)
        response = self._get(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_user_bookmarks_followers(self, user_id):
        """
                Get users that bookmarked any of a given users topics
                GET /v1/users/{user-id}/bookmarks/followers

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/bookmarks/followers".format(self.version, user_id)
        response = self._get(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def link_device_user(self, user_id, client_id):
        """
                Associate a device with a user, user joins the device creator s organisation
                PUT /v1/users/{user-id}/claim-device/{client-id}

                :param user_id: User id
                :type user_id: :py:class:`str`

                :param client_id: The unique id for the device.
                :type client_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/claim-device/{}".format(
            self.version, user_id, client_id)
        response = self._put(url, ["v1"])
        return True if response.status_code in [200, 204, 422] else False

    def get_user_device_errors(self, user_id):
        """
                Retrieve device errors for a given user
                GET /v1/users/{user-id}/device-errors

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/device-errors".format(self.version, user_id)
        response = self._get(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def set_device(self, user_id, create_device_input):
        """
                Create a new device for a user
                POST /v1/users/{user-id}/devices

                :param user_id: User id
                :type user_id: :py:class:`str`

                param create_device_input: device metadata
                :type create_device_input: :py:class:`dict`

                create_device_input = {
                        "description": "string",
                        "tags": [
                                "string"
                        ],
                        "locked-password": true,
                        "client-id": "string",
                        "password": "string",
                        "name": "string",
                        "org-id": "string",
                        "batch": "string",
                        "device-type": "string",
                        "location": {
                                "lat": 0,
                                "lon": 0,
                                "elevation": 0,
                                "zip": "string",
                                "postcode": "string"
                        }
                }

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/devices".format(self.version, user_id)
        response = self._post(url, ["v1"], create_device_input)
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_user_devices(self, user_id):
        """
                Get devices associated with a user
                GET /v1/users/{user-id}/devices

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/devices".format(self.version, user_id)
        response = self._get(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_device_meta(self, user_id, client_id, queryparams):
        """
                Get device metadata
                GET /v1/users/{user-id}/devices/{client-id}

                :param client_id: The unique id for the device.
                :type client_id: :py:class:`str`

                :param user_id: User id
                :type user_id: :py:class:`str`

                :param queryparams: The query string parameters

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/devices/{}".format(
            self.version, user_id, client_id)

        response = self._get(url, ["v1"], **queryparams)
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def delete_device(self, user_id, client_id):
        """
                Delete a device
                DELETE /v1/users/{user-id}/devices/{client-id}

                :param client_id: The unique id for the device.
                :type client_id: :py:class:`str`

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/devices/{}".format(
            self.version, user_id, client_id)
        response = self._delete(url, ["v1"])
        return True if response.status_code in [200, 204, 422] else False

    def update_device_meta(self, user_id, client_id, update_device_input):
        """
                Update device metadata
                PUT /v1/users/{user-id}/devices/{client-id}

                :param client_id: The unique id for the device.
                :type client_id: :py:class:`str`

                :param user_id: User id
                :type user_id: :py:class:`str`

                param update_device_input: device metadata
                :type update_device_input: :py:class:`dict`

                update_device_input = {
                        "name": "string",
                        "description": "string",
                        "batch": "string",
                        "device-type": "string",
                        "location": {
                                "lat": 0,
                                "lon": 0,
                                "elevation": 0,
                                "zip": "string",
                                "postcode": "string"
                        },
                        "tags": [
                                "string"
                        ]
                }

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/devices/{}".format(
            self.version, user_id, client_id)
        response = self._put(url, ["v1"], update_device_input)

        return True if response.status_code in [200, 204, 422] else False

    def reset_device_passw(self, user_id, client_id):
        """
                Generate a new password for a device
                POST /v1/users/{user-id}/devices/{client-id}/reset-password

                :param user_id: User id
                :type user_id: :py:class:`str`

                :param client_id: The unique id for the device.
                :type client_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/devices/{}/reset-password".format(
            self.version, user_id, client_id)
        response = self._post(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_user_devices_info(self, user_id, queryparams={}):
        """
                Get information about the values of multiple devices with one call
                GET /v1/users/{user-id}/devices/bulk

                :param user_id: User id
                :type user_id: :py:class:`str`

                :param queryparams: The query string parameters

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/devices/bulk".format(self.version, user_id)
        response = self._get(url, ["v1"], **queryparams)

        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def delete_user_devices(self, user_id, device_del):
        """
                Delete devices in bulk (all in one transaction)
                DELETE /v1/users/{user-id}/devices/bulk

                :param user_id: User id
                :type user_id: :py:class:`str`

                param device: device meta
                :type device: :py:class:`dict`


                device = [
                  {
                        "client-id": "string"
                  }
                ]

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/devices/bulk".format(self.version, user_id)
        response = self._delete(url, ["v1"], device_del)
        return True if response.status_code in [200, 204, 422] else False

    def update_user_bulk_devices(self, user_id, bulk_update_params_input):
        """
                Update the description, tags and location of multiple devices with one call]
                PUT /v1/users/{user-id}/devices/bulk

                :param user_id: User id
                :type user_id: :py:class:`str`

                param bulk_update_params_input: metadata
                :type bulk_update_params_input: :py:class:`dict`

                bulk_update_params_input = {
                  "all-devices": true,
                  "devices": [
                        "string"
                  ],
                  "values": {
                        "description": "string",
                        "description-various": true,
                        "tags": [
                          "string"
                        ],
                        "tags-various": true,
                        "location": {
                          "lat": 0,
                          "lon": 0
                        },
                        "location-various": true
                  }
                }

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/devices/bulk".format(self.version, user_id)
        response = self._put(url, ["v1"], bulk_update_params_input)
        return True if response.status_code in [200, 204, 422] else False

    def set_user_bulk_devices(self, user_id, new_device):
        """
                Create new devices in bulk (all in one transaction)
                POST /v1/users/{user-id}/devices/bulk

                :param user_id: User id
                :type user_id: :py:class:`str`

                param new_device: metadata
                :type new_device: :py:class:`dict`

                new_device = [
                        {
                                "description": "string",
                                "tags": [
                                  "string"
                                ],
                                "locked-password": true,
                                "client-id": "string",
                                "password": "string",
                                "name": "string",
                                "org-id": "string",
                                "batch": "string",
                                "device-type": "string",
                                "location": {
                                  "lat": 0,
                                  "lon": 0,
                                  "elevation": 0,
                                  "zip": "string",
                                  "postcode": "string"
                                }
                        }
                ]

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/devices/bulk".format(self.version, user_id)
        response = self._post(url, ["v1"], new_device)
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_user_org_invits(self, user_id):
        """
                Get pending org invitations for a user
                GET /v1/users/{user-id}/invitations

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/invitations".format(self.version, user_id)
        response = self._get(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_user_orgs(self, user_id):
        """"
                Get organisations a user is member of
                GET /v1/users/{user-id}/orgs

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/orgs".format(self.version, user_id)
        response = self._get(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def delete_user_org(self, user_id, org_id):
        """
                Leave an organisation (stop being a member)
                DELETE /v1/users/{user-id}/orgs/{org-id}

                :param user_id: User id
                :type user_id: :py:class:`str`

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/orgs/{}".format(self.version, user_id, org_id)
        response = self._delete(url, ["v1"])
        return True if response.status_code in [200, 204, 422] else False

    def get_user_owned_orgs(self, user_id):
        """
                Get organisations a user owns
                GET /v1/users/{user-id}/owned-orgs

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/owned-orgs".format(self.version, user_id)
        response = self._get(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_user_topics(self, user_id):
        """
                Get topics associated with a user
                GET /v1/users/{user-id}/topics

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/topics".format(self.version, user_id)
        response = self._get(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_user_stats(self, user_id):
        """
                Retrieve usage stats for a given user
                GET /v1/users/{user-id}/usage-stats

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/usage-stats".format(self.version, user_id)
        response = self._get(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_user_datasets(self, user_id):
        """
                Get datasets associated with a user
                GET /v2/users/{user-id}/datasets

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/datasets".format(self.version, user_id)
        response = self._get(url, ["v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_user_devices(self, user_id):
        """
                Get devices associated with a user
                GET /v2/users/{user-id}/devices

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/devices".format(self.version, user_id)
        response = self._get(url, ["v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_user_topics(self, user_id):
        """
                Get topics associated with a user
                GET /v2/users/{user-id}/topics

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/topics".format(self.version, user_id)
        response = self._get(url, ["v2", "v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def delete_user_bulk_topics(self, user_id):
        """
                Bulk delete topics by ids
                DELETE /v2/users/{user-id}/topics/bulk

                :param user_id: User id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/users/{}/topics/bulk".format(self.version, user_id)
        response = self._get(url, ["v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    # ---------------------------------------- #
    # [v1/v2] topics : Topic operations
    # ---------------------------------------- #

    def get_pub_topic_info(self, topic):
        """
                Get public topic information [NO-AUTH]
                GET /v1/public/topics/{topic}

                :param topic: The unique id for the interest topic.
                :type topic: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/public/topics/{}".format(self.version, topic)
        response = self._get(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def search_pub_topic_info(self, topic):
        """
                Search for public topics [NO-AUTH]
                GET /v1/search/topics/{term}

                :param topic: The unique id for the interest topic.
                :type topic: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/search/topics/{}".format(self.version, topic)
        response = self._get(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def set_topic(self, new_topic_input):
        """
                Create a topic
                POST /v*/topics

                create_topic_input {
                  "topic": "string",
                  "name": "string",
                  "description": "string",
                  "public": true,
                  "topic-info": {
                        "format": "string"
                  },
                  "schema-id": 0,
                  "rollups-enabled": true
                }

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/topics".format(self.version)
        response = self._post(url, ["v1"], new_topic_input)
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def delete_topic(self, topic):
        """
                Delete a topic
                DELETE /v1/topics/{topic}

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/topics/{}".format(self.version, topic)
        response = self._delete(url, ["v1"])
        return True if response.status_code in [200, 204, 422] else False

    def get_topic_meta(self, topic):
        """
                Get topic metadata
                GET /v1/topics/{topic}

                :param topic: The unique id for the interest topic.
                :type topic: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/topics/{}".format(self.version, topic)
        response = self._get(url, ["v1"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def update_topic_meta(self, topic, topic_input):
        """
                Update topic metadata
                PUT /v*/topics/{topic}

                :param topic: The unique id for the interest topic.
                :type topic: :py:class:`str`

                {
                  "name": "string",
                  "topic-info": {
                        "format": "string"
                  },
                  "description": "string",
                  "public": true,
                  "rollups-enabled": true,
                  "schema-id": 0
                }

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/topics/{}".format(self.version, topic)
        response = self._put(url, ["v1", "v2"], topic_input)
        return True if response.status_code in [200, 204, 422] else False

    # ---------------------------------------- #
    # [v1/v2] orgs : Organisation operations
    # ---------------------------------------- #

    def create_org(self, create_org_input):
        """
                Create an organisation
                POST /v1/orgs

                {
                  "id": "string",
                  "name": "string",
                  "website": "string",
                  "description": "string",
                  "email": "string"
                }

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs".format(self.version)
        response = self._post(url, ["v1", "v2"], create_org_input)
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def update_org(self, org_id):
        """
                Update organisation metadata
                PUT /v1/orgs/{org-id}

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}".format(self.version, org_id)
        response = self._put(url, ["v1", "v2"], create_org_input)
        return True if response.status_code in [200, 204, 422] else False

    def delete_org(self, org_id):
        """
                Delete an organisation. Be careful! This is will also delete devices and topics
                DELETE /v1/orgs/{org-id}

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """

        url = "/{}/orgs/{}".format(self.version, org_id)
        response = self._delete(url, ["v1", "v2"])
        return True if response.status_code in [200, 204, 422] else False

    def get_org_meta(self, org_id):
        """
                Get organisation metadata
                GET /v1/orgs/{org-id}

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}".format(self.version, org_id)
        response = self._get(url, ["v1", "v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def accept_org_invit(self, org_id, tokens):
        """
                Accept an organisation invitation
                PUT /v1/orgs/{org-id}/confirm-membership/{token}

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/confirm-membership/{}".format(
            self.version, org_id, tokens)
        response = self._get(url, ["v1", "v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_org_devices(self, org_id):
        """
                Get devices associated with an organisation
                GET /v1/orgs/{org-id}/devices

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/devices".format(self.version, org_id)
        response = self._get(url, ["v1", "v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_filtered_org_devices(self, org_id, d_batch, d_type):
        """
                Get a device s associated organisation with a given batch and type
                GET /v1/orgs/{org-id}/devices/{batch}/{type}

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/devices/{}/{}".format(
            self.version, org_id, d_batch, d_type)
        response = self._get(url, ["v1", "v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_org_device_meta(self, org_id, client_id):
        """
                Get device metadata
                GET /v1/orgs/{org-id}/devices/{client-id}

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :param client_id: The unique id for the device.
                :type client_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/devices/{}".format(self.version, org_id, client_id)
        response = self._get(url, ["v1", "v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def delete_org_device(self, org_id, client_id):
        """
                Delete a device
                DELETE /v1/orgs/{org-id}/devices/{client-id}

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :param client_id: The unique id for the device.
                :type client_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/devices/{}".format(self.version, org_id, client_id)
        response = self._delete(url, ["v1", "v2"])
        return True if response.status_code in [200, 204, 422] else False

    def delete_org_device(self, org_id, client_id, update_device_input):
        """
                Update device metadata
                PUT /v1/orgs/{org-id}/devices/{client-id}

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :param client_id: The unique id for the device.
                :type client_id: :py:class:`str`

                update_device_input = {
                  "name": "string",
                  "description": "string",
                  "batch": "string",
                  "device-type": "string",
                  "location": {
                        "lat": 0,
                        "lon": 0,
                        "elevation": 0,
                        "zip": "string",
                        "postcode": "string"
                  },
                  "tags": [
                        "string"
                  ]
                }

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/devices/{}".format(self.version, org_id, client_id)
        response = self._put(url, update_device_input)
        return True if response.status_code in [200, 204, 422] else False

    def get_org_device_errors(self, org_id):
        """
                Retrieve device errors for a given org
                GET /v1/orgs/{org-id}/errors

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/errors".format(self.version, org_id)
        response = self._get(url, ["v1", "v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_org_pending_invits(self, org_id):
        """
                Get pending invitations for an organisation
                GET /v1/orgs/{org-id}/invitations

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/invitations".format(self.version, org_id)
        response = self._get(url, ["v1", "v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_org_members(self, org_id):
        """
                Get members of an org
                GET /v1/orgs/{org-id}/members

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/members".format(self.version, org_id)
        response = self._get(url, ["v1", "v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def invite_user_to_org(self, org_id, user_id):
        """
                Invite user to join organisation (email will be sent)
                POST /v1/orgs/{org-id}/members/{user-id}

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :param user_id: user id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/members/{}".format(self.version, org_id, user_id)
        response = self._post(url, ["v1", "v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def delete_user_from_org(self, org_id, user_id):
        """
                Delete a user from an organisation
                DELETE /v1/orgs/{org-id}/members/{user-id}

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :param user_id: user id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/members/{}".format(self.version, org_id, user_id)
        response = self._delete(url, ["v1", "v2"])
        return True if response.status_code in [200, 204, 422] else False

    def reinvite_user_to_org(self, org_id, user_id):
        """
                Resend an organisation invitation email
                POST /v1/orgs/{org-id}/members/invitation-data/{user-id}

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :param user_id: user id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """

        url = "/{}/orgs/{}/members/invitation-data/{}".format(
            self.version, org_id, user_id)
        response = self._post(url, ["v1", "v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_invit_status(self, org_id, user_id):
        """
                Get invitation status for organisation and user
                GET /v1/orgs/{org-id}/members/invitation-data/{user-id}

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :param user_id: user id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/members/invitation-data/{}".format(
            self.version, org_id, user_id)
        response = self._get(url)
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_org_topics(self, org_id):
        """
                Get topics associated with an organisation
                GET /v1/orgs/{org-id}/topics

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/topics".format(self.version, org_id)
        response = self._get(url, ["v1", "v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_org_stats(self, org_id):
        """
                Retrieve usage stats for a given org
                GET /v1/orgs/{org-id}/usage-stats

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/orgs/{}/usage-stats".format(self.version, org_id)
        response = self._get(url, ["v1", "v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_pub_org_meta(self, org_id):
        """
                Get public organisation metadata including topics [NO-AUTH]
                GET /v1/public/orgs/{org-id}

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/public/orgs/{}".format(self.version, org_id)
        response = self._get(url, ["v1", "v2"])
        return response

    # ---------------------------------------- #
    # [v2] schemas : Schema operations
    # ---------------------------------------- #
    def get_schemas(self, org_id):
        """
                Get all the available schemas that can be applied to topics [NO-AUTH]
                GET /v2/schemas

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/public/orgs/{}".format(self.version, org_id)
        response = self._get(url, ["v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    # ---------------------------------------- #
    # [v2] projects : Project operations
    # ---------------------------------------- #

    def get_pub_proj_info(self, project_id):
        """
                Get public project information [NO-AUTH]
                GET /v2/public/projects/{project-id}

                :param project_id: The unique id for the project.
                :type project_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/public/projects/{}".format(self.version, project_id)
        response = self._get(url, ["v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    def get_pub_datasets(self, project_id):
        """
                Get public datasets for a given project [NO-AUTH]
                GET /v2/public/projects/{project-id}/datasets

                :param project_id: The unique id for the project.
                :type project_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/public/projects/{}/datasets".format(
            self.version, project_id)
        response = self._get(url, ["v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None

    # ---------------------------------------- #
    # OpenSensors Real-Time API
    # realtime.opensensors.io
    # ---------------------------------------- #

    # ---------------------------------------- #
    # [v2] events : SSE streams for device & dataset event
    # ---------------------------------------- #
    def get_device_sd(self, client_id):
        """
                Opens a SSE stream with debug events for a device
                GET /v2/debug-events/{client-id}

                :param client_id: The unique id for the device.
                :type client_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/debug-events/{}".format(self.version, client_id)
        response = self._get_stream_events(url, ["v1", "v2"])
        return response

    def get_pub_sd(self, dataset_id):
        """
                Opens a SSE stream for a public dataset [NO-AUTH]
                GET /v2/public/events/datasets/{dataset-id}

                :param dataset_id: The unique id for the dataset.
                :type dataset_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/public/events/datasets/{}".format(self.version, dataset_id)
        response = self._get_stream_events(url, ["v2"])
        return response

    # ---------------------------------------- #
    # events : SSE streams for device & message event
    # ---------------------------------------- #

    def get_org_topics_sd(self, org_id):
        """
                Opens a SSE stream for all topics of an organisation
                GET /v1/events/orgs/{org-id}/topics

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/events/orgs/{}/topics".format(self.version, org_id)
        response = self._get_stream_events(url, ["v1", "v2"])

        return response

    def get_topics_sd(self, topic):
        """
                Opens a SSE stream for a given topic
                GET /v1/events/topics/{topic}

                :param topic: The unique id for the interest topic.
                :type topic: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/events/topics/{}".format(self.version, topic)
        response = self._get_stream_events(url, ["v1", "v2"])
        return response

    def get_user_bookmarked_topics_sd(self, user_id):
        """
                Opens a SSE stream for bookmarked topics for a user
                GET /v1/events/users/{user-id}/bookmarks

                :param user_id: user id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/events/users/{}/bookmarks".format(self.version, user_id)
        response = self._get_stream_events(url, ["v1", "v2"])
        return response

    def get_user_topics_sd(self, user_id):
        """
                Opens a SSE stream for all topics for a user
                GET /v1/events/users/{user-id}/topics

                :param user_id: user id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/events/users/{}/topics".format(self.version, user_id)
        response = self._get_stream_events(url, ["v1", "v2"])
        return response

    def get_pub_org_topics_sd(self, org_id):
        """
                Opens a SSE stream for a organisations' all public topics [NO-AUTH]
                GET /v1/public/events/orgs/{org-id}/topics

                :param org_id: The unique id for the organization.
                :type org_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/public/events/orgs/{}/topics".format(self.version, org_id)
        response = self._get_stream_events(url, ["v1", "v2"])

        return response

    def get_pub_topic_sd(self, topic):
        """
                Opens a SSE stream for a public topic [NO-AUTH]
                GET /v1/public/events/topics/{topic}

                :param topic: The unique id for the interest topic.
                :type topic: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """

        url = "/{}/public/events/topics/{}".format(self.version, topic)

        response = self._get_stream_events(url, ["v1", "v2"])
        return response

    def get_pub_user_topics(self, user_id):
        """
                Opens a SSE stream for a users' all public topics [NO-AUTH]
                GET /v1/public/events/users/{user-id}/topics

                :param user_id: user id
                :type user_id: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/public/events/users/{}/topics".format(self.version, user_id)
        response = self._get_stream_events(url, ["v1", "v2"])
        return response

    # ---------------------------------------- #
    # messages : Send messages
    # ---------------------------------------- #
    def send_msg_topic(self, topic):
        """
                Post a message to a topic on behalf of a device
                POST /v1/topics/{topic}

                :param topic: The unique id for the interest topic.
                :type topic: :py:class:`str`

                :returns: The JSON output from the API or an error message
                """
        url = "/{}/topics/{}".format(self.version, topic)
        response = self._post(url, ["v1", "v2"])
        return response.json() if response.status_code in [200, 204, 422, 500] else None
