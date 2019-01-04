import urllib, requests, os, csv, re, sys, time
import urllib.request, urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver

#main url link
Main_Url = 'https://www.airlinequality.com/review-pages/a-z-airline-reviews/'
driver = webdriver.Firefox(executable_path='C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.get(Main_Url)
Main_Html = driver.execute_script("return document.documentElement.outerHTML")
driver.close()
Sel_Main_Soup = BeautifulSoup(Main_Html,"html.parser")

for container1 in Sel_Main_Soup.find_all(attrs={"class":"items"}):
     if container1.li is None:
         continue
     else:
        for container2 in container1.find_all('a'):
            #Getting all links from the main page
            #print(container2.get('href'))
            Air_Url = urllib.parse.urljoin('https://www.airlinequality.com/review-pages/a-z-airline-reviews/',container2.get('href') + '?sortby=post_date%3ADesc&pagesize=100')
            time.sleep(5)
            driver = webdriver.Firefox(executable_path='C:\Program Files\Mozilla Firefox\geckodriver.exe')
            driver.get(Air_Url)
            Air_Html = driver.execute_script("return document.documentElement.outerHTML")
            driver.close()
            Sel_Air_Soup = BeautifulSoup(Air_Html,"html.parser")

            for container3 in Sel_Air_Soup(attrs={"class":"review-info"}):

                Airline_Name = container3.find('h1').text.strip()

                container5 = container3.find(attrs={"class":"review-count"})
                Num_Reviews = container5.span.text.strip()

                container6 = container3.find(attrs={"class":"rating-10 rating-large"})
                Over_All_Rating = container6.span.text.strip()

                i = 1
                IE = 0
                SC =0
                SS =0
                VM =0
                for container4 in container3.find_all(attrs={"class":"review-rating-stars stars"}):
                    Rating = len(container4.find_all(attrs={"class":"star fill"}))

                    if i == 1:
                        FB = Rating
                        i += 1
                    elif i == 2:
                        IE = Rating
                        i += 1
                    elif i == 3:
                        SC = Rating
                        i += 1
                    elif i == 4:
                        SS = Rating
                        i += 1
                    elif i == 5:
                        VM = Rating
                        i += 1
            x = 0
            Review = []
            j = 0
            for container7 in Sel_Air_Soup.find_all(attrs={"class":"text_content "}):
                if j <= 25:


                    Temp_Review = container7.text.strip()

                    Temp_Review = Temp_Review.replace("✅ Trip Verified | ", "")
                    Temp_Review = Temp_Review.replace("Not Verified | ", "")
                    Temp_Review = Temp_Review.replace("✅ Verified Review |", "")
                    Temp_Review = Temp_Review.replace(",", " ")
                    Temp_Review = Temp_Review.strip()
                    Review.append(Temp_Review)
                    j += 1




            List = [Airline_Name,Over_All_Rating,Num_Reviews,FB,IE,SC,SS,VM,Review]
            print(List)
            with open(os.path.expanduser(r"~/Desktop/670projectdata/data1.csv"),"a",encoding='utf-8') as data_file:
                csv_data = csv.writer(data_file)
                csv_data.writerow(List)
