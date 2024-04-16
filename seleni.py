# from selenium.webdriver import Chrome
import os
import time
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from decouple import config
import pyautogui
# import webbrowser
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def setup(*,url,groupsFile):
    clear_screen()
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
   
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
   
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    groups = []
    with open(groupsFile,'r') as file:
        groups = file.readlines()
        print('[+] Groups Succesfully')
    return [driver, groups]

def logIn(*,driver,email,password) -> None:  
    driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(email)
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="pass"]').send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@name='login']").click()
    time.sleep(4)
    print('[+] Logged Succesfully')

def posting(*,driver,groups,url,postFile):
    print('[+] Initializing posting process')

    for group in groups:
        currentURL = str(url + "groups/"+ group.strip())
        print(f"[+] {currentURL}")
        driver.get(currentURL)
        time.sleep(3)
        try:
            try:
                driver.find_element(By.XPATH,'/html/body//div[2]/a[2]//span[contains(text(), "Conversación")]').click()
            except:
                print("[-] Not in secondary div")
            driver.find_element(By.XPATH,"//*[contains(text(), 'Escribe algo...')]").click()
            
            time.sleep(2)
            with open(postFile,"r") as file:
                content = file.read()
                time.sleep(2)
                
                print(f"[+] Contenido: {content}")
                
                pyautogui.typewrite(content)
                pyautogui.hotkey('ctrl','v')
                time.sleep(5)
                # driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/span/img').click()
                # driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div/div').click()
                driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div/div/div/div[1]/div/span/span[contains(text(),"Publicar")]').click()
                time.sleep(60)
        except Exception as e:
            print(f'[-] An exception occurred: {e}')
    
def main():
    url = "https://www.facebook.com/"
    email = config("email")
    password = config("password")
    postFile = "./fBot/publicaciones/casa.txt" 
    groupsFile = "./fBot/publicaciones/groups.txt"
   
    stp = setup(url=url,groupsFile=groupsFile)    
    logIn(driver=stp[0],email=email,password=password) 
    
    while True:
        posting(driver=stp[0],groups=stp[1],url=url,postFile=postFile)      
        time.sleep(int(3600*3))
        
if __name__=="__main__":
    main()