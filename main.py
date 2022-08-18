import os
import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def log_in(driver):
    # click to log in button
    time.sleep(10)
    log_in_button = driver.find_element(By.XPATH, '//*[@id="t-188693591"]/div/div[1]/div/main/div[1]/div/div/div/div/'
                                                  'header/div/div[2]/div[2]/a')

    log_in_button.click()
    # click to log in with Facebook button
    time.sleep(5)
    log_in_with_facebook_button = driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div[1]/'
                                                                'div/div/div[3]/span/div[2]/button')
    log_in_with_facebook_button.click()

    # switch to Facebook login window
    main_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    print(driver.title)

    # login and hit enter
    time.sleep(5)
    login_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')
    login_field.send_keys(os.getenv("PHONE"))
    password_field.send_keys(os.getenv("PASSWORD"))
    password_field.send_keys(Keys.ENTER)

    # switch to Tinder window
    driver.switch_to.window(main_window)
    print(driver.title)


def main():
    # options = Options()
    # options.binary_location = "/usr/bin/google-chrome-stable /usr/share/man/man1/google-chrome-stable.1.gz"  # chrome binary location specified here
    # options.add_argument("--start-maximized")  # open Browser in maximized mode
    # options.add_argument("--no-sandbox")  # bypass OS security model
    # options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)
    chrome_driver_path = "/usr/lib/chromium-browser/chromedriver"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get("https://tinder.com/")

    log_in(driver)

    time.sleep(10)
    location_pop_up = driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div/div/div[3]/button[1]')
    location_pop_up.click()
    time.sleep(2)
    notification_pop_up = driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div/div/div[3]/button[2]')
    notification_pop_up.click()

    cookies_pop_up = driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[2]/div/div/div[1]/div[1]/button')
    cookies_pop_up.click()

    time.sleep(10)

    for n in range(20):
        time.sleep(5)
        try:
            # action = ActionChains(driver)
            # action.send_keys(Keys.ARROW_UP)
            time.sleep(5)
            like_button = driver.find_element(By.XPATH,
                                              '//*[@id="u-1650273590"]/div/div[1]/div/div/main/div/div/div[1]/div/div[5]/div/div[4]/button')
            like_button.click()
        except ElementClickInterceptedException:
            try:
                match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
                match_popup.click()
            except NoSuchElementException:
                time.sleep(2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
