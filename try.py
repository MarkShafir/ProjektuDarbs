from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.chrome.service import Service 
  
service = Service() 
option = webdriver.ChromeOptions() 
driver = webdriver.Chrome(service=service, options=option) 
  
 
driver.get('https://www.nvidia.com/Download/index.aspx')  
 
login_form = driver.find_element(By.XPATH, "//btn_drvr_lnk_txt") 
login_form.click() 
 
driver.vers = driver.find_element(By.ID, "tdVersion") 
print(driver.vers.text)