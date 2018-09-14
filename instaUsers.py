import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from random import randint
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from excelData import *


class toni(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/accounts/login/?hl=es")
        time.sleep(1)

#self.user.send_keys('plus54vpn@gmail.com')
        self.user = self.driver.find_element_by_name('username')
        self.user.send_keys('tonymaccarroneph')
#self.password.send_keys('tecateca12')
        self.password = self.driver.find_element_by_name('password')
        self.password.send_keys('antonio22')

        self.password.send_keys(Keys.ENTER)

        profile: str = input('Tipear Profile: ')
        time.sleep(1)
        self.driver.get('https://www.instagram.com/'+profile+'/?hl=es')
        time.sleep(2)
        continuar = str
        while continuar != 'si':
            continuar = input('Arrancamos?')
            time.sleep(0.5)
#self.driver.find_element_by_class_name('_9AhH0').click()

    def detectVideo(self):
        try:
            self.driver.find_element_by_class_name('zV_Nj')
            a = True
        except NoSuchElementException:
            a = False

        return a

    def findUserThatLikes(self):
        time.sleep(1)
        while self.detectVideo() == False:
            try:
                self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
                time.sleep(2)
                self.detectVideo()
            except NoSuchElementException:
                pass
        userThatLikes = self.driver.find_element_by_class_name('zV_Nj')
        qty = userThatLikes.text
        print('\n')
        print (qty, 'sin modificar')
        userThatLikes.click()
        time.sleep(2)
        qty = re.sub("[^0-9]", "", qty)
        qty= int(qty)
        rango = int(qty/10)
        if qty > 10:
            for x in range(0,rango*3):
                xpath = 'wFPL8 '
                scroll = self.driver.find_elements_by_class_name(xpath)
                time.sleep(2)

                try:
                    self.driver.execute_script("return arguments[0].scrollIntoView(true);", scroll[-1])
                except NoSuchElementException:
                    pass
        else:
            pass
        time.sleep(3)
        self.users = self.driver.find_elements_by_class_name('FPmhX')
        print(len(self.users))
        print('\n')
        time.sleep(2)

        return self.users

    def test(self):
        for x in range(0, 5):
            self.findUserThatLikes()
            self.navigateAndLike()
        again = input('Seguimos likeando? (y/n): ')
        if again == 'y':
            profile = input('Tipear Profile: ')
            self.driver.get('https://www.instagram.com/' + profile + '/?hl=es')
            time.sleep(3)
            continuar = str
            while continuar != 'si':
                continuar = input('Arrancamos?')
                time.sleep(0.5)
            self.test()
        else:
            pass

    def LikeForUsers(self):
        tiempo = randint(1, 4)

        try:
            self.driver.find_element_by_xpath("//span[@aria-label='Me gusta']").click()
        except NoSuchElementException:
            pass
        try:
            self.driver.find_element_by_xpath("//span[@aria-label='Like']").click()
        except NoSuchElementException:
            pass
        time.sleep(tiempo * 1.09)
        slidearRandom = randint(1, 4)
        for x in range(0, slidearRandom):
            self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
            time.sleep(slidearRandom)

    def navigateAndLike(self):
        for idx, user in enumerate(self.users):
            link = user.get_attribute('href')
            user.send_keys(Keys.CONTROL + Keys.ENTER)
            while (len(self.driver.window_handles)) == 1:
                time.sleep(0.5)

            self.driver.switch_to.window(self.driver.window_handles[1])

            headerywait = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "head")))

            '''if "Sorry, this page isn't available." in self.driver.page_source or "Esta página no está disponible." in self.driver.page_source or 'Oops, an error occurred' in self.driver.page_source or 'Sorry, something went wrong' in self.driver.page_source:
                pass
            else:
            implicitwait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_mainc")))
            '''

            if 'This Account is Private' in self.driver.page_source or 'No posts yet.' in self.driver.page_source or 'Esta cuenta es privada' in self.driver.page_source or 'Aún no hay publicaciones.' in self.driver.page_source or "Sorry, this page isn't available." in self.driver.page_source or "Esta página no está disponible." in self.driver.page_source or 'Oops, an error occurred' in self.driver.page_source or 'Sorry, something went wrong' in self.driver.page_source:
                time.sleep(1.5)
                pass

            elif self.driver.current_url in return_excelValue('Lista'):
                print('Ya esta en la lista')

            elif self.driver.current_url in return_excelValue('Cruda'):
                print('Ya esta en la lista')

            else:
                time.sleep(1.5)

                try:
                    element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_9AhH0")))
                except:
                    pass

                try:
                    self.driver.find_element_by_class_name('_9AhH0').click()
                except NoSuchElementException:
                    pass
                time.sleep(1)
                for x in range(0, 5):
                    self.LikeForUsers()
                appendLink(link)
                print(idx)

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)

    def LikeSlide(self):
        tiempo = randint(5,10)

        try:
            self.driver.find_element_by_link_text('Me gusta').click()
        except NoSuchElementException:
            print('ya le di like')
            pass


        '''
        try:
            self.driver.find_element_by_link_text('Like').click()
        except NoSuchElementException:
            print('ya le di like')
            pass
        '''
        time.sleep(tiempo*1.09)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
        time.sleep(tiempo*0.75)
