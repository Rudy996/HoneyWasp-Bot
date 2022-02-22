from selenium import webdriver
import time
from string import digits, ascii_uppercase
from random import choice, randint

from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_extension("MetaMask.crx")
# options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
try:
    private = ("") # PrivateKey
    passw = ("") #Пароль от метамаска

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    driver.get(
        "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase")
    time.sleep(1)
    print("Начинаем импортировать ключи и добавлять пароль")
    clu4iki = driver.find_element_by_xpath("//input[@type='password']")
    # clu4iki = driver.find_element_by_xpath("MuiInput-input")
    clu4iki.send_keys(private)
    password1 = driver.find_element_by_id("password")
    password1.send_keys(passw)
    password2 = driver.find_element_by_id("confirm-password")
    password2.send_keys(passw)
    driver.find_element_by_class_name("first-time-flow__terms").click()
    driver.find_element_by_class_name("first-time-flow__button").click()
    print("Были импортированны ключи и добавлен пароль")
    time.sleep(5)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(2)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network")
    time.sleep(1)
    elems = driver.find_elements_by_class_name("form-field__input")
    print("Начинаем добавлять сеть Polygon")
    elems[0].send_keys("Matic")
    elems[1].send_keys("https://polygon-rpc.com/")
    elems[2].send_keys("137")
    elems[3].send_keys("MATIC")
    elems[4].send_keys("https://polygonscan.com/")
    driver.find_element_by_class_name("btn-primary").click()
    print("Сеть Polygon добавлена")
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.app.honeywasp.com/")
    time.sleep(3)
    driver.find_element_by_xpath("//div[@id='root']/header/nav/div/div/div[2]/div/button").click()
    time.sleep(1)
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select a Wallet'])[1]/following::span[1]").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    time.sleep(3)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(0.2)
    driver.find_element_by_class_name("btn-primary").click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    while True:
        name = ''.join(choice(ascii_uppercase) for i in range(6))
        driver.find_element_by_id("username").send_keys(" ")
        driver.find_element_by_id("username").send_keys(name)
        time.sleep(1)
        global start
        try:
            start = driver.find_element_by_xpath("//button[@type='submit']").is_enabled()
            while start == True:
                driver.find_element_by_xpath("//button[@type='submit']").click()
                time.sleep(1)
                start = driver.find_element_by_xpath("//button[@type='submit']").is_enabled()
        except:
            print("")
        try:
            cl = driver.find_element_by_class_name("items-center").is_enabled()
            while cl == True:
                driver.find_element_by_class_name("items-center").click()
                time.sleep(1)
                cl = driver.find_element_by_class_name("items-center").is_enabled()
        except:
            print("")
        time.sleep(1)
        try:
            retry = driver.find_elements_by_class_name("text-base")
            retry[2].click()
        except:
            print("")

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
