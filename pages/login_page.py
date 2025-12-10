from selenium.webdriver.common.by import By

class LoginPage:
    
    def __init__(self,driver):
        self.driver = driver
        self.username = (By.NAME,"uid")
        self.password = (By.NAME, "password")
        self.loginbtn = (By.NAME, "btnLogin")
        
    
    def enter_username(self,user):
        self.driver.find_element(*self.username).clear()
        self.driver.find_element(*self.username).send_keys(user)
        
    
    def enter_password(self,pw):
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(pw)
        
    
    def click_login(self):
        self.driver.find_element(*self.loginbtn).click()
        
    
    def login(self, user, pw):
        self.enter_username(user)
        self.enter_password(pw)
        self.click_login()
        