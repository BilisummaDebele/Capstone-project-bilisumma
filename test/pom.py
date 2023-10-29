import time

from selenium import webdriver

from src.page.landingPage import LandingPage
from src.page.RegPage import RegPage
from src.page.LoginPage import LoginPage
from src.page.product_page import ProductPage
from src.page.order_page import OrderPage
from src.page.cart_page import CartPage

driver = webdriver.Firefox()
driver.get("http://shop.icraftsoft.net:8095/")
driver.maximize_window()

# Landing Page
lp = LandingPage(driver)# object create
lp.click_register()
time.sleep(3)

# Register username and password
rg = RegPage(driver)
rg.get_username()
time.sleep(3)
rg.getEmail()
time.sleep(3)
rg.getButton()
time.sleep(3)

# Login page
lg = LoginPage(driver)
lg.get_login()
time.sleep(2)
lg.login_textbox()
time.sleep(2)
lg.click_login()
time.sleep(2)
lg.click_home()
time.sleep(2)
lg.get_login_again()
time.sleep(2)

# ProductPage
pp = ProductPage(driver)
pp.search_box()
time.sleep(2)
pp.add_to_cart()
time.sleep(2)


# cart page
cart = CartPage(driver)
time.sleep(2)
cart.click_on_cart()
time.sleep(2)
cart.click_buy_now()
time.sleep(2)


# OrderPage
Ord = OrderPage(driver)
time.sleep(2)
Ord.click_on_Buynow()
time.sleep(2)
Ord.click_on_home()
time.sleep(2)
Ord.click_on_logout()
time.sleep(2)
