from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('D:/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
driver.set_window_size(1920, 1080)
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "login-otp-button").click()
time.sleep(1)
driver.find_element(By.ID, "accounts-index").click()
time.sleep(1)
driver.find_element(By.ID, "payments-form").click()
time.sleep(1)
driver.find_element(By.ID, "cards-overview-index").click()
time.sleep(1)
driver.find_element(By.ID, "deposits-index").click()
time.sleep(1)
driver.find_element(By.ID, "loans-index").click()
time.sleep(1)
driver.find_element(By.ID, "externaltraderoom-index").click()
time.sleep(1)
driver.find_element(By.ID, "insurance-vehicle").click()
time.sleep(1)
driver.find_element(By.ID, 'bank-overview').click()

time.sleep(3)