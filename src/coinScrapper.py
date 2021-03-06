from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "C:/Users/Lenovo LEGION/Desktop/chromedriver.exe"


class Scrapper:
    def __init__(self, currency_name):
        self.currency_name = currency_name

    def scrap_articles(self):
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        link = f"https://coinmarketcap.com/currencies/{self.currency_name}/news"
        driver.get(link)
        paragraphs = []
        for num in range(1, 6):
            if num != 3:
                paragraph = driver.find_element(By.XPATH, f'/html/body/div/div[1]/div/div[2]/div/div[3]/div/div/main/'
                                                          f'div[2]/div[{num}]/a/div[1]/p').text
                paragraphs.append(paragraph)
        driver.quit()
        return paragraphs
