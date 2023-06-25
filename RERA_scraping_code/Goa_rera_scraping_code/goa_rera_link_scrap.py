from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select
import time
import json

# driver=webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# time.sleep(2)
# driver.get('https://rera.goa.gov.in/reraApp')
# time.sleep(2)
# form_element=driver.find_element_by_css_selector('.form-control')

# # Create a Select object
# select = Select(form_element)

# # Choose an option by its value
# select.select_by_value('Project')

# driver.find_element_by_css_selector('.flipkart-navbar-button.btn.simp-search').click()
# time.sleep(1)

# project_link=[]
# link=driver.find_elements_by_css_selector('.col-md-9.no_pad_lft')
# for k in range(len(link)):
#     x=link[k].find_element_by_tag_name('a').get_attribute('href')
#     dic={'link':x}
#     project_link.append(dic)
# for i in range(10,1150,10):
#     # if i>860:
#     xpath_expression = f'//a[@href="javascript:pagging({str(i)})"]'
#     driver.find_element_by_xpath(xpath_expression).click()
#     time.sleep(12)
#     link=driver.find_elements_by_css_selector('.col-md-9.no_pad_lft')
#     for k in range(len(link)):
#         x=link[k].find_element_by_tag_name('a').get_attribute('href')
#         dic={'link':x}
#         project_link.append(dic)
#     with open('goa_rera_project_link1.json','w') as f:
#         json.dump(project_link,f)
    
#     print('====='+str(i)+'====')