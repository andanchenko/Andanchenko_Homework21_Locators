from selenium.webdriver import Chrome


def test_01():
    chrome_driver = Chrome('chromedriver.exe')
    chrome_driver.get('https://demoqa.com/automation-practice-form')
    xpath_locator_first_name = '//input[@id="firstName"]'
    css_locator_first_name = '#firstName'
    xpath_locator_last_name = '//input[@id="lastName"]'
    css_locator_last_name = '#lastName'
    xpath_locator_email = '//input[@id="userEmail"]'
    css_locator_email = '#userEmail'
    xpath_locator_mail_gender = '//input[@id="gender-radio-1"]'
    css_locator_mail_gender = '#gender-radio-1'
    xpath_locator_female_gender = '//input[@id="gender-radio-2"]'
    css_locator_female_gender = '#gender-radio-2'
    xpath_locator_other_gender = '//input[@id="gender-radio-3"]'
    css_locator_other_gender = '#gender-radio-3'
    xpath_locator_mobile = '//input[@id="userNumber"]'
    css_locator_mobile = '#userNumber'
    xpath_locator_birthday = '//div[@class="react-datepicker__input-container"]/input[@id="dateOfBirthInput"]'
    css_locator_birthday = 'div[class = "react-datepicker__input-container"] input'
    xpath_locator_sports = '//div/input[@id="hobbies-checkbox-1"]'
    css_locator_sports = 'div input[id="hobbies-checkbox-1"]'
    xpath_locator_reading = '//input[@id="hobbies-checkbox-2"]'
    css_locator_reading = '#hobbies-checkbox-2'
    xpath_locator_music = '//input[@id="hobbies-checkbox-3"]'
    css_locator_music = '#hobbies-checkbox-3'
    xpath_locator_upload_file = '//div/input[@type="file"]'
    css_locator_upload_file = 'div input[type="file"]'
    xpath_locator_address = '//textarea[@placeholder="Current Address"]'
    css_locator_address = 'textarea[placeholder="Current Address"]'
    xpath_locator_state = '//input[@id="react-select-3-input"]'
    css_locator_state = 'input[id="react-select-3-input"]'
    xpath_locator_city = '//input[@id="react-select-4-input"]'
    xpath_locator_submit = '//button[@type="submit"]'
    css_locator_submit = 'button[type="submit"]'


def test_02():
    chrome_driver = Chrome('chromedriver.exe')
    chrome_driver.get('https://demoqa.com/books')
    xpath_locator_book_link1 = '//span[@id="see-book-Git Pocket Guide"]/a'
    xpath_locator_book_link2 = '//span[@id="see-book-Learning JavaScript Design Patterns"]/a'
    xpath_locator_book_link3 = '//span[@id="see-book-Designing Evolvable Web APIs with ASP.NET"]/a'
    xpath_locator_book_link4 = '//span[@id="see-book-Speaking JavaScript"]/a'
    xpath_locator_book_link5 = '//span[@id="see-book-You Don\'t Know JS"]/a'
    xpath_locator_book_link6 = '//span[@id="see-book-Programming JavaScript Applications"]/a'
    xpath_locator_book_link7 = '//span[@id="see-book-Eloquent JavaScript, Second Edition"]/a'
    xpath_locator_book_link8 = '//span[@id="see-book-Understanding ECMAScript 6"]/a'
    xpath_locator_previous = '//div[@class="-previous"]/button'
    xpath_locator_next = '//div[@class="-next"]/button'
    xpath_locator_input_search = '//input[@id="searchBox"]'
    xpath_locator_button_login = '//button[@id="login"]'


def test_03():
    chrome_driver = Chrome('chromedriver.exe')
    chrome_driver.get('https://demoqa.com/accordian')
    xpath_locator_question1 = '//div[@id="section1Heading"]'
    xpath_locator_question2 = '//div[@id="section2Heading"]'
    xpath_locator_question3 = '//div[@id="section3Heading"]'
