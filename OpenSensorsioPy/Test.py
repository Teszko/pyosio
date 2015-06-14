from Config import *
from OpenSensorsAPI import *


# create an object 
opensensor = OpenSensorAPI(API_KEY)

print("I am: ")
print opensensor.whoAmI()


print("MY Devices are:")
print opensensor.listDevices()

print ("My Topics are:")
print opensensor.listTopics()

print ("Messages by user:")

print opensensor.getUserMessages({'start-date':'2014-11-24', 'end-date':'2014-11-25'})
print opensensor.getUserMessages({'client':'252','start-date':'2014-11-24'})

print ("Messages by topic:") 
opensensor.getUserMessages('Fablab_test')
