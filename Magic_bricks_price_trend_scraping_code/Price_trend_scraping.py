import urllib.request
import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm
import re
import pandas as pd
from selenium import webdriver
import time
import numpy as np
import pandas as pd
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import random as ra
from selenium.webdriver.common.by import By
import time
import random as ra
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import warnings
from itertools import chain
# list(chain(*nested_list))
warnings.filterwarnings('ignore')
start = time.time()

box={}
# driver=webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# driver=webdriver.Chrome(executable_path=r"C:/Users/naveen.maurya/Downloads/chromedriver_win32/chromedriver.exe")

mumbai=[]
for i in range(1,11):
    driver.get("https://www.magicbricks.com/Property-Rates-Trends/ALL-RESIDENTIAL-rates-in-Kolkata/Page-"+str(i))
    time.sleep(ra.choice([1,2,3]))
    x=driver.find_element_by_id("localitySec")
    mumbai.append(x.text.split('\n'))
    time.sleep(1)
    print('===page=='+str(i))
print('====location scraped===')
Mumbai=list(chain(*mumbai))

for k in Mumbai:
    link="https://www.magicbricks.com/Property-Rates-Trends/Multistorey-Apartment-rates-"+str(k)+"-in-Kolkata"
    # https://www.magicbricks.com/Property-Rates-Trends/Multistorey-Apartment-rates-Bhosale-Nagar-in-Pune
    Web = requests.get(link)
    Parse = BeautifulSoup(Web.text, 'html')
    x=Parse.find_all('script', type='text/javascript')
    x1=x[38]
    x2=x1.text.replace('\n','').replace('\t','')
    x3=x2.split(';')
    
    lr=[]
    avr=[]
    ur=[]
    qr=[]
    for i in x3:
        if '.push' in i:
            if 'lowerRange.push' in i:
                l=re.findall('-?\d+\.?\d*', i)
                lr.append(l)
            if 'averageRange.push' in i:
                l=re.findall('-?\d+\.?\d*', i)
                avr.append(l)
            if 'upperRange.push' in i:
                l=re.findall('-?\d+\.?\d*', i)
                ur.append(l)
            if 'quartrValues.push' in i:
                l=re.findall('\(+(.*?)\)',i)
                qr.append(l)
    
    lower=list(chain(*lr))
    average=list(chain(*avr))
    upper=list(chain(*ur))
    quarter=list(chain(*qr))
    
    quart=[]
    for j in range(len(quarter)):
        x=quarter[j].replace('"',"")
        quart.append(x)
    
    box[k]={}
    box[k]['upperRange']=upper
    box[k]['lowerRange']=lower
    box[k]['averageRange']=average
    box[k]['quartrValues']=quart
    time.sleep(ra.choice([26,10,15,20,8,5,7,30,25]))
    with open("price_trend_kolkata.json",'w') as f:
        json.dump(box,f)
    print('======'+str(k)+'===')
end = time.time()
p=end - start
print('**********excution time of the code is=======',p//3600,'hour',p//60,'minute',p%60,'second')