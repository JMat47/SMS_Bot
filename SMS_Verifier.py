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
#names_list = ["9384832755","9840656355"]

donorData = pd.read_csv(r"Sent_log.csv")
names_list = [list(row) for row in donorData.values]
print(names_list)

wait_for_verification = input()
sleep(2)

for name in names_list:
    start_chat_button = driver.find_element_by_xpath("/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/div/mw-fab-link/a")
    start_chat_button.click()

    sleep(1)

    search_for_chat = driver.find_element_by_xpath("/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/mw-new-conversation-sub-header/div/div[2]/mw-contact-chips-input/div/mat-chip-list/div/input")
    search_for_chat.send_keys(name[2])
    search_for_chat.send_keys("\n")

    sleep(3)

    recieved_text = driver.find_elements_by_xpath("/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-messages-list/mws-bottom-anchored/div/div/div/mws-message-wrapper")
    recieved_text = recieved_text[1:]
    recieved_text =[x.text for x in recieved_text]
    t = "".join(recieved_text).lower()
    if("yes" in t and "no" in t):
        name.append("Ambigious")
    elif("wrong" in t):
        name.append("Wrong INFO")
    elif("yes" in t):
        name.append("Donor")
    elif("no" in t):
        name.append("Not a Donor")
    else:
        name.append("No Valid reply")

    data = [name]
    column_names = ["Name", "BloodGroup", "PhoneNo","District","City","SMS","Donor"]
    df = pd.DataFrame(data, columns=column_names)
    df.to_csv('Verify_log.csv',mode='a', index=False, header=False)


sleep(5)
driver.quit()
   
