import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from random import randint


class toni(unittest.TestCase):
# >>> Web browser Section

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/accounts/login/?hl=es")
        time.sleep(1)

# >>> Login Section
#self.user.send_keys('USER1234')
        self.user = self.driver.find_element_by_name('username')
        self.user.send_keys('tonymaccarroneph')

#self.password.send_keys('PASS1234')
        self.password = self.driver.find_element_by_name('password')
        self.password.send_keys('antonio22')

# >>> Hashtag Section
        self.password.send_keys(Keys.ENTER)
        location = input('Location: ')
        time.sleep(1.3)
        self.driver.get('https://www.instagram.com/explore/locations/'+location+'/?hl=es')
        self.driver.implicitly_wait(10)
        element = self.driver.find_element_by_class_name('_9AhH0')
        try:
            WebDriverWait(self.driver, 120).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,'_9AhH0')))
        except NoSuchElementException:
            pass
        element.click()

# >>> Image Pop up Section
    def findUser(self):
        time.sleep(2)
        user = self.driver.find_element_by_class_name('zV_Nj')
        user.send_keys(Keys.CONTROL + Keys.ENTER)
        self.driver.switch_to.window(self.driver.window_handles[1])
        print(self.driver.current_url)
        time.sleep(1.05)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        print(self.driver.current_url)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)

# >>> Like Section
    def LikeSlide(self):
        tiempo = randint(1,3)
        try:
            self.driver.find_element_by_xpath("//span[@aria-label='Me gusta']").click()
        except NoSuchElementException:
            pass
        try:
            self.driver.find_element_by_xpath("//span[@aria-label='Like']").click()
        except NoSuchElementException:
            pass
        time.sleep(tiempo*1.05)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
        time.sleep(tiempo*0.75)

# >>> Likes definition Section
    def testSa(self):
        cantidad = int(input('Cantidad de likes: '))
        for x in range(0, cantidad):
            if 'stopinsta' in self.driver.current_url:
                break
            else:
                pass
            print (str(x) + ' '+ self.driver.current_url)
            self.LikeSlide()
        again = input('Seguir likeando? (y/n): ')
        if again == 'y':
            hashtag = input('Tipear Hash: ')
            self.driver.get('https://www.instagram.com/explore/tags/'+hashtag+'/?hl=es')
            self.testSa()
        else:
            pass
