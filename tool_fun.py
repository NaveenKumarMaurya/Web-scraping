import os
from bs4 import BeautifulSoup
def file_list(path):
    file=[]
    for i in os.listdir(path):
        if i.endswith('.html'):
            file.append(i)
    return file

def html_object(path,count,file):
    sample_file=path +"\\" +file[count]
    size=os.path.getsize(sample_file)
    if size>90:
        with open(sample_file, 'r', encoding='utf-8', newline='') as f:
            page = f.read()
            html_object = BeautifulSoup(page)
    return html_object

def tool(html_object,selector):
    try:
        x=html_object.select(selector)
        x1=x[0].text
        x2=x1.replace('\\r\\n','')
        x3=x2.strip()
        return x3
    except:
        pass

def tool1(html_object,selector):
    lst=[]
    x=html_object.select(selector)
    for k in range(len(x)):
        x1=x[k].text
        x2=x1.replace('\\r\\n','')
        x3=x2.replace('\\t','')
        x4=x3.strip()
        lst.append(x4)
    return lst









        