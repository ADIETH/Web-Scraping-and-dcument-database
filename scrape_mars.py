#  import dependencies

from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
#************************************************************************************
#  define browser :chromedriver 
#*********************************************************************************
def init_browser():
    # path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

# NASA Mars News

def mars_news_function():

    browser = init_browser()

   # setting variable to scape NASA Mars News site   '

    url_Mars_News = "https://mars.nasa.gov/news/"

    browser.visit(url_Mars_News)
    time.sleep(1)

    html = browser.html

    soup = bs(html,'html.parser')

    # find news headings 
    article_heading_list = []

    for article_heading in soup.find_all('div',class_="content_title"):
        article_heading_list.append(article_heading.find('a').text)

    # find information about new articles 

    article_details_list = []

    for article_details in soup.find_all('div',class_="article_teaser_body"):
        
        article_details_list.append(article_details.text)


    # setting Varibles for Latest New Articles and Titles

    latest_News_Title = article_heading_list[0]

    latest_News_Details = article_details_list[0]

    News_dict = {"Headline": latest_News_Title,"Details": latest_News_Details}


    return News_dict 

    # ***************************************************************************
    # JPL Mars Space Images - Featured Image
    # ***************************************************************************

def Feature_Image_function():
    
    browser = init_browser()

    url_Mars_Space_Images = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(url_Mars_Space_Images)
    time.sleep(1)

    html = browser.html

    soup = bs(html,'html.parser')


    # find the newest image for this site https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

    featured_image_list = []

    for image in soup.find_all('div',class_="img"):
        featured_image_list.append(image.find('img').get('src'))


    #feature image
    feature_Image = featured_image_list[0]

    #feature image url 
    feature_Image_url = "https://www.jpl.nasa.gov/" + feature_Image

    feature_Image_dict = {"image": feature_Image_url}

    # print feature image ur

    return feature_Image_dict

    # ***************************************************************************
    # Mars Weather
    # ***************************************************************************

def Weather_function():
    
    browser = init_browser()

    # Set Up for Mars Weather

    url_Mars_Weather = "https://twitter.com/marswxreport?lang=en"

    browser.visit(url_Mars_Weather)
    time.sleep(1)

    html = browser.html

    soup = bs(html,'html.parser')

    # Locate Mars Weather
    weather_info_list = []

    for weather_info in soup.find_all('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
        weather_info_list.append(weather_info.text)

    # Variable for latest Mars Information
    Latest_Mars_Weather = weather_info_list[0]

    mars_weather_dict = {"mar_weather": Latest_Mars_Weather }

    return mars_weather_dict


# ***************************************************************************
# Mars Facts
# ***************************************************************************

def Mars_Facts_table_function():
    
     # set dataframe 
    df_Mars_Facts = pd.read_html("https://space-facts.com/mars/")

    df_Mars_Facts = df_Mars_Facts[0]

    df_Mars_Facts.rename({0:"Parameters", 1:"Values"},axis=1, inplace=True)

    # convert data from df to HTML table

    df_Mars_Facts_table = df_Mars_Facts.to_html("Mars_Facts_Table.html")

    df_Mars_Facts_dict = {"df_Mars_Facts": df_Mars_Facts_table}


    return df_Mars_Facts_dict


# ***************************************************************************
# Mars hemisphere
# ***************************************************************************

def hemisphere_images():

    # setting variable
    url_Mars_Hemisperes = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser = init_browser()
    browser.visit(url_Mars_Hemisperes)

    html = browser.html

    soup = bs(html,'html.parser')

    mars_hemisperes_title_list = []

    for img_title in soup.find_all('div',class_="description"):
     mars_hemisperes_title_list.append(img_title.find('h3').text)
        
    mars_hemisphere_image_url = []

    for image in soup.find_all('div',class_="item"):
    
     url = "https://astrogeology.usgs.gov/"
    
    mars_hemisphere_image_url.append(url + image.find('img').get('src'))
    # finding image URL 
    full_image_url = [] 

    for each_url in mars_hemisphere_image_url:
        split_url = each_url.split(".tif_thumb.png")[0]
    
    image_url = split_url + ".tif/full.jpg"
    
    full_image_url.append(image_url)
    
    
    image_one = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    image_two = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    image_three = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    image_four = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'
    
    # Appenin the dictionary with the image url string and the hemisphere title to a list. 

    full_hemisphere_dict = {"image_one": image_one, "image_two":image_two, "image_three":image_three, "image_four":image_four}

    return full_hemisphere_dict

