def test_search(selenium):
    #open google
    selenium.get('https://google.com')

    #find search field on the main page by name
    search_input=selenium.find_element_by_name('q')

    #clear search bar and type in some text for search:
    search_input.clear()
    search_input.send_keys('first123456test')

    #click search button
    search_button=selenium.find_element_by_name('btnK')
    search_button.submit()

    #make screenshot of browser window
    selenium.save_screenshot('result.png')