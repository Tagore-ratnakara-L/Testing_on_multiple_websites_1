import time

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/Main_Page')
driver.switch_to.new_window('tab')
# time.sleep(10)
# driver1 = webdriver.Chrome()
driver.get('https://python.org')
# driver.execute_script('window.open();')
print(driver.current_window_handle)# A02DF6A6EE218EF66EC6DF5E64919BFE
print(driver.current_url)#https://www.python.org/
print(driver.window_handles)
#['37AFFBC39668F4CA7834F8244E561161', 'B15D0BE5FCC9A963E2121F99081BFCEA', '5D1A752CD13D4A190B64CCD9EBDBD17B']
time.sleep(3)
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    print(f'Now on {driver.current_url}')
    # Now on https: // en.wikipedia.org / wiki / Main_Page
    # Now on https: // www.python.org /

driver.quit()
