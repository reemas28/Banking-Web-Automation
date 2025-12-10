from pages.login_page import LoginPage

def test_invalid_input(setup):
    driver = setup
    driver.get("https://demo.guru99.com/V4/")
    
    login = LoginPage(driver)
    login.login("mngr64878", "sesedyu")
    
    try:
        alert = driver.switch_to.alert
        text = alert.text
        alert.accept()
        assert "User or Password is invalid" in text or len(text) >0
    except Exception:
        assert driver.title is None or "Manager" not in driver.title