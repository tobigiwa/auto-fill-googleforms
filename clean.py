from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.common.by import By
from dataclasses import dataclass
from typing import NoReturn, List

URL: str = "https://docs.google.com/forms/d/e/1FAIpQLSeG_hjjalfPzCFvS_pBT6FYnj5URYeMmCkIooOq0DbXA6LDXg/viewform"

chrome_options = Options()
chrome_options.add_argument("--headless")

driver: webdriver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options)


@dataclass
class Scrape:
    """ 
    The class need to be instantiated, the task of scrapping is defined in
    it __call__() method. Invoke the instance as a function and pass the URL.
    """

    browser: WebDriver = driver

    def FindOne(self, locator: str, strategy: WebDriver = By.CSS_SELECTOR) -> WebElement:
        "Call to selenium.WebDriver.remote.webelement.WebElement.find_element()"
        return self.browser.find_element(strategy, locator)

    def FindAll(self, locator: str, strategy: webdriver = By.CSS_SELECTOR) -> List[WebElement]:
        "Call to selenium.webdriver.remote.webelement.WebElement.find_elements()"
        return self.browser.find_elements(strategy, locator)

    def __call__(self, url: str) -> NoReturn:
        runs: str = input(
            "HOW MANY TIMES WOULD YOU LIKE TO FILL THIS FORM, PRESS ENTER FOR DEFAULT(ONCE):")
        if runs == "" or runs is None:
            runs: int = 1
        else:
            runs: int = int(runs)

        for run in range(runs):

            print("\n*****************************************************")
            print("AT RUN:", run + 1)
            print("*****************************************************\n")

            self.browser.get(url)

            allQuestions = self.FindAll(".geS5n")
            counter: int = 0

            for eachQuestion in allQuestions:

                allOptions: List[WebElement] = eachQuestion.find_elements(
                    By.CSS_SELECTOR, ".nWQGrd.zwllIb")

                choice: WebElement = random.choice(allOptions)
                choice.click()
                time.sleep(0.4)
                counter += 1

            time.sleep(0.4)
            self.FindOne(".lRwqcd .NPEfkd").click()  # click submit

            print("*****************************************************")
            print("RUN:", run + 1, "COMPLETED")
            print("*****************************************************\n")
            time.sleep(1.2)

        print("\n\n*****************************************************")
        print("BYE!!!...hoped Robot served you well")
        self.browser.quit()
        print("*****************************************************")


go = Scrape()
go(url=URL)
