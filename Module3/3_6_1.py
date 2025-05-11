from selenium import webdriver
import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "testovna@gmail.com"
PASS = "Test123Test"
links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', links)
def test_submit_answer(browser, link):
    browser.get(link)

    time.sleep(5)
    login_button = browser.find_element(By.ID, "ember466")
    login_button.click()
    time.sleep(5)

    input1 = browser.find_element(By.ID, 'id_login_email')
    input1.send_keys(EMAIL)

    input2 = browser.find_element(By.ID, 'id_login_password')
    input2.send_keys(PASS)

    button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    button.click()

    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.modal-dialog"))
    )


    answer = str(math.log(int(time.time())))
    textarea = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )
    textarea.clear()
    textarea.send_keys(answer)


    submit_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    )
    submit_btn.click()

    feedback = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
    ).text

    assert feedback == "Correct!", f"Неверный фидбек: '{feedback}'"





