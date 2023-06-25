import json
from tool_fun import file_list
from multiprocessing import process, Pool
from itertools import chain
from Process import process
import time
import warnings
warnings.filterwarnings('ignore')



if __name__ == '__main__':  
    # lst=[]
    box={}
    start = time.time()
    pool = Pool(processes=100)
    path=r"C:\Users\naveen.maurya\OneDrive - Aurum\scraped_data\rera\maha_rera_all_html_updated_feb_2023"
    file, rera =file_list(path)
    lst1=pool.starmap(process, zip(file, rera))
    lst2=list(chain(*lst1))
    box[rera]=lst2
    # lst.append(lst2)
    with open("maha_rera_all_project_feb_2023.json",'w') as f:
            json.dump(box,f)
    
    end = time.time()
    print('Time : ' , str(end-start))