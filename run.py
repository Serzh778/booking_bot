import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking import Booking

# Import necessary libraries and modules

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

try:
    # Create a new instance of the Booking class and perform various actions

    with Booking() as bot: 
        # Create an instance of the Booking class and use it as a context manager
        # This ensures that the resources are properly managed and cleaned up

        bot.land_first_page()
        # Navigate to the booking.com homepage

        bot.place_to_go('Bangkok')
        # Enter 'Bangkok' in the search field

        time.sleep(1)
        # Wait for 1 second

        bot.close_button()
        # Close the sign-in info dialog

        time.sleep(2)
        # Wait for 2 seconds

        bot.place_to_go_clicked()
        # Click on the search button for 'Bangkok'

        time.sleep(1)
        # Wait for 1 second

        bot.calendar(check_in='2023-04-09', check_out='2023-04-22')
        # Set the check-in and check-out dates in the calendar

        time.sleep(1)
        # Wait for 1 second

        bot.guest_block_click()
        # Open the guest block to modify the number of guests

        time.sleep(1)
        # Wait for 1 second

        bot.adult_add(2)
        # Add 2 adults to the guest count

        time.sleep(1)
        # Wait for 1 second

        bot.done_click()
        # Click on the 'Done' button to confirm the guest count

        time.sleep(1)
        # Wait for 1 second

        bot.search_button()
        # Click on the search button to search for accommodations

        time.sleep(4)
        # Wait for 4 seconds

        bot.apply_filtrations()
        # Apply filtrations to refine the search results

        time.sleep(4)
        # Wait for 4 seconds

        bot.prices()
        # Retrieve and print the prices of accommodations

        time.sleep(1000)
        # Wait for 1000 seconds (for demonstration purposes)

        print('Exiting...')
        # Print a message indicating successful execution

except Exception as e:
    raise e
    # Raise any exceptions that occurred during the execution
