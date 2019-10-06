    #!/usr/bin/env python
    # coding: utf-8

    # Dependencies
import os
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

    # Read HTML from file

filepath = os.path.join(".", "Resources", "News_NASA.html")
with open(filepath,encoding='utf-8') as file:
    html = file.read()

def scrape():

    mars_info = {}

    # Create a Beautiful Soup object
    #soup = bs(html, 'lxml')
    soup = bs(html, 'html.parser')
    type(soup)

    print(soup.prettify())

    news_title = soup.find('div', class_='content_title').find('a').text.strip()
    news_p = soup.find('div', class_='article_teaser_body').find('p').text.strip()
    mars_info["news_title"] = news_title
    mars_info["news_p"] = news_p

    #JPL Mars Space Images - Featured Image
    #As per professor Vikas, using Splinter may disable Python add -ons and this portion should be optional.


    # # Mars Weather
    # #Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # #Use Pandas to convert the data to a HTML table string.

    # In[8]:


    #MarsWeather
    # Read HTML from file
    filepathMWT = os.path.join(".", "Resources", "MarsWeatherTwitter.html")
    with open(filepathMWT,encoding='utf-8') as file:
        htmlMWT = file.read()


    #MarsWeather
    # Create a Beautiful Soup object
    #soup = bs(html, 'lxml')
    soupMWT = bs(htmlMWT, 'html.parser')
    type(soup)


    #MarsWeather
    print(soupMWT.prettify())

    #MarsWeather
    tweets = soupMWT.find_all('div', class_='js-tweet-text-container')

    for tweet in tweets: 
        mars_weather = tweet.find('p').text
        if 'sol' in mars_weather:
            print(mars_weather)
            break
        else: 
            pass

    mars_info["mars_weather"] = mars_weather       


    # # Mars Facts
    # Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # Use Pandas to convert the data to a HTML table string.
    # 

    #MarsFacts
    filepathMF = os.path.join(".", "Resources", "MarsFacts.html")
    with open(filepathMF,encoding='utf-8') as file:
        htmlMF = file.read()


    tables = pd.read_html(filepathMF)
    tables


    df = tables[1]

    df.columns = ['Fact','Value']

    df.set_index('Fact', inplace=True)


    html_table = df.to_html()
    html_table

    html_table.replace('\n', '')


    mdf.to_html('table.html')
    mars_info["fact_table"] = html_table

    return mars_info
