from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import sys
from selenium.webdriver.common.by import By
from dataclasses import dataclass
from typing import NoReturn, List

URL: str = "https://docs.google.com/forms/d/e/1FAIpQLSeG_hjjalfPzCFvS_pBT6FYnj5URYeMmCkIooOq0DbXA6LDXg/viewform"

driver: webdriver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))


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
            print("\nSince you went for default, robot will fill form once")
        else:
            runs: int = int(runs)
            print(f"\nRobot will fill form {runs +1 } times\n\n")

        for run in range(runs):

            print("\n*****************************************************")
            print("                                                     ")
            print("AT RUN:", run + 1)
            print("                                                     ")
            print("*****************************************************\n")

            self.browser.get(url)

            allQuestions = self.FindAll(".geS5n")
            print("Total lenght of questions is------", len(allQuestions))
            counter: int = 0

            for eachQuestion in allQuestions:
                print("question at number-----", counter + 1,
                      "Question is ```  ", self.FindAll(".geS5n .M7eMe")[counter].text, "   ```")

                allOptions: List[WebElement] = eachQuestion.find_elements(
                    By.CSS_SELECTOR, ".nWQGrd.zwllIb")

                choice: WebElement = random.choice(allOptions)
                print(
                    f"this question has {len(allOptions)} options, I'll be picking option {allOptions.index(choice) + 1} which is   ``{choice.text}``  \n")
                choice.click()
                time.sleep(3)
                counter += 1

            print("done filling form")
            time.sleep(3)
            self.FindOne(".lRwqcd .NPEfkd").click()
            print("form submitted...")
            time.sleep(4)

        print("\n\n*****************************************************")
        print("BYE!!!...hoped Robot served you well")
        self.browser.quit()
        print("*****************************************************")


go = Scrape()
go(url=URL)
