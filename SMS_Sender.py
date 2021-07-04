## Initializing Depedancies

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException  
import pandas as pd

## Function to check wether a particular element exists 
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

## Loading Chrome Driver
driver = webdriver.Chrome(executable_path=r"chromedriver.exe")

## Loading Whatsapp Web
driver.get("https://messages.google.com/web/authentication?redirected=true")

wait_for_verification = input()

sleep(2)

names_list = ["9176684086" ,"9962055580","73585 79588","98845 20487"]

for name in names_list:
    start_chat_button = driver.find_element_by_xpath("/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/div/mw-fab-link/a")
    start_chat_button.click()

    sleep(1)

    search_for_chat = driver.find_element_by_xpath("/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/mw-new-conversation-sub-header/div/div[2]/mw-contact-chips-input/div/mat-chip-list/div/input")
    search_for_chat.send_keys(name)
    search_for_chat.send_keys("\n")

    sleep(1)

    send_text = driver.find_element_by_xpath("/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-message-compose/div/div[2]/div/mws-autosize-textarea/textarea")
    send_text.send_keys("Hey there,")
    send_text.send_keys(Keys.SHIFT, "\n")
    send_text.send_keys("Apologies for interrupting your day. We are a group of students who have put forward an initiative to make receiving and donating blood an easier process. We wanted to help during these difficult times in the smallest way we could, and we would love your help in doing so.")
    send_text.send_keys(Keys.SHIFT, "\n")
    send_text.send_keys(Keys.SHIFT, "\n")
    send_text.send_keys("If you could confirm the following details below you could be saving a life:")
    send_text.send_keys(Keys.SHIFT, "\n")
    send_text.send_keys(Keys.SHIFT, "\n")
    send_text.send_keys("-> *Your Blood Group is: {}*".format(name[1]))
    send_text.send_keys(Keys.SHIFT, "\n")
    send_text.send_keys("-> *Your are currently in: {}*".format(name[4]))
    send_text.send_keys(Keys.SHIFT, "\n")
    send_text.send_keys("-> *You are still a donor*" )
    send_text.send_keys(Keys.SHIFT, "\n")
    send_text.send_keys(Keys.SHIFT, "\n")
    send_text.send_keys("If the above mentioned details are correct reply with a *YES*" )
    send_text.send_keys(Keys.SHIFT, "\n")
    send_text.send_keys("If any of the details are not correct reply with *WRONG* " )
    send_text.send_keys(Keys.SHIFT, "\n")
    send_text.send_keys("If you are no longer a donor reply with a *NO* " )
    send_text.send_keys(Keys.SHIFT, "\n")
    send_text.send_keys(Keys.SHIFT, "\n")
    send_text.send_keys("P.S: this is an automated message, if you have any queries or doubts feel free to email us at blodindia@gmail.com" )
    send_text.send_keys("\n")
    sleep(1)


