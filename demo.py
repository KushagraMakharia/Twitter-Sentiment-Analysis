import tweepy
from textblob import TextBlob
import csv


# Step 1 - Authenticate
consumer_key= 'CONSUMER_KEY'
consumer_secret= 'CONSUMER_SECRET_KEY'

access_token='ACCESS_TOKEN_KEY'
access_token_secret='ACCESS_TOKEN_SECRET_KEY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')
infile = 'file.csv'




#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

with open(infile, 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        sentence = row[0]
        blob = TextBlob(sentence)
        print ('sentence')
       	if(analysis.sentiment.polarity > 0.5):
       		print ("positive")
       	else:
       		print("negative")
        	
