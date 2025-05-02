"""
Name : SeleniumDragDropRandomizer
Author : Suman Gangopadhyay
Date : 2-May-2025
Description : This program uses Selenium to automate random drag-and-drop actions, moving capital cities to their 
              corresponding countries on the demo page at http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html. 
              It shuffles the order of actions for each run and uses Explicit Waits for reliability.
Email : linuxgurusuman@gmail.com
"""


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import time
import random


class Data:
   '''
    The URL is the location of the drag-and-drop demo page, and the dictionary contains capital names as keys 
    and a dictionary with capital and country IDs as values.
    '''
   
   url = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"

   # Dictionary mapping capitals to their respective countries with corresponding box IDs
   capital_to_country = {
        "Oslo": {"capital_id": "box1", "country_id": "box101"},
        "Stockholm": {"capital_id": "box2", "country_id": "box102"},
        "Helsinki": {"capital_id": "box3", "country_id": "box103"},
        "Washington": {"capital_id": "box4", "country_id": "box104"},
        "London": {"capital_id": "box5", "country_id": "box105"},
        "Berlin": {"capital_id": "box6", "country_id": "box106"},
        "Madrid": {"capital_id": "box7", "country_id": "box107"}
    }

class SumanDragDrop(Data):
    '''
    This class handles the drag-and-drop functionality for capital-city pairs using Selenium WebDriver.
    It inherits from the Data class, which contains the URL and capital-country mapping.
    '''
    def __init__(self):

        # Set up the WebDriver (using Chrome in this example)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))        
        self.actions = ActionChains(self.driver)
    
    def drag_and_drop(self):        

        try:

            # Maximize the browser window to ensure elements are visible
            self.driver.maximize_window()

            # Navigate to the demo page
            self.driver.get(self.url)            

            # Randomize the order of capital-country pairs
            capital_list = list(self.capital_to_country.items())
            random.shuffle(capital_list)

            # Perform drag-and-drop for each capital-city pair in random order
            for capital, data in capital_list:
                try:
                    # Wait for the capital element to be present and clickable
                    capital_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, data["capital_id"])))
                    
                    # Wait for the country element to be present and visible
                    country_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, data["country_id"])))
                    
                    # Perform drag-and-drop using ActionChains
                    self.actions.drag_and_drop(capital_element, country_element).perform()
                    
                    print(f"Successfully dragged {capital} to its country")

                    # Optional wait for a moment to observe the action
                    time.sleep(2)  
                    
                except TimeoutException as error:
                    print(f"Error: Timeout waiting for elements for {capital}. {str(error)}")
                except NoSuchElementException as error:
                    print(f"Error: Could not find element for {capital}. {str(error)}")
                except WebDriverException as error:
                    print(f"Error: WebDriver issue while processing {capital}. {str(error)}")

            print("All drag-and-drop actions completed successfully!")

        except Exception as error:
            print(f"An unexpected error occurred: {str(error)}")

        finally:                     
            # Close the browser
            self.driver.quit()

# Main function to run the script
# This is the entry point of the script. It creates an instance of SumanDragDrop and calls the drag_and_drop method.

if __name__ == "__main__":

    drag_drop = SumanDragDrop()
    drag_drop.drag_and_drop()
