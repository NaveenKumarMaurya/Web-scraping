import pandas as pd
import pandas as pd
from selenium import webdriver
import time
import pandas as pd
from selenium import  webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager,IEDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.keys import Keys
import random as ra
import warnings
import requests
warnings.filterwarnings('ignore')

# df3=pd.read_csv('rera_id_mumbai.csv')
df=pd.read_json(r'C:\Users\naveen.maurya\Downloads\projects_gis_27022023.json')
import urllib.request
# url = 'https://www.crematrix.com/rera-charter/redirect-rera-projects?rera_code='+str(df3['rera_id'][i])
for i in range(len(df)):
    
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