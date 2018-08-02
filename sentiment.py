from classifier import *
from gql import gql, Client
import graphene
import requests
import json
import time




#////////////////// SENTIMENT ANALYSIS IN SPANISH - TRIAL 1 ////////////////////////
clf = SentimentClassifier()
# x = "maricón, maricón joder, joder, joder, joder, joder"
# print(clf.predict(x))

#///////////////// GraphQl Client ///////////////////////////////////////////////////

url = 'http://localhost:3000/graphql'
json = { "query" : "{allUsers{ username reviews{downvotes upvotes title additionalComments pros cons created company{name}}}}" }
d = requests.post(url=url, json=json).json()

#///////////////////// Getting the Data ////////////////////////////////////////////

users =  d['data']['allUsers']


not_active = []
active = []

for user in users:
	if not user['reviews']:
		not_active.append(user['username'])
	else:
		active.append(user)


for user in active:
	user['number_reviews'] = len(user['reviews'])
	for review in user['reviews']:
		
		# Calculating the 
		review['created'] = int(time.time()) - int(review['created'])//1000
		review['days_from_current'] = review['created']//(60*60*24)

		# Combining the entire text for now
		review['text_total'] = review['title'] + ' ' +  review['pros'] + ' ' + review['cons'] + ' ' + review['additionalComments']
		review['sentiment'] = clf.predict(review['text_total'])
	#print(user['reviews'])


#/////////////////////////////////// SIMILARITY OF TEXT //////////////////////////////////////

print(active)









