# -*- coding: utf-8 -*-
"""
Submit application to Immobilienscout24
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import config


def submit_application(ref):
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

    driver.get(f'https://www.immobilienscout24.de{ref}#/basicContact/email')
    driver.implicitly_wait(10)

    el = driver.find_element_by_id('contactForm-salutation')
    for option in el.find_elements_by_tag_name('option'):
        if option.text == 'Herr':
            option.click() # select() in earlier versions of webdriver
            break

    # Fill out application form from configuration values
    last_name = driver.find_element_by_id('contactForm-lastName')
    last_name.send_keys(config.contact_form['last_name'])

    first_name = driver.find_element_by_id('contactForm-firstName')
    first_name.send_keys(config.contact_form['first_name'])

    email = driver.find_element_by_id('contactForm-emailAddress')
    email.send_keys(config.contact_form['email'])

    street = driver.find_element_by_id('contactForm-street')
    street.send_keys(config.contact_form['street'])

    house = driver.find_element_by_id('contactForm-houseNumber')
    house.send_keys(config.contact_form['house_number'])

    post = driver.find_element_by_id('contactForm-postcode')
    post.send_keys(config.contact_form['postal_code'])

    city = driver.find_element_by_id('contactForm-city')
    city.send_keys(config.contact_form['city'])

    text_area = driver.find_element_by_id('contactForm-Message')
    text_area.clear()
    text_area.send_keys(config.application_text)

    submit_button1 = driver.find_element_by_xpath(
        "//button[@data-ng-click='submit()' or contains(.,'Anfrage senden')]"
    )

    time.sleep(5)  # May not be required
    submit_button1.click()

    time.sleep(3)  # May not be required

    try:
        submit_button = driver.find_element_by_xpath(
            "//button[@data-ng-click='submit()' or "
            "contains(.,'Anfrage senden')]"
        )
    except NoSuchElementException:
        driver.quit()
    else:
        ActionChains(driver).move_to_element(submit_button).perform()
        time.sleep(3)  # May not be required
        submit_button.click()
        driver.quit()
