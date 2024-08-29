# apt install -y python3 python3-pip
# pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import logging

logging.basicConfig(filename='/var/log/bt-hub-dmz.log', level=logging.INFO)
#logging.disable() ## <--- Uncomment to disable logging.

# <--------- VARABLES TO BE CHANGED ---------------> #

router_ip = "xxx.xxx.xxx.xxx" ## <--- Enter the IP address of your BT Home Hub here!
fourth_octet = "xxx" ## <--- Set the forth octet of the IP address to be entered into the DMZ settings!
password = "<ADMIN_PASSWORD>" ## <--- Enter the BT Home Hub admin password here!

#<-------------------------------------------------->#

url = "http://" + router_ip + "/home.htm"
n = 1
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

octet = router_ip.split(".")
first_octet = octet[0]
second_octet = octet[1]
third_octet = octet[2]
DMZ_IP = first_octet + "." + second_octet + "." + third_octet + "." + fourth_octet

driver.get(url)
time.sleep(n)
driver.find_element(By.ID ,"gotoA").click() # Select the Advance settings tile.
time.sleep(n)
driver.find_element(By.ID ,"advFirewall").click() # Select the Firewall tile.
time.sleep(n)
driver.find_element(By.ID , "login_password_input_noshow").send_keys(password) # Input password at the Enter the admin password prompt.
time.sleep(n)
driver.find_element(By.ID ,"ok_button").click() # Click the OK button at the Enter the admin password prompt.
time.sleep(n)
driver.find_element(By.ID ,"secMenu_configuration").click() # Select the Configration tab.
time.sleep(n)
element = driver.find_element(By.ID ,"dmz_ip")
DMZ_SERVER = element.get_attribute("value")

if DMZ_SERVER != DMZ_IP:
    logging.info(str(datetime.now()) + ' DMZ server was ' + str(DMZ_SERVER) + ' and is now: ' + str(DMZ_IP))
    driver.find_element(By.ID ,"show_IP_address_dmz").click() # Click on the Show IP address button under the DMZ section.
    driver.find_element(By.ID ,"dmz_ip").click() # Click the Device IP address field.
    driver.find_element(By.ID ,"IP1").click()  # Click the 1st octet field.
    driver.find_element(By.ID ,"IP1").clear() # Clear the existing number is the 1st octet field.
    driver.find_element(By.ID ,"IP1").send_keys(first_octet) # Input the 1st octet number into the 1st octet field.
    driver.find_element(By.ID ,"IP2").click()
    driver.find_element(By.ID ,"IP2").clear()
    driver.find_element(By.ID ,"IP2").send_keys(second_octet) # set 2nd octet of DMZ ip address.
    driver.find_element(By.ID ,"IP3").click()
    driver.find_element(By.ID ,"IP3").clear()
    driver.find_element(By.ID ,"IP3").send_keys(third_octet) # set 3rd octet of DMZ ip address.
    driver.find_element(By.ID ,"IP4").click()
    driver.find_element(By.ID ,"IP4").clear()
    driver.find_element(By.ID ,"IP4").send_keys(fourth_octet) # set 4th octet of DMZ ip address.
    time.sleep(n)
    driver.find_element(By.ID ,"IPset").click() # Click the Set button on the Set IP address dialogue.
    time.sleep(n)
    driver.find_element(By.XPATH ,'//*[@onclick="SaveButtonConfiguration()"]').click() # Click the Save button.
    time.sleep(5)
    driver.quit()
else: 
    logging.info(str(datetime.now()) + ': DMZ server is: ' + str(DMZ_IP))
    
