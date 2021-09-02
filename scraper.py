# Import Necessary Modules
import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver


# Link + Browser Info
start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('chromedriver')
browser.get(start_url)
time.sleep(10)

# Function to Exract Information from Site
def scrape():
    headers = ["Proper name", "Distance (ly)", "Mass (M)", "Radius (R)"]
    star_data = []
    
    for i in range(0, 96):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for tr_tag in soup.find_all('tr', attrs = {'class', 'headersort'}):
            td_tags = tr_tag.find_all('td')
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if (index == 0):
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else: 
                    try: 
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append('')

            star_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/tbody/tr[1]').click()

    with open("brightStars.csv", "w") as f: 
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers) 
        csvwriter.writerows(star_data) 
scrape()