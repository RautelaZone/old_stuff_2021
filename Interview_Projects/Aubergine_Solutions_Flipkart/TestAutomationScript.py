from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

"""
Logger configuration
"""
logging.basicConfig(filename="test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    )

logger = logging.getLogger()
logger.setLevel(logging.INFO)
"""
Credentials and Values
"""

URL = "https://www.google.com/"
value = "Filpkart"
myPincode = "121001"
otherPincode = "121002"
listURL = "https://www.flipkart.com/home-kitchen/home-appliances/air-conditioners/window~type/pr?sid=j9e%2Cabm%2Cc54&otracker=nmenu_sub_TVs+%26+Appliances_0_Window+ACs&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&fm=neo%2Fmerchandising&iid=M_e18ed58a-f8ca-473b-a8fc-8b51a41e29c1_1_372UD5BXDFYS_MC.CRYRXZFTEPW5&otracker=hp_rich_navigation_5_1.navigationCard.RICH_NAVIGATION_Appliances~Air%2BConditioners~Window%2BACs_CRYRXZFTEPW5&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_5_L2_view-all&cid=CRYRXZFTEPW5"

"""
This method will add products to cart one by one.
"""


def addingToCart():
    handles = driver.window_handles
    parentWindow = driver.current_window_handle
    size = len(handles)
    for x in range(size):
        driver.switch_to.window(handles[x])
    driver.implicitly_wait(3)
    addToCartButton = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")))
    addToCartButton.click()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Total Amount')]")))
    driver.close()
    driver.switch_to.window(parentWindow)
    driver.get(listURL)
    driver.implicitly_wait(3)


"""
Added the cases for Cross Browsers- firefox, and chrome
"""
browser = input("Enter browser name (Chrome/Firefox): ")
if browser.startswith('firefox') or browser.startswith('Firefox') or browser.startswith('ff'):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browser.startswith("chrome") or browser.startswith("Chrome"):
    driver = webdriver.Chrome(ChromeDriverManager().install())
else:
    logger.error("Invalid broswer.")
    raise Exception('Please provide valid browser name...')


print("-" * 70)
print("Launching Browser........")
logger.info("Launching Browser........")
print("-" * 70)
driver.get(URL)

driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element_by_xpath("//input[@title='Search']").click()
driver.find_element_by_xpath("//input[@title='Search']").clear()
driver.find_element_by_xpath("//input[@title='Search']").send_keys(value)
print(f"{value} is searched...")
logger.info("Text 'Flikart' is searched.")
print("-" * 70)

driver.implicitly_wait(3)
results = driver.find_elements_by_xpath("//div[@class='pcTkSc']")
print(f"Total searched item related to {value} is:", len(results))
print(f"Searched items related to {value} are:")
for result in results:
    print(result.text)
logger.info("Searched item list has been printed to console.")
print("-" * 70)

driver.find_element_by_xpath("//input[@title='Search']").send_keys(Keys.ENTER)
driver.implicitly_wait(5)
driver.find_element_by_xpath("//span[@class='ellip' and contains(text(),'flipkart.com')]").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//button[contains(text(),'✕')]").click()
driver.implicitly_wait(3)
print("Pop-up has been closed...")
logger.info("Pop-up has been closed...")
print("-" * 70)
logoPresent = driver.find_element_by_xpath("//img[@title='Flipkart']").is_displayed()
assert logoPresent == True, "Title didn't match"
logger.info("Landed to Flipkart website.")
print(f"Landed to {value} website...")
print("-" * 70)

"""
Mouse hovering to items to navigate to Window AC Category
"""
action = ActionChains(driver)
appliance_menu = driver.find_element_by_xpath("//img[@alt='Appliances']")
action.move_to_element(appliance_menu).perform()
driver.implicitly_wait(2)
AC_menu = driver.find_element_by_xpath("//a[contains(text(),'Air Conditioners')]")
action.move_to_element(AC_menu).perform()
driver.implicitly_wait(2)
windowACMenu = driver.find_element_by_xpath("//a[contains(text(),'Window ACs')]")
action.move_to_element(windowACMenu).click().perform()
logger.info("Clicked to Window AC Category.")
print("Navigated to Window AC Category...")
print("-" * 70)

value1 = 2
value2 = 3
value3 = 6
driver.implicitly_wait(5)
secEle = driver.find_element_by_xpath(
    "//label[@class='_2iDkf8']//following::span[contains(text(),'Add to Compare')][2]").click()
thirdEle = driver.find_element_by_xpath(
    "//label[@class='_2iDkf8']//following::span[contains(text(),'Add to Compare')][3]").click()
sixthEle = driver.find_element_by_xpath(
    "//label[@class='_2iDkf8']//following::span[contains(text(),'Add to Compare')][6]").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//span[contains(text(),'COMPARE')]").click()
itemList = driver.find_elements_by_xpath("//a[@class='_3L_M2k']")

logger.info("Compared three products...")
print("Comparing three products...")
print("-" * 70)

"""
Listing Products
"""
print("Products are: ")
uniqueProd = []
uniquePrice = []
for item in itemList:
    products = item.text
    if products not in uniqueProd:
        uniqueProd.append(products)
for item in uniqueProd:
    print(item)
logger.info("Product list has been printed to console.")
print("-" * 70)

"""
Listing Products' Price
"""
priceList = driver.find_elements_by_xpath("//div[@class='_30jeq3']")
print("Price of products are:")
for item in priceList:
    prices = item.text
    if prices not in uniquePrice:
        uniquePrice.append(prices)

price1 = uniquePrice[0]
price2 = uniquePrice[1]
price3 = uniquePrice[2]

for item in uniquePrice:
    print(item)
logger.info("Price list has been printed to console.")
print("-" * 70)

item1 = "Voltas 1.5 Ton 3 Star Window AC  - White"
item2 = "Voltas 1.5 Ton 3 Star Window AC  - White"
item3 = "Blue Star 1.5 Ton 5 Star Window AC  - White"

"""
Calling method 'addingToCart()'
"""
driver.get(listURL)
driver.find_element_by_xpath("//div[contains(text(),'" + item1 + "')]").click()
addingToCart()

driver.find_element_by_xpath("//div[contains(text(),'" + item2 + "')]").click()
addingToCart()

driver.find_element_by_xpath("//div[contains(text(),'" + item3 + "')]").click()
addingToCart()
driver.refresh()

logger.info("All three items have been added to cart.")
print(f"Following products have been added to cart:\n{item1}\n{item2}\n{item3}")
print("-" * 70)

"""
Checking availability and Printing message for native area pincode
"""
driver.find_element_by_xpath("//a[@class='_3SkBxJ']").click()
driver.find_element_by_xpath("//input[@placeholder='Enter delivery pincode']").clear()
driver.find_element_by_xpath("//input[@placeholder='Enter delivery pincode']").send_keys(myPincode)
driver.find_element_by_xpath("//span[contains(text(),'Check')]").click()
deliveryMsg = driver.find_elements_by_xpath("//div[@class='_2pqhhf']")
print(f"Availability/Delivery Messages for pincode {myPincode}: ")
for msg in deliveryMsg:
    print(msg.text)
logger.info("Availability/Delivery Messages for relative pincodes have been printed.")
print("-" * 70)

"""
Checking availability and Printing messaged for other area pincode
"""
driver.find_element_by_xpath("//div[@class='_12cXX4']").click()
driver.find_element_by_xpath("//input[@placeholder='Enter delivery pincode']").clear()
driver.find_element_by_xpath("//input[@placeholder='Enter delivery pincode']").send_keys(otherPincode)
driver.find_element_by_xpath("//span[contains(text(),'Check')]").click()
driver.implicitly_wait(10)
deliveryMsg = driver.find_elements_by_xpath("//div[@class='_2pqhhf']")
print(f"Availability/Delivery Messages for pincode {otherPincode}: ")
for msg in deliveryMsg:
    print(msg.text)
print("-" * 70)

driver.quit()
print("Closing the browser...")
logger.info("Closing the browser.")
logger.info("================================================= END =========================================")
print("-" * 70)
