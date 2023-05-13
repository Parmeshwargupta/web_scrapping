# If you want to scrap a wesite :
# 1. Use API
# 2. HTML Web Scraping using some tool like bs4
# Step 0: install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib
import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"

# Step 1:Get the  HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)
# Step3:HTML Tree traversal
# commonly used types of objects:
# print(type(soup))
# print(type(title))# 1. Tag
# print(type(title.string))# 2. NevigableString
# print(type(soup))# 3. BeautifulSoup
# 4. Comment
# markup = "<p><!--this is a comment--></p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.p.string)
# print(type(soup2.p.string))
# exit()

title = soup.title

# print(title)
# Get the title of the HTML page
paras = soup.find_all('p')
# print(paras)
anchors = soup.find_all('a')
# print(anchors)

# Get first element int he HTML page
print(soup.find('p'))
# Get classes of any element in the HTML page
print(soup.find('p')['class'])
# Get the id of any element of any HTML page
# print(soup.find('p')['id'])
# find all the element with class text-sm
print(soup.find_all('p', class_='text-sm'))
# Get the text from the tags/soup
print(soup.find('p').get_text())

# Get all the text from the HTML page
print(soup.get_text())
# Get the all the links on the page
all_links = set()

for link in anchors:
    if(link.get('href') != '/'):
        link_text = "https://codewithharry.com"+link.get('href')
        all_links.add(link_text)
        print(link_text)
print(all_links)

imgpreview2 = soup.find(id='imgpreview2')
print(imgpreview2.children)
# for item in imgpreview2.children:
#     print(item)
# print(imgpreview2.contents)
# print(imgpreview2)
# for elem in imgpreview2.contents:
#     print(elem)
# for item in imgpreview2.strings:
#     print(item)
# print(imgpreview2.parent)
# print(imgpreview2.patrents)
for item in imgpreview2 .parents:
    # print(item)
    print(item.name)
