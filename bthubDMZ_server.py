# <---- This script will connect to the below Docker image. ---->
# docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest
# pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# <--------- VARABLES TO BE CHANGED ---------------> #

router_ip = "xxx.xxx.xxx.xxx" ## <--- Enter the IP address of your BT Home Hub here!
docker_host = "xxx"  ## <--- Forth ocetet of the IP address for your Docker host running selenium/chrome!
fourth_octet = "xxx" ## <--- Set the forth octet of the IP address to be entered for the DMZ settings!
password = "<ADMIN_PASSWORD>" ## <--- Enter the BT Home Hub admin password here!

#<-------------------------------------------------->#

url = "http://" + router_ip + "/home.htm"
n = 1

octet = router_ip.split(".")
first_octet = octet[0]
second_octet = octet[1]
third_octet = octet[2]
DMZ_IP = first_octet + "." + second_octet + "." + third_octet + "." + fourth_octet

server = "http://" + first_octet + "." + second_octet + "." + third_octet + "." + docker_host + ":4444/wd/hub" 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Remote(command_executor=server, options=chrome_options)

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

