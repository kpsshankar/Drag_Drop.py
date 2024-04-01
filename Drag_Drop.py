import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service




url = "https://jqueryui.com/droppable/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.switch_to.frame(driver.find_element(by=By.TAG_NAME, value="iframe"))


actions = ActionChains(driver)
actions.drag_and_drop(driver.find_element(by=By.ID, value="draggable"), driver.find_element(by=By.ID, value="droppable")).perform()
time.sleep(3)
driver.quit()
