import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking import Booking


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

try:
    with Booking() as bot: 
        bot.land_first_page()
        bot.place_to_go('Bangkok')
        time.sleep(1)
        bot.close_button()
        time.sleep(2)
        bot.place_to_go_clicked()
        time.sleep(1)
        bot.calendar(check_in='2023-04-09',check_out='2023-04-22')
        time.sleep(1)
        bot.guest_block_click()
        time.sleep(1)
        bot.adult_add(2)
        time.sleep(1)
        bot.done_click()
        time.sleep(1)
        bot.search_button()
        time.sleep(4)
        bot.apply_filtrations()
        time.sleep(4)
        bot.prices()
        time.sleep(1000) 
        print('Exiting...')
except Exception as e:
    raise e