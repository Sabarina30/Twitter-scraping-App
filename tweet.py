import snscrape.modules.twitter as sntwitter
import pandas as pd
import streamlit as st
from pymongo import MongoClient


def df():
    Features = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{result} + since:{start_date} until:{end_date}'
                                                             ).get_items()):
        if i > s1:
            break
        Features.append(
            [tweet.date, tweet.id, tweet.url, tweet.rawContent, tweet.user, tweet.replyCount,
             tweet.retweetCount,
             tweet.lang, tweet.source, tweet.likeCount])
    c = pd.DataFrame(Features,
                     columns=["Date Created", "Email", "URL", "contents", "user_name", "replies",
                              "retweets",
                              "language", "Source of Tweet", "Number of Likes"])
    return c


with st.form('form1'):
    st.header("Twitter Scraping")
    keyword = st.text_input('Looking for?')
    result = keyword.title()
    s1 = st.slider('How many tweets do you want to get?', 1, 100)
    st.write("You Chose", s1)
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    submit_button = st.form_submit_button(label='search')

    if submit_button:
        tweets_df = df()
        st.write(tweets_df)

btn = st.button('upload')
if btn:
    tweets_df = df()
    tweets_df.to_csv('file1.csv')
    data = pd.read_csv('file1.csv')
    client = MongoClient('localhost', 27017)
    db = client["tweets1"]
    collections = db['scrappers']
    data.reset_index(inplace=True)
    data_dict = data.to_dict('records')
    collections.insert_many(data_dict)
    st.write('uploaded to database')

status = st.radio("Choose a file to download: ", ('csv', 'json'))
if status == 'csv':
    tweets_df = df()
    tweets_df.to_csv("csvfile")
    with open('csvfile', 'rb') as file:
        st.download_button(label='download', data=file, file_name='scrapers_tweets.csv')
else:
    tweets_df = df()
    tweets_df.to_json("jsonfile")
    with open('jsonfile', 'rb') as file:
        st.download_button(label='download', data=file, file_name='scrapers_tweets.json')
