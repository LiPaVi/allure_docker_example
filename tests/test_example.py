import allure
import requests


@allure.title("Test Example")
def test_example():
    assert 1 == 1


@allure.title("Test Bad")
def test_fail():
    assert 1 == 0


@allure.title("Test Error")
def test_error():
    assert 1 / 0


