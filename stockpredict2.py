import tweepy
from textblob import TextBlob
import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

consumer_key = 'ucVkfDer70ELRO4cp15ur6V4X'
consumer_secret = 'd4QUIzpVcczKy6iusoxOlWLVXoRkMITK3J09YjxYItJpTpHwkv'

access_token = '1214363690-LNW6RmZVxpqCTnK0qAK2Wr64ZntFoUGhCJzF43w'
access_token_secret = '5U7NwxHvQq51gQ6vE8c3PaOnTQgRK3yg3mla2zbylAnFi'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Dow Jones')

pos_tweet = 0
neg_tweet = 0
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity > 0:
        pos_tweet += 1
    else:
        neg_tweet += 1

    if pos_tweet > neg_tweet:
        print("Positive Overall")
    else:
        print("Negative Overall")

dates = []
prices = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
    return

get_data('DOW.csv')

def create_datasets(dates, prices):
    train_size = int(len(dates) * 0.67)
    train_x, train_y = [], []
    test_x, test_y = [], []
    cntr = 0
    for date in dates:
        if cntr<train_size:
            train_x.append(date)
        else:
            test_x.append(date)
    for price in prices:
        if cntr<train_size:
            train_y.append(price)
        else:
            test_y.append(price)
    
    return train_x,train_y,test_x,test_y




def predict_prices(dates, prices, x):
    train_x, train_y, test_x, test_y = create_datasets(dates, prices)
    
    train_x = np.reshape(train_x,(len(train_x),1))
    train_y = np.reshape(train_y,(len(train_y),1))
    test_x = np.reshape(test_x,(len(test_x),1))
    test_y = np.reshape(test_y,(len(test_y),1))

    model=Sequential()
    model.add(Dense(32,input_dim=1,kernel_initializer='random_uniform',activation='relu'))
    model.add(Dense(32,input_dim=1,kernel_initializer='random_uniform',activation='relu'))
    model.add(Dense(16,kernel_initializer='random_uniform',activation='relu'))
    
    model.add(Dense(1,kernel_initializer='random_uniform',activation='relu'))
    model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])
    model.fit(train_x,train_y,epochs=100,batch_size=3,verbose=1)

predicted_price = predict_prices(dates, prices, 2)
print(predicted_price)