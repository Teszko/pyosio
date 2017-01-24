![MIT license](https://img.shields.io/badge/licence-MIT-blue.svg)
![Stable](https://img.shields.io/badge/status-stable-green.svg)

# pyosio
pyosio: A Python wrapper around OpenSensors.io API
OpenSensors.io is an IOT platform that enables anyone to create real time smart IoT products.

## Getting Started

### Installation
You can install the package via:
```sh
$ pip install git+git://github.com/tzano/pyosio.git
```
Install the dependencies:
```sh
$ pip install -r requirements.txt
```

### Initialization

- Create your account on: https://publisher.opensensors.io/login

- Grab `YOUR_SECRET_KEY` from your Open Sensors account (Account > User Profile > Api Key). `YOUR_USERNAME` is the one you use to login.

- You can store the username/api_key in a file "api_credentials.yml".

```py
from pyosio.osio import OpenSensorsAPI

user_id = ""
api_key = ""

osio_client = OpenSensorsClient(user_id, api_key)

print osio_client.who_am_i()

```
## API Structure

All endpoints follow the structure listed in the official OpenSensors API documentation [https://api.opensensors.io/index.html]. Below, you can find the list of all endpoints together with all the methods that can be used to fetch or post data through this wrapper.

    +- OpenSensors REST API
    |  +- login : Login and retreive a JWT
    |  |  +- who_am_i: Returns the user id associated with the API key or JWT token
    |  |  +- login: Login and retrieve a JWT token
    |  |
    |  +- datasets : Datasets operations
    |  |  +- get_dataset_meta: Get dataset metadata
    |  |  +- get_pub_dataset_meta: Get public dataset information
    |  |
    |  +- messages : Stored messages
    |  |  +- get_device_msgs: Get messages for a given device
    |  |  +- get_topic_msgs: Get messages for a given topic
    |  |  +- get_user_msgs: Get messages for a given user
    |  |  +- get_pub_dataset_msgs: Get messages for a given public dataset
    |  |  +- get_bulk_pub_dataset_msgs: Get messages for a given public dataset
    |  |
    |  +- users : User operations
    |  |  +- get_pub_user_meta: Get public user metadata including topics
    |  |  +- update_user_meta: Update user metadata
    |  |  +- get_user_meta: Get user metadata
    |  |  +- get_api_key: Get API key
    |  |  +- generate_api_key: Generate a new API key
    |  |  +- bookmark_topic: Create a bookmark for a given user and topic
    |  |  +- delete_bookmarked_topic: Delete a bookmark for a given user and topic
    |  |  +- get_user_bookmarks: Get bookmarks associated with a user
    |  |  +- get_user_bookmarks_followers: Get users that bookmarked given users topics
    |  |  +- link_device_user: Associate a device with a user
    |  |  +- get_user_device_errors: Retrieve device errors for a given user
    |  |  +- set_device: Create a new device for a user
    |  |  +- get_user_devices: Get devices associated with a user
    |  |  +- get_device_meta: Get device metadata
    |  |  +- delete_device: Delete a device
    |  |  +- update_device_meta: Update device metadata
    |  |  +- reset_device_passw: Generate a new password for a device
    |  |  +- get_user_devices_info: Get info about the values of multiple devices
    |  |  +- delete_user_devices: Delete devices in bulk
    |  |  +- update_user_bulk_devices: Update multiple devices
    |  |  +- set_user_bulk_devices: Create new devices in bulk 
    |  |  +- get_user_org_invits: Get pending org invitations for a user
    |  |  +- get_user_orgs: Get organisations a user is member of
    |  |  +- delete_user_org: Leave an organisation
    |  |  +- get_user_owned_orgs: Get organisations a user owns
    |  |  +- get_user_topics: Get topics associated with a user
    |  |  +- get_user_stats: Retrieve usage stats for a given user
    |  |  +- get_user_datasets: Get datasets associated with a user
    |  |  +- get_user_devices: Get devices associated with a user
    |  |  +- get_user_topics: Get topics associated with a user
    |  |  +- delete_user_bulk_topics: Bulk delete topics by ids
    |  |
    |  +- orgs : Organisation operations
    |  |  +- create_org: Create an organisation
    |  |  +- update_org: Update organisation metadata
    |  |  +- delete_org: Delete an organisation
    |  |  +- get_org_meta: Get organisation metadata
    |  |  +- accept_org_invit: Accept an organisation invitation
    |  |  +- get_org_devices: Get devices associated with an organisation
    |  |  +- get_filtered_org_devices: Get a device's associated organisation
    |  |  +- get_org_device_meta: Get device metadata
    |  |  +- delete_org_device: Delete a device
    |  |  +- get_org_device_errors: Retrieve device errors for a given org
    |  |  +- get_org_pending_invits: Get pending invitations for an organisation
    |  |  +- get_org_members: Get members of an org
    |  |  +- invite_user_to_org: Invite user to join organisation
    |  |  +- delete_user_from_org: Delete a user from an organisation
    |  |  +- reinvite_user_to_org: Resend an organisation invitation email
    |  |  +- get_invit_status: Get invitation status for organisation and user
    |  |  +- get_org_topics: Get topics associated with an organisation
    |  |  +- get_org_stats: Retrieve usage stats for a given org
    |  |  +- get_pub_org_meta: Get public organisation metadata
    |  |
    |  +- topics : Topic operations
    |  |  +- get_pub_topic_info: Get public topic information
    |  |  +- search_pub_topic_info: Search for public topics 
    |  |  +- set_topic: Create a topic
    |  |  +- delete_topic: Delete a topic
    |  |  +- get_topic_meta: Get topic metadata
    |  |  +- update_topic_meta: Update topic metadata
    |
    + 
    +- OpenSensors Real-Time API
    |  +- events : SSE streams for device & dataset event
    |  |  +- get_device_sd: Opens a SSE stream with debug events for a device
    |  |  +- get_pub_sd: Opens a SSE stream for a public dataset
    |  |
    |  +- events : SSE streams for device & message event
    |  |  +- get_org_topics_sd: Opens a SSE stream for all topics of an org
    |  |  +- get_topics_sd: Opens a SSE stream for a given topic
    |  |  +- get_user_bookmarked_topics_sd: Opens a SSE stream for bookmarked topics
    |  |  +- get_user_topics_sd: Opens a SSE stream for all topics for a user
    |  |  +- get_pub_org_topics_sd: Opens a SSE stream for a org's all public topics
    |  |  +- get_pub_topic_sd: Opens a SSE stream for a public topic
    |  |  +- get_pub_user_topics: Opens a SSE stream for a users' all public topics
    |  |
    |  +- messages : Send messages
    |  |  +- send_msg_topic: Post a message to a topic on behalf of a device
    |  |
    +  +

### Tests
    
To learn how to use the API, you can go through the tests.

    python -m tests.osio_api_login_tests
    python -m tests.osio_api_messages_tests
    python -m tests.osio_api_datasets_tests
    python -m tests.osio_api_users_tests
    python -m tests.osio_api_projects_tests
    python -m tests.osio_api_schemas_tests
    python -m tests.osio_api_topics_tests
    python -m tests.osio_api_org_tests
    python -m tests.osio_realtime_api_tests
    python -m tests.osio_api_projects_tests

## Documentation: 
You can learn more about the system through OSIO's wiki pages.

- [OpenSensors REST API](https://api.opensensors.io/index.html)
- [OpenSensors Real-Time API](https://realtime.opensensors.io/index.html)
- [OpenSensors.io FAQ](https://www.opensensors.io/faq)
- [OpenSensors Open Data community](https://www.opensensors.io/community)
- [OpenSensors Knowledge base](http://support.opensensors.io/support/home)

## Example of Open Public datasets
- [Transport data](https://publisher.opensensors.io/orgs/TFL)
- [Weather data](https://publisher.opensensors.io/orgs/metoffice)
- [Air Quality data](https://opensensors.io/orgs/London-Air-Quality-Network)
- [Worldwide earthquake data](https://publisher.opensensors.io/orgs/EMSC)


## OSIO wrappers written in other languages: 

- rosio: An R interface to OpenSensors.io
https://github.com/lgatto/rosio


## Support

If you are having issues, please let us know or submit a pull request.


## License

The project is licensed under the MIT License.
