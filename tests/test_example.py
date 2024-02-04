import allure
import requests


@allure.id("334")
@allure.title("Test Example")
def test_example():
    assert 1 == 1


@allure.id("333")
@allure.title("Test Bad")
def test_fail():
    assert 1 == 0


@allure.id("331")
@allure.title("Test Error")
def test_error():
    assert 1 / 0
