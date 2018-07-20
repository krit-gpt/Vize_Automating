from selenium import webdriver
from selenium.webdriver.support.ui import Select
import xlrd

driver = webdriver.Chrome('C:\\Users\\pragy\\Desktop\\Krit\\Vize\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://app.incentivizinggood.com/create-company-profile');

sheet = xlrd.open_workbook('C:\\Users\\pragy\\Desktop\\Book.xlsx')
file = sheet.sheet_by_index(0)

print(file.row_values(1))

name = driver.find_element_by_name("name")
# select = Select(driver.find_element_by_name('name'))

name.send_keys("hello")

email = driver.find_element_by_name("contactEmail")
email.send_keys("Email!!")

industry = driver.find_element_by_name("industry")
industry.send_keys("My Industry")

location = driver.find_element_by_name("locations.0")
location.send_keys("Tijuana")

contactinfo = driver.find_element_by_name("otherContactInfo")
contactinfo.send_keys("My Address")

websiteurl = driver.find_element_by_name("websiteURL")
websiteurl.send_keys("www.microsoft.com")

description = driver.find_element_by_name("descriptionOfCompany")
description.send_keys("Great company")






