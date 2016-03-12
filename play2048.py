from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def play2048():
    browser = webdriver.Firefox()
    browser.get('https://gabrielecirulli.github.io/2048/')
    scoreElem = browser.find_element_by_class_name('score-container')
    htmlElem = browser.find_element_by_tag_name('html')

    tries = 0

    while tries < 100:
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)

        #score = int( scoreElem.text )
        print('The score after try' + str(tries) + ' is: ' + scoreElem.text)
    
        tries += 1

    print('The final score is: ' + scoreElem.text)