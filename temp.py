Page_count = (int(Num_Reviews)/10)
                Page_count = round(Page_count)
                if Page_count == 0:
                    Review_Url = urllib.parse.urljoin('https://www.airlinequality.com/review-pages/a-z-airline-reviews/',container2.get('href'))
                    driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')
                    driver.get(Air_Url)
                    Air_Html = driver.execute_script("return document.documentElement.outerHTML")
                    driver.close()
