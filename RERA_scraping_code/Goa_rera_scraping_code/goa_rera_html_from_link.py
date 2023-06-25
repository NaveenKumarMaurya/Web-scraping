from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select
import time
import json
import requests
import urllib.request
import os


with open('goa_rera_project_link2.json','r') as f:
    data=json.laod(f)
# url = 'https://www.crematrix.com/rera-charter/redirect-rera-projects?rera_code='+str(df3['rera_id'][i])
for i in range(len(data)):
    
    url = 'https://www.crematrix.com/rera-charter/redirect-rera-projects?rera_code='+str(df['Application_No'][i])
    Web = requests.get(url)
    save_path = r'C:\Users\naveen.maurya\OneDrive - Aurum\scraped_data\rera\maha_rera_all_html_updated_feb_2023'
    completeName = os.path.join(save_path,str(df['Application_No'][i]) +".html") 
    f=open(completeName,'w')
    # f=open(str(df3['Rera_Id'][i])+'.html','w')
    # page=urllib.request.urlopen(url)
    # pagetext=str(page.read())
    # f.write(pagetext)
    f.write(str(Web.content))
    f.close()
    print('page'+str(i))