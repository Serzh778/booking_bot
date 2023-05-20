from selenium import webdriver
import booking.constants as const
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# The `Booking` class is a subclass of `webdriver.Chrome` that adds some additional functionality and behavior to the Chrome driver.
class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/SeleniumDrivers", teardown=False): 
        # The `__init__` method is called when a new instance of the class is created. It initializes some instance variables and calls the superclass's `__init__` method to create a new Chrome driver instance.
        self.driver_path = driver_path 
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # The `__exit__` method is called when the `with` statement is exited. It checks if `self.teardown` is `True` and calls the `quit` method to close the Chrome driver instance if it is.
        if self.teardown:
            self.quit()

    def land_first_page(self): 
        # The `land_first_page` method navigates to the booking.com homepage using the `BASE_URL` constant from the `booking.constants` module.
        self.get(const.BASE_URL)
    
    def place_to_go(self, place_to_go):
        # Locates the search field element and enters the provided place_to_go value.
        search_field = self.find_element(By.ID, ':Ra9:')
        search_field.clear()
        search_field.send_keys(place_to_go)

    def place_to_go_clicked(self):
        # Locates and clicks on the element representing the place to go.
        element1 = self.find_element(By.CLASS_NAME, 'cd1e09fdfe')
        element1.click()

    def close_button(self):
        # Locates and clicks on the dismiss button to close the sign-in info.
        dismiss_button = self.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")
        dismiss_button.click()

    def calendar(self, check_in, check_out):
        # Selects the check-in and check-out dates in the calendar.
        check_in_element = self.find_element(By.CSS_SELECTOR, f'[data-date="{check_in}"]')
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR, f'[data-date="{check_out}"]')
        check_out_element.click()

    def guest_block_click(self):
        # Locates and clicks on the guest block element.
        guest_block_element = self.find_element(By.CLASS_NAME, 'd67edddcf0')
        guest_block_element.click()

    def adult_add(self, times):
        # Locates and clicks on the add button for increasing the number of adults.
        add_element = self.find_element(By.XPATH, "//button[@class='fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 d64a4ea64d']")
        for i in range(times):
            add_element.click()

    def done_click(self):
        # Locates and clicks on the done button to confirm the guest selection.
        done_element = self.find_element(By.XPATH, "//button[@class='fc63351294 a822bdf511 e2b4ffd73d f7db01295e c938084447 a9a04704ee d285d0ebe9']/span[text()='Done']")
        done_element.click()

    def search_button(self):
        # Locates and clicks on the search button to initiate the search.
        search_element = self.find_element(By.XPATH, "//button[@class='fc63351294 a822bdf511 d4b6b7a9e7 cfb238afa1 c938084447 f4605622ad aa11d0d5cd' and @type='submit']/span[text()='Search']")
        search_element.click()

    def apply_filtrations(self):
        # Applies the filtration for the desired criteria (in this case, five-star hotels).
        column = self.find_element(By.ID, 'filter_group_class_:R14q:')
        five_star = column.find_element(By.ID, ':Rlf94q:')
        five_star.click()

    def budget(self):
        # Applies the budget filtration.
        column1 = self.find_element(By.ID, 'filter_group_pri_:Rcq:')
        budget = column1.find_element(By.ID, ':rfm:')
        budget.click()

    def next_button_click(self):
        # Clicks on the next button to navigate to the next page and retrieves prices within a certain range.
        next_button = self.find_element(By.CSS_SELECTOR, "button.fc63351294[type='button']")
        while True:
            try:
                next_button.click()
                values = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='price-and-discounted-price']"))
                )
                prices = []
                for price in values:
                    price_text = price.text.replace('THB', '').replace(',', '').strip()
                    price_value = int(price_text)
                    if price_value <= 30000:
                        prices.append(price_value)
                return prices
            except Exception:
                print('there is a problem')

    def prices(self):
        # Iterates through the pages and retrieves all prices within the specified range.
        all_prices = []
        while True:
            prices = self.next_button_click()
            if not prices:
                break
            all_prices.extend(prices)

        print(all_prices)

        # Closes the driver
        self.quit()
