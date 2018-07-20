from selenium import webdriver
from selenium.webdriver.support.ui import Select
import xlrd


sheet = xlrd.open_workbook('C:\\Users\\pragy\\Desktop\\Book.xlsx')
file = sheet.sheet_by_index(0)

# print(file.row_values(0))
# print(file.row_values(1))

'''
1-50
51 - 500
501 - 2000
2001 - 5000
5000+
'''

driver = webdriver.Chrome('C:\\Users\\pragy\\Desktop\\Krit\\Vize\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://vize-staging-0.meteorapp.com/create-company-profile')

#TODO - Button, for loop for all the entries, Julian clarifications
for i in range(3,14):
    data = file.row_values(i)
    name_data = data[0]
    contact_info_data = data[1]
    location_data = data[2]
    email_data = data[3]
    size_data = data[4]
    industry_data = data[5]
    url_data = data[6]
    description_data = data[7]

    if size_data <= 50:
        size_data = "1 - 50"
    elif size_data <= 500:
        size_data = "51 - 500"
    elif size_data <= 2000:
        size_data = "501-2000"
    elif size_data <= 5000:
        size_data = "2001 - 5000"
    else:
        size_data = "5000+"





    # ------------------------------WRITING CODE---------------------------

    # driver = webdriver.Chrome('C:\\Users\\pragy\\Desktop\\Krit\\Vize\\chromedriver.exe')  # Optional argument, if not specified will search path.
    # driver.get('https://vize-staging-0.meteorapp.com/create-company-profile');

    name = driver.find_element_by_name("name")
    name.send_keys(name_data)

    email = driver.find_element_by_name("contactEmail")
    email.send_keys(email_data)

    nemps = driver.find_element_by_name("numEmployees")
    nemps.send_keys(size_data)

    industry = driver.find_element_by_name("industry")
    industry.send_keys(industry_data)

    location = driver.find_element_by_name("locations.0")
    location.send_keys(location_data)

    contactinfo = driver.find_element_by_name("otherContactInfo")
    contactinfo.send_keys(contact_info_data)

    websiteurl = driver.find_element_by_name("websiteURL")
    websiteurl.send_keys(url_data)

    description = driver.find_element_by_name("descriptionOfCompany")
    description.send_keys(description_data)

    log_but2 = "//button[@type='submit']"
    driver.find_element_by_xpath(log_but2).click()
    # button1 = driver.find_element_by_class_name("btn-primary")
    # button1.click()

    driver.implicitly_wait(10)
    # button2 = driver.find_element_by_css_selector("button.btn.btn-default")
    # button2.click()

    # driver.implicitly_wait(5)






