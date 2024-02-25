import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://selenium.dev')
driver.set_network_conditions(
    offline=True,
    latency=50,
    download_throughput=500 * 1024,
    upload_throughput=500 * 1024
)
driver.set_network_conditions(
    offline=False,
    latency=5000,
    download_throughput=250 * 1024,
    upload_throughput=250 * 1024
)
driver.get('https://python.org')
print(driver.get_network_conditions())
time.sleep(4)
driver.close()
