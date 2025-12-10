from pages.login_page import LoginPage

def test_valid_login(setup):
    driver = setup
    driver.get("https://demo.guru99.com/V4/")
    
    login = LoginPage(driver)
    login.login("mngr648546", "zazaqen")
    
    assert "Manager" in driver.title
    