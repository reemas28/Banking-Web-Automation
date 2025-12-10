from pages.login_page import LoginPage
from pages.fund_transfer_page import FundtransferPage

def test_valid_transfer(setup):
    driver = setup
    driver.get("https://demo.guru99.com/V4/")
    
    login = LoginPage(driver)
    login.login("mngr648546","zazaqen")
    
    ft = FundtransferPage(driver)
    ft.navigate_to_fundtransfer()
    
    ft.transfer(payer= '178849', payee='178850', amount=2000, descript= 'salary')
    
    assert ft.is_transfer_succesfull()