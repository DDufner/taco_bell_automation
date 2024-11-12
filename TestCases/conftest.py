from selenium import webdriver
import pytest

@pytest.fixture()
def driver_setup():
    driver = webdriver.Firefox()
    return driver