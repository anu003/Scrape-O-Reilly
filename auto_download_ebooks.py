import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import json

url = raw_input("Enter the O'relley's free ebook url:")#'http://www.oreilly.com/data/free/archive.html?imm_mid=0e7547&cmp=em-data-free-na-stny16_nem4_end_summer'
result = requests.get(url)

# extracting e-book download links
if result.raise_for_status() == 200:
    soup = BeautifulSoup(result.text, 'lxml')
    class_selection = soup.findAll('div', attrs = {'class' : 'product-row cover-showcase'})
    anchor_selection = class_selection.findAll('a')
    ebook_download_links = []
    for anchor in anchor_selection:
        if anchor.has_attr('href'):
            ebook_download_links.append(anchor.get('href'))

# filling the text and clicking the buttons
driver = webdriver.Chrome("/Users/KittusMac/Downloads/chromedriver")
for url in ebook_download_links:
    # opens the url provided by the user
    driver.get(url)
    # user details are stored in a json file
    # find and fill the fields
    element1 = driver.find_element_by_name("first")
    element1.send_keys(user_details["first-name"])
    element2 = driver.find_element_by_name("last")
    element2.send_keys(user_details["last-name"])
    element3 = driver.find_element_by_name("email")
    element3.send_keys(user_details["email-id"]])
    # get free e-books download button
    new_page = driver.find_element_by_name("x-a").click()
    # gets the current url
    downloads_url = driver.current_url
    response = requests.get(downloads_url.encode('utf-8'))
    s = BeautifulSoup(response.text, 'lxml')
    class_selection = s.find('ul', attrs = {'class' : 'formats floatl mb'})
    # Downloads the ebooks to the local downloads folder
    driver.get(class_selection.find('a').get('href'))
