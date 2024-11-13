from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
import time
from time import sleep
flag=0
driver = webdriver.Chrome()

def login_instagram(driver):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys("")
    password_input.send_keys("")
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

def save_cookies(driver, filename="cookies.pkl"):
    cookies = driver.get_cookies()
    with open(filename, 'wb') as file:
        pickle.dump(cookies, file)
    print("Cookies have been saved successfully.")

def load_cookies(driver, filename="cookies.pkl"):
    try:
        with open(filename, 'rb') as file:
            cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        print("Cookies have been loaded successfully.")
    except FileNotFoundError:
        print("Cookie file not found. You need to log in first.")

def main():
    global flag
    cookie_file = "cookies.pkl"
    driver.get("https://www.instagram.com")
    time.sleep(2)
    if "Log in" not in driver.page_source:
        print("Already logged in!")
    else:
        print("Not logged in. Loading cookies...")
        load_cookies(driver, cookie_file)
        driver.refresh()
    
    if "Log in" in driver.page_source:
        print("Logging in...")
        login_instagram(driver)
        save_cookies(driver, cookie_file)
    recurring()

def recurring():
    driver.get("https://www.instagram.com/direct/t/17850847643639917/")
    sleep(5)
    xpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div[2]/a/div/span/div[2]/span/div"
    try:
        element = driver.find_element(By.PARTIAL_LINK_TEXT, """parnika""")
        print(element.text)
        if "now" in element.text:
         if flag==0:
            driver.get("https://www.instagram.com/reel/C31TKc9PlFx/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==")
            sleep(2)
            share = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[3]/section[1]/div[1]/button/div[2]""")
            share.click()
            sleep(2)
            srch = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/input")
            srch.send_keys("parnika")
            driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[3]/div/label/div/input").click()
            sleep(2)
            driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div").click()
            flag=1
        else:
            flag=0
    except(e):
        sleep(5)
        recurring()
    sleep(60)
    recurring()

main()
