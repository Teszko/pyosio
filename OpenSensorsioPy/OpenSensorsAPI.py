import requests


BASE_URL = 'https://opensensors.io/api/1.0'

class OpenSensorAPI():

    def __init__(self, API_KEY, user=None):
        self.user= user
        self.apiKey = API_KEY
        self.headers ={'Authorization':'api-key ' + self.apiKey }

    def connect(self,url):
        ''' Connect to the API
        '''
        try:
            response = requests.get(url,headers=self.headers)
            if response.status_code == requests.codes.ok:
                return response
            else:
                response.raise_for_status()
        except requests.exceptions.ConnectionError as exc:
            print('A Connection error occurred.', exc)

    def whoAmI(self):
        ''' Get User's name
        '''
        url= BASE_URL + "/whoami"
        return self.connect(url).text

    def listDevices(self):
        ''' List all the devices
        '''
        url= BASE_URL + "/users/{}/devices/".format(self.whoAmI())
        return self.connect(url).json()

    def listTopics(self):
        ''' List all the topics
        '''
        url= BASE_URL + "/users/{}/topics/".format(self.whoAmI())
        return self.connect(url).json()

    def createDevice(self):
        ''' Create a new device
        '''
        url= BASE_URL + "/users/{}/devices/".format(self.whoAmI())
        headers = {"Authorization": "api-key {}".format(self.apiKey)}
        try:
            req = requests.post(url, data= {}, headers=headers)
            return req
        except requests.exceptions.ConnectionError as exc:
            print('A Connection error occurred.', exc)

    def getUserMessages(self,parms):
        ''' Find messages published by particular users
            Arguments: start-date, end-date, client, topic
        '''
        url= BASE_URL + "/users/{}/messages-by-owner".format(self.whoAmI())
        try:
            response = requests.get(url,params=parms, headers=self.headers)
            return response.json()
        except requests.exceptions.ConnectionError as exc:
            print('A Connection error occurred.', exc)

    def getUserMsgsByTopic(self,topic):
        ''' 
            get User's Messages Filtered By Topic
            Arguments: start-date, end-date, client, topic
        '''
        url= BASE_URL + "/users/{}/messages-by-topic".format(self.whoAmI())
        parms= {'topic':topic}
        try:
            response = requests.get(url,params=parms, headers=self.headers)
            return response.json()
        except requests.exceptions.ConnectionError as exc:
            print('A Connection error occurred.', exc)





