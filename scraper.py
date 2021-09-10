# Import Necessary Modules
import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup

# Link + Browser Info
start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('chromedriver')
browser.get(start_url)
time.sleep(10)

# Function to Exract Information from Site
def scrape():
    headers = ["Proper name", "Distance (ly)", "Mass (M)", "Radius (R)"]
    star_data = []
    
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    for table_tag in soup.find_all('table', attrs = {'class', 'wikitable sortable jquery-tablesorter'}):
        tbody_tag = table_tag.find_all('tbody')
        for tbody_tag in soup.find_all():
            tr_tag = tbody_tag.find_all('tr')
            for tr_tag in soup.find_all():
                td_tags = tr_tag.find_all('td')
                temp_list = []
                for index, td_tag in enumerate(td_tags):
                    if (index == 0):
                        temp_list.append(td_tag.find_all("a"))
                    else: 
                        try: 
                            temp_list.append(td_tag.contents[0])
                        except:
                            temp_list.append('')

                star_data.append(temp_list)

    with open("brightStars.csv", "w") as f: 
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers) 
        csvwriter.writerows(star_data) 

scrape()