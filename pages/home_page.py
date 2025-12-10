from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.manager_id = (By.XPATH, "//td[contains(normalize-space()='Manager Id =')]")
        
    
    def is_logged(self):
        
        try:
            return "Manager" in self.driver.title or self.driver.find_element(*self.manager_id)
        except Exception:
            return False