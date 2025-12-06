#API is application programming interface , third party services that we write code to talk to 
#many API's live on the internet , code pretends to be browser and connects to that third party API on a server to get data
# for this we have requests package to make web requests as we are browser ourselves 

#for example here we can use itunes , https://itunes.apple.com/search?entity=song&limit=1&term=weezer , here we are searching for a single song by weezer 
#this returns a text to us which is JSON string format we can see that because use of {} and [] and other characters 
# a browser just translates for us this json string 
#write program for python to pretend to be a browser 

import requests
import sys #to give arguments having space use quotes 

if len(sys.argv) != 2: #we are using command line argument here to get from user which artists to search for 
    sys.exit()

response =requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]) #function used to get response from a server , we give url 

#print(response.json()) #response.json is a method object , This executes the method and returns the parsed JSON content.
#here we see that requests lib converts the json to a dictionary which uses the same format as json 

#we can see that its not readable therefore we have a lib to help 
import json

#print(json.dumps(response.json(), indent= 2 )) #just for formatting, indent used in json.dump to indent the response to 2 spaces to right 
#we can see now the dictionaries present clearly and keys in '' and associated values , resultCount is 1 because we limited the response to 1 

#here we can see artistID used by apple to assign a unique id to this artist , we also see trackName : Say it aint so , if we have to find all the tracks we can iterate over this key

o = response.json() #saving the dictionary here 

for result in o["results"]: #in the value with key results , iterate by result over the dictionary and print value at trackName key 
    print(result["trackName"])

