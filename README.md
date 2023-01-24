# Twitter-scraping-App
Today, data is scattered everywhere in the world. 
Especially in social media, there may be a big quantity of data on Facebook, Instagram, Youtube, Twitter, etc.
1.snscrape
 snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items.By using the “snscrape” Library, Scrape the twitter data from Twitter.snscrape requires Python 3.8 or higher. The Python package dependencies are installed automatically when you install snscrape.
 INSTALLATION:
 pip3 install snscrape
 pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
scrapping data accordingly date, id, url, tweet content, user,reply count, retweet count,language, source, like count.
create dataframe in python with above features.
2.pymongo
PyMongo is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python
Store each collection of data into a document into Mongodb.
3.GUI using streamlit
Streamlit is a Python library that makes building beautiful, interactive apps in a few lines of code easy.
Create a GUI using streamlit that should contain the feature to enter the keyword or Hashtag to be searched, select the date range and limit the tweet count need to be scraped. After scraping, the data needs to be displayed in the page and need a button to upload the data into Database and download the data into csv and json format.
