## Initializing Depedancies
from selenium import webdriver
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
driver.get("https://messages.google.com/web/authentication")

#names_list = ["9176684086" ,"9962055580","73585 79588","98845 20487"]
names_list = ["8838210069"]

# donorData = pd.read_csv(r"Final_Data.csv")
# names_list = [list(row) for row in donorData.values]
# print(names_list)

wait_for_verification = input()
sleep(2)

for name in names_list:
    start_chat_button = driver.find_element_by_xpath("/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/div/mw-fab-link/a")
    start_chat_button.click()

    sleep(1)

    search_for_chat = driver.find_element_by_xpath("/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/mw-new-conversation-sub-header/div/div[2]/mw-contact-chips-input/div/mat-chip-list/div/input")
    search_for_chat.send_keys(name)
    search_for_chat.send_keys("\n")

    sleep(5)

    # recieved_text = driver.find_element_by_xpath("/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-messages-list/mws-bottom-anchored")
    # print(recieved_text.text)

    recieved_text = driver.find_elements_by_css_selector("div _ngcontent-vgx-c166 [class='text-msg ng-star-inserted']")
    print(recieved_text)

   
