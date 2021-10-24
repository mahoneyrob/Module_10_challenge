#!/usr/bin/env python
# coding: utf-8




# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd




executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)





# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)





html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')




slide_elem.find('div', class_='content_title')





# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title





# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images



# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)





# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()





# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')





# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel





# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url





df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df





df.to_html()





# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)
html = browser.html
img_soup = soup(html, 'html.parser')

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
# Create lists to hold images names and urls
i_names = []
t_urls = []
h_urls = []

# Find image names and put in i_names
img_names = img_soup.find_all('div', class_="collapsible results")
names = img_names[0].find_all('h3')

for name in names:
    i_names.append(name.text)

# Find image urls from thumbnails
thumbnails = img_names[0].find_all('a')
for thumbnail in thumbnails:
    
    thumbnail_url = 'https://marshemispheres.com/' + thumbnail['href']
    #get unique urls
    if (thumbnail_url not in t_urls):
        
        t_urls.append(thumbnail_url)


# 3. Write code to retrieve the image urls and titles for each hemisphere.

for url in t_urls:
    
    # Click through each thumbanil link
    browser.visit(url)
    
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    # Get url with jpg
    new_url = img_soup.find_all('img', class_='wide-image')
    img_url = new_url[0]['src']
    
    hemi_url = 'https://marshemispheres.com/' + img_url
    h_urls.append(img_link)

# put in hemisphere list

for i in range(len(i_names)):
    hemisphere_image_urls.append({'img_url': h_urls[i], 'title': i_names[i]})




# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls





# 5. Quit the browser
browser.quit()







