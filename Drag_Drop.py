from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# action chains
from selenium.webdriver import ActionChains


class DragAndDrop:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def boot(self):
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def draggable(self, draggable):
        fullXPath = "/html/body/div[1]"
        element = self.driver.find_element(by=By.XPATH, value=fullXPath)
        element.send_keys(draggable)
        sleep(5)

    def droppable(self, droppable):
        fullXPath = "/html/body/div[2]"
        element = self.driver.find_element(by=By.XPATH, value=fullXPath)
        element.send_keys(droppable)
        sleep(5)

    def dragAndDrop(self,draggable):
        try:
            self.boot()
            self.draggable()
            self.droppable()
            self.action.drag_and_drop(draggable, droppable).perform()
            sleep(3)
            fullXPath = "/html/body/div[2]/p"
            droptext = self.driver.find_element(by=By.XPATH, value=fullXPath)
        except  droptext == "Dropped!":
            print("Success")
        else:
            print("Error")

    #except NoSuchElementException as e:
    #print(e)

        finally:
            self.driver.quit()

obj = DragAndDrop("https://jqueryui.com/droppable/")
#obj.dragAndDrop()
