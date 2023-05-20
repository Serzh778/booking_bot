from selenium import webdriver
import booking.constants as const
import os
from selenium.webdriver.common.by import By
from booking.booking_filtration import BookingFiltration
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration():
    def __init__(self, driver: WebDriver):
        # The `BookingFiltration` class handles the filtration functionality on the booking.com website.
        # It takes a WebDriver object as a parameter to interact with the browser.
        self.driver = driver

    def star_filtration(self):
        # Applies the star filtration to filter the results for five-star hotels.
        column = self.driver.find_element(By.ID, 'filter_group_class_:R14q:')
        five_star = column.find_element(By.ID, ':Rlf94q:')
        five_star.click()

