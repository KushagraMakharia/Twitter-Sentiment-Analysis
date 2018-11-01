import tweepy
from textblob import TextBlob
import csv




# Step 1 - Authenticate
consumer_key= ''  #Comsumer Key
consumer_secret= '' #Consumer Secret Key

access_token='' #Access Token
access_token_secret='' #Access Secret Token

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



#Step 2 - Function
def get_label(analysis, threshold = 0):
	if analysis.sentiment[0]>threshold:
		return 'Positive'
	else:
		return 'Negative'

#Step 3 - Retrieve Tweets
public_tweets = api.search('Bohemian Rapsody')




for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

#Step 4 - Make a csv of output
sentiment_polarities = []
with open('Bohemian Rapsody', 'w') as movie_file:
		movie_file.write('tweet,sentiment_label\n')
		for tweet in public_tweets:
			analysis = TextBlob(tweet.text)
			#Get the label corresponding to the sentiment analysis
			sentiment_polarities.append(analysis.sentiment[0])
			movie_file.write('%s,%s\n' % (tweet.text, get_label(analysis)))

        	
