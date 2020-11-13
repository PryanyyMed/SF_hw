import time


def test_petfriends(web_browser):
    # Open PetFriends base page:
    web_browser.get("https://petfriends1.herokuapp.com/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = web_browser.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    # click existing user button
    btn_exist_acc = web_browser.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    """ add email
    field_email = web_browser.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys("dan555505@gmail.com")

    # add password
    field_pass = web_browser.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys("123456Pp")

    # click submit button
    btn_submit = web_browser.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    # click my pets page
    btn_exist_acc = web_browser.find_element_by_link_text(u"Мои питомцы")
    btn_exist_acc.click()"""

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    assert web_browser.current_url == 'https://petfriends1.herokuapp.com/all_pets', "login error"
    # if selenium.current_url == 'https://petfriends1.herokuapp.com/all_pets':
    #    # Make the screenshot of browser window:
    #    selenium.save_screenshot('result_petfriends.png')
    # else:
    #    raise Exception("login error")
