from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FundtransferPage:
    
    def __init__(self,driver):
        self.driver = driver
        self.menu_link = (By.LINK_TEXT, "Fund Transfer")
        self.payers_accno = (By.NAME, "payersaccount")
        self.payees_accno = (By.NAME, "payeesaccount")
        self.payamount = (By.NAME, "ammount")
        self.description = (By.NAME, "desc")
        self.submit = (By.NAME, "AccSubmit")
        self.successmsg = (By.XPATH, "//p[normalize-space()='Fund Transfer Details']")
    

    def navigate_to_fundtransfer(self):
        # Scroll page to top so footer doesn't cover menu
        self.driver.execute_script("window.scrollTo(0, 0);")

        # Wait for it to be clickable
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu_link)
        )

        # Click safely
        link.click()
        
    
    def transfer(self, payer, payee, amount, descript = "Test transfer"):
        self.driver.find_element(*self.payers_accno).clear()
        self.driver.find_element(*self.payers_accno).send_keys(payer)
        
        self.driver.find_element(*self.payees_accno).clear()
        self.driver.find_element(*self.payees_accno).send_keys(payee)
        
        self.driver.find_element(*self.payamount).clear()
        self.driver.find_element(*self.payamount).send_keys(amount)
        
        self.driver.find_element(*self.description).clear()
        self.driver.find_element(*self.description).send_keys(descript)
        
        self.driver.find_element(*self.submit).click()
        
    
    def is_transfer_succesfull(self):
        
        try:
            return len(self.driver.find_element(*self.successmsg)) > 0
        except Exception:
            return False