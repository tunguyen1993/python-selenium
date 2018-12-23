from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from flask import jsonify

class InstagramBot:
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url
        self.driver = webdriver.Chrome()

    def closeBrower(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(1)
        login_button = driver.find_element_by_css_selector('p.izU2O a')
        login_button.click()
        time.sleep(1)
        user_name_ele = driver.find_element_by_css_selector("div.f0n8F input[type='text']")
        user_name_ele.clear()
        user_name_ele.send_keys(self.username)
        password_ele = driver.find_element_by_css_selector("div.f0n8F input[type='password']")
        password_ele.clear()
        password_ele.send_keys(self.password)
        password_ele.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.get(self.url)

        # print(driver.find_element_by_css_selector('.EDfFK div span span').text)
        content = driver.find_element_by_xpath("//meta[@property='og:title']").get_attribute("content")
        post_type = driver.find_element_by_xpath("//meta[@property='og:type']").get_attribute("content")
        views = 0
        likes = 0
        comments = 0
        if post_type == 'video':
            views = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/span/span').text
        else:
            likes = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/a/span').text

        if driver.find_element_by_xpath("//meta[@name='description']"):
            meta = driver.find_element_by_xpath("//meta[@name='description']").get_attribute("content")
            meta = meta.split(' ')
            likes = meta[0]
            comments = meta[2]

        return jsonify(
            content=content,
            views=views,
            likes=likes,
            comments=comments,
        )

class FacebookBot:
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url
        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        driver.get('https://www.facebook.com/login')
        time.sleep(1)
        user_name_ele = driver.find_element_by_xpath('//*[@id="email"]')
        user_name_ele.clear()
        user_name_ele.send_keys(self.username)
        password_ele = driver.find_element_by_xpath('//*[@id="pass"]')
        password_ele.clear()
        password_ele.send_keys(self.password)
        password_ele.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.get(self.url)
        time.sleep(1)

    def get_url_not_login(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(1)

    def get_data_login(self):
        driver = self.driver
        content = driver.find_element_by_class_name('_1rg-')
        contents = content.get_attribute('innerHTML')
        actions_element = driver.find_elements_by_class_name('_36_q')
        actions = []
        reactions_element = driver.find_elements_by_class_name('_3t54')
        for action in actions_element:
            actions.append(action.text)
        reaction = []
        for reactions in reactions_element:
            reaction.append(reactions.get_attribute('innerHTML'))
        # comments = driver.find_element_by_class_name('_ipm _-56').get_attribute("content")

        self.driver.close()
        return jsonify(
            content=contents,
            actions=actions,
            reaction=reaction
        )

    def get_data_not_login_video(self):
        driver = self.driver
        actions = driver.find_element_by_css_selector('._1f6t ._524d >a').get_attribute('aria-label')
        view = driver.find_element_by_css_selector('._1t6k .fcg').text
        content = driver.find_element_by_css_selector('.userContent').get_attribute('innerHTML')
        self.driver.close()
        view = view.split(' ')
        actions = actions.split(' ')

        return jsonify(
            like=actions[0],
            comment=actions[3],
            share=actions[6],
            view=view[0],
            content=content
        )

    def get_data_not_login_post(self):
        driver = self.driver
        actions = driver.find_element_by_css_selector('._1f6t ._524d >a').get_attribute('aria-label')
        content = driver.find_element_by_css_selector('.userContent').get_attribute('innerHTML')
        self.driver.close()
        actions = actions.split(' ')

        return jsonify(
            like=actions[0],
            comment=actions[3],
            share=actions[6],
            content=content
        )
