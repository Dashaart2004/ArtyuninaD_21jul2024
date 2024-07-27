from selenium import webdriver
import pytest
import allure
from main import MainPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from api import ApiRequests

api = ApiRequests("https://www.sibdar-spb.ru/ajax/basketOrder.php")


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.mark.ui_test
@allure.id(1)
@allure.title("Отправка заказа")
def test_make_order(driver):
    main_page = MainPage(driver)
    main_page.input_info_about_me()
    result = main_page.check_response()
    assert result == "Спасибо, Ваша заявка отправлена!"


@pytest.mark.ui_test
@allure.id(2)
@allure.title("Появление фотографии диплома")
def test_opening_diploma(driver):
    main_page = MainPage(driver)
    main_page.click_to_open_diploma()
    result = main_page.opening_window()
    assert result == True


@pytest.mark.ui_test
@allure.id(3)
@allure.title("Наличие валидного продукта во вкладке")
def test_page_consist_of_prod(driver):
    main_page = MainPage(driver)
    main_page.go_to_dried_mushrooms()
    res = main_page.check_text_prod()
    assert res == "Сухой Белый Гриб"


@pytest.mark.api_test
@allure.id(4)
@allure.title("Добавление товара")
def test_add_product():
    result = api.add_prod()
    assert result == 1


@pytest.mark.api_test
@allure.id(5)
@allure.title("Увеличение количества  товара")
def test_increase_prod():
    result = api.increase_prod()
    assert result == 3


@pytest.mark.api_test
@allure.id(6)
@allure.title("Уменьшение  количества  товара")
def test_reduction_prod():
    result = api.reduction_prod()
    assert result == 2
