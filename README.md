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
    |  |  +- who_am_i
    |  |  +- login
    |  |
    |  +- datasets : Datasets operations
    |  |  +- get_dataset_meta
    |  |  +- get_pub_dataset_meta
    |  |
    |  +- messages : Stored messages
    |  |  +- get_device_msgs
    |  |  +- get_topic_msgs
    |  |  +- get_user_msgs
    |  |  +- get_pub_dataset_msgs
    |  |  +- get_bulk_pub_dataset_msgs
    |  |
    |  +- users : User operations
    |  |  +- get_pub_user_meta
    |  |  +- update_user_meta
    |  |  +- get_user_meta
    |  |  +- get_api_key
    |  |  +- generate_api_key
    |  |  +- bookmark_topic
    |  |  +- delete_bookmarked_topic
    |  |  +- get_user_bookmarks
    |  |  +- get_user_bookmarks_followers
    |  |  +- link_device_user
    |  |  +- get_user_device_errors
    |  |  +- set_device
    |  |  +- get_user_devices
    |  |  +- get_device_meta
    |  |  +- delete_device
    |  |  +- update_device_meta
    |  |  +- reset_device_passw
    |  |  +- get_user_devices_info
    |  |  +- delete_user_devices
    |  |  +- update_user_bulk_devices
    |  |  +- set_user_bulk_devices
    |  |  +- get_user_org_invits
    |  |  +- get_user_orgs
    |  |  +- delete_user_org
    |  |  +- get_user_owned_orgs
    |  |  +- get_user_topics
    |  |  +- get_user_stats
    |  |  +- get_user_datasets
    |  |  +- get_user_devices
    |  |  +- get_user_topics
    |  |  +- delete_user_bulk_topics
    |  |
    |  +- orgs : Organisation operations
    |  |  +- create_org
    |  |  +- update_org
    |  |  +- delete_org
    |  |  +- get_org_meta
    |  |  +- accept_org_invit
    |  |  +- get_org_devices
    |  |  +- get_filtered_org_devices
    |  |  +- get_org_device_meta
    |  |  +- delete_org_device
    |  |  +- get_org_device_errors
    |  |  +- get_org_pending_invits
    |  |  +- get_org_members
    |  |  +- invite_user_to_org:
    |  |  +- delete_user_from_org
    |  |  +- reinvite_user_to_org
    |  |  +- get_invit_status
    |  |  +- get_org_topics
    |  |  +- get_org_stats
    |  |  +- get_pub_org_meta
    |  |
    |  +- topics : Topic operations
    |  |  +- get_pub_topic_info
    |  |  +- search_pub_topic_info
    |  |  +- set_topic
    |  |  +- delete_topic
    |  |  +- get_topic_meta
    |  |  +- update_topic_meta
    |  +
    + 
    +- OpenSensors Real-Time API
    |  +- events : SSE streams for device & dataset event
    |  |  +- get_device_sd
    |  |  +- get_pub_sd
    |  |
    |  +- events : SSE streams for device & message event
    |  |  +- get_org_topics_sd
    |  |  +- get_topics_sd
    |  |  +- get_user_bookmarked_topics_sd
    |  |  +- get_user_topics_sd
    |  |  +- get_pub_org_topics_sd
    |  |  +- get_pub_topic_sd
    |  |  +- get_pub_user_topics 
    |  |
    |  +- messages : Send messages
    |  |  +- send_msg_topic
    +  +

### Tests
    
To test the endpoints of the API, you can go through the tests. Please, note that you need to include your own faked data when you test the methods. 
```sh
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
```

## API Endpoints
You can find below the list of all API endpoints to fetch data from Open Sensors API.

### OpenSensors REST API
#### Login : Login and retreive a JWT
- Returns the user id associated with the API key or JWT token
```python
osio_client.who_am_i()
```  
- Login and retrieve a JWT token [NO-AUTH]
```python
osio_client.login(user_id='', password='')
```  
#### Datasets : Datasets operations
- Get dataset metadata
```python
osio_client.get_dataset_meta(dataset_id='')
```  
- Get public dataset information [NO-AUTH]
```python
osio_client.get_pub_dataset_meta(dataset_id='')
```  
#### Messages : Stored messages
- Get messages for a given device
```python
osio_client.get_device_msgs(client_id='', queryparams={})
```  
- Get messages for a given topic
```python
osio_client.get_topic_msgs(topic='', queryparams={})
```  
- Get messages for a given user
```python
osio_client.get_user_msgs(user_id='', queryparams={})
```  
- Get messages for a given public dataset [NO-AUTH]
```python
osio_client.get_pub_dataset_msgs(dataset_id='', queryparams={})
``` 
-  Get messages for a given public dataset [NO-AUTH]
```python
osio_client.get_bulk_pub_dataset_msgs(dataset_msgs_bulk_input={})
``` 
#### Users : User operations
- Get public user metadata including topics [NO-AUTH]
```python
osio_client.get_pub_user_meta(user_id='')
``` 
- Update user metadata
```python
osio_client.update_user_meta(user_id='', data={})
``` 
- Get user metadata
```python
osio_client.get_user_meta(user_id='')
``` 
- Get API key
```python
osio_client.get_api_key(user_id='')
``` 
- Generate a new API key
```python
osio_client.generate_api_key(user_id='')
``` 
- Create a bookmark for a given user and topic
```python
osio_client.bookmark_topic(user_id='', topic='')
``` 
- Delete a bookmark for a given user and topic
```python    
osio_client.delete_bookmarked_topic(user_id='', topic='')
``` 
- Get bookmarks associated with a user
```python  
osio_client.get_user_bookmarks(user_id='')
``` 
- Get users that bookmarked any of a given users topics
```python 
osio_client.get_user_bookmarks_followers(user_id='')
``` 
- Associate a device with a user, user joins the device creator s organisation
```python 
osio_client.link_device_user(user_id='', client_id='')
``` 
- Retrieve device errors for a given user
```python 
osio_client.get_user_device_errors(user_id='')
``` 
- Create a new device for a user
```python 
osio_client.set_device(user_id='', create_device_input={})
``` 
- Get devices associated with a user
```python 
osio_client.get_user_devices(user_id=''):
``` 
- Get device metadata
```python 
osio_client.get_device_meta(user_id='', client_id='', queryparams={})
``` 
- Delete a device
```python 
osio_client.delete_device(user_id='', client_id='')
``` 
- Update device metadata
```python 
osio_client.update_device_meta(user_id='', client_id='', update_device_input={})
``` 
- Generate a new password for a device
```python 
osio_client.reset_device_passw(user_id='', client_id='')
``` 
- Get information about the values of multiple devices with one call
```python 
osio_client.get_user_devices_info(user_id='', queryparams={})
``` 
- Delete devices in bulk (all in one transaction)
```python
osio_client.delete_user_devices(user_id='', device_del={})
``` 
- Update the description, tags and location of multiple devices with one call]
```python
osio_client.update_user_bulk_devices(user_id='', bulk_update_params_input={})
``` 
- Create new devices in bulk (all in one transaction)
```python
osio_client.set_user_bulk_devices(user_id='', new_device={})
``` 
- Get pending org invitations for a user
```python
osio_client.get_user_org_invits(user_id='')
``` 
- Get organisations a user is member of
```python
osio_client.get_user_orgs(user_id='')
``` 
- Leave an organisation (stop being a member)
```python
osio_client.delete_user_org(user_id='', org_id='')
``` 
- Get organisations a user owns
```python
osio_client.get_user_owned_orgs(user_id='')
``` 
- Get topics associated with a user
```python
osio_client.get_user_topics(user_id='')
``` 
- Retrieve usage stats for a given user
```python
osio_client.get_user_stats(user_id='')
``` 
- Get datasets associated with a user
```python
osio_client.get_user_datasets(user_id='')
``` 
- Get devices associated with a user
```python
osio_client.get_user_devices(user_id='')
```
- Get topics associated with a user
```python
osio_client.get_user_topics(user_id='')
```
- Bulk delete topics by ids
```python
osio_client.delete_user_bulk_topics(user_id='')
```
#### Orgs : Organisation operations
- Create an organisation
```python
osio_client.create_org(create_org_input={})
```
- Update organisation metadata
```python
osio_client.update_org(org_id='')
```
- Delete an organisation. Be careful! This is will also delete devices and topics
```python
osio_client.delete_org(org_id='')
```
- Get organisation metadata
```python
osio_client.get_org_meta(org_id='')
```
- Accept an organisation invitation
```python
osio_client.accept_org_invit(org_id='', tokens={})
```
- Get devices associated with an organisation
```python    
osio_client.get_org_devices(org_id='')
```
- Get a device s associated organisation with a given batch and type
```python
osio_client.get_filtered_org_devices(org_id='', d_batch={}, d_type={})
```
- Get device metadata
```python
osio_client.get_org_device_meta(org_id='', client_id='')
```
- Delete a device
```python
osio_client.delete_org_device(org_id='', client_id='')
```
- Update device metadata
```python
osio_client.update_org_device(org_id='', client_id='', update_device_input={})
```
- Retrieve device errors for a given org
```python
osio_client.get_org_device_errors(org_id='')
```
- Get pending invitations for an organisation
```python
osio_client.get_org_pending_invits(org_id='')
```
- Get members of an org
```python
osio_client.get_org_members(org_id='')
```
- Invite user to join organisation (email will be sent)
```python
osio_client.invite_user_to_org(org_id='', user_id='')
```
- Delete a user from an organisation
```python
osio_client.delete_user_from_org(org_id='', user_id='')
```
- Resend an organisation invitation email
```python
osio_client.reinvite_user_to_org(org_id='', user_id='')
```
- Get invitation status for organisation and user
```python
osio_client.get_invit_status(org_id='', user_id='')
```
- Get topics associated with an organisation
```python
osio_client.get_org_topics(org_id='')
```
- Retrieve usage stats for a given org
```python
osio_client.get_org_stats(org_id='')
```
- Get public organisation metadata including topics [NO-AUTH]
```python
osio_client.get_pub_org_meta(org_id='')
```
### Schemas : Schema operations
- Get all the available schemas that can be applied to topics [NO-AUTH]
```python
osio_client.get_schemas(org_id='')
```
#### Topics : Topic operations

- Get public topic information [NO-AUTH]
```python
osio_client.get_pub_topic_info(topic='')
```
- Search for public topics [NO-AUTH]
```python
osio_client.search_pub_topic_info(topic='')
```
- Create a topic
```python
osio_client.set_topic(new_topic_input={})
```
- Delete a topic
```python
osio_client.delete_topic(topic='')
```
- Get topic metadata
```python
osio_client.get_topic_meta(topic='')
```
- Update topic metadata
```python
osio_client.update_topic_meta(topic='', topic_input={})
```
### Projects : Project operations
- Get public project information [NO-AUTH]
```python
osio_client.get_pub_proj_info(project_id='')
```
- Get public datasets for a given project [NO-AUTH]
```python
osio_client.get_pub_datasets(project_id='')
```
### OpenSensors Real-Time API
#### Events : SSE streams for device & dataset event

- Opens a SSE stream with debug events for a device
```python
osio_client.get_device_sd(client_id='')
```
- Opens a SSE stream for a public dataset [NO-AUTH]
```python
osio_client.get_pub_sd(dataset_id='')
```
#### Events : SSE streams for device & message event
- Opens a SSE stream for all topics of an organisation
```python
osio_client.get_org_topics_sd(org_id='')
```
- Opens a SSE stream for a given topic
```python
osio_client.get_topics_sd(topic='')
```
- Opens a SSE stream for bookmarked topics for a user
```python
osio_client.get_user_bookmarked_topics_sd(user_id='')
```
- Opens a SSE stream for all topics for a user
```python
osio_client.get_user_topics_sd(user_id='')
```
- Opens a SSE stream for a organisations' all public topics [NO-AUTH]
```python
    osio_client.get_pub_org_topics_sd(org_id='')
```
- Opens a SSE stream for a public topic [NO-AUTH]
```python
    osio_client.get_pub_topic_sd(topic='')
```
- Opens a SSE stream for a users' all public topics [NO-AUTH]
```python
    osio_client.get_pub_user_topics(user_id='')
```
#### Messages : Send messages
- Post a message to a topic on behalf of a device
```python
osio_client.send_msg_topic(topic=''):
```

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
