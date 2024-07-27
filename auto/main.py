from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__driver.get("https://www.sibdar-spb.ru/")
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/section[3]/div/div/div[1]/a')))


    @allure.step('Переход на вкладку "Заказать звонок"')
    def input_info_about_me(self):
        WebDriverWait(self.__driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/section[3]/div/div/div[1]/a'))
        )
        self.__driver.find_element(By.XPATH, "/html/body/section[3]/div/div/div[1]/a").click()
        self.__driver.find_element(By.CSS_SELECTOR, '[class="req"]').send_keys("Darya")
        WebDriverWait(self.__driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="Введите телефон *"]'))
        )
        self.__driver.find_element(By.CSS_SELECTOR, '[placeholder="Введите телефон *"]').send_keys("9009945587")
        self.__driver.find_element(By.CSS_SELECTOR, '[class="flex btn-default btnsendajax"]').click()

    @allure.step('Появление текста после отправки формы')
    def check_response(self):
            response_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.thanks.gen_thanks h3"))
        )
            return response_element.text

    @allure.step('Переход к диплому')
    def click_to_open_diploma(self):
        self.__driver.find_element(By.ID, "bx_3099439860_65").click()

    @allure.step('Появление фото диплома')
    def opening_window(self):
        WebDriverWait(self.__driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[src="/upload/iblock/df2/df297634492a84b20bcbf6d5daf18131.png"]'))
        )
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="fancybox-container-1"]/div[2]/div[4]/div[1]/div/img')))
            return True
        except:
            return False

    @allure.step('Переход на вкладку "Сухие грибы"')
    def go_to_dried_mushrooms(self):
        self.__driver.find_element(By.ID, 'bx_1847241719_15').click()

    @allure.step('Просмотр текста продукта')
    def check_text_prod(self):
        WebDriverWait(self.__driver, 20).until(
        EC.presence_of_element_located((By.ID, 'bx_3218110189_259'))
        )
        return self.__driver.find_element(By.XPATH, '//*[@id="bx_3218110189_259"]/h3').text
