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
warnings.filterwarnings('ignore')

df3=pd.read_csv('rera_id.csv')





# driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://maharerait.mahaonline.gov.in/')
time.sleep(3)

all_data=[]
timme=[1,2,3]
for i in range(len(df3)):
    url ='https://www.crematrix.com/rera-charter/redirect-rera-projects?rera_code='+str(df3['rera_id'][i])
    driver.execute_script("window.open('');")
    time.sleep(ra.choice(timme))
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)
    print('********rera page no__'+str(i)+'__is open*********')
    time.sleep(ra.choice(timme))
    
    x=driver.find_elements_by_css_selector('.x_content')
    #rera_id
    try:
        rera_id=df3['rera_id'][i]
    except:
        rera_id='NA'
    #information type
    try:
        x1=x[0].find_elements_by_css_selector('.col-md-3.col-sm-3')
        information_type=x1[1].text
        print('==information type scraped==')
    except:
        information_type='NA'
    ##############################################################################################   
    x2=x[1].find_elements_by_css_selector('.col-md-3.col-sm-3')
    
    # organization name
    try:
        org_name=[]
        for i in range(len(x2)):
            if x2[i].text.startswith('Name'):
                org_name.append(x2[i+1].text)
            elif x2[i].text.startswith('First Name'):
                org_name.append(x2[i+1].text)   
        organization_name=org_name
        print('==organization name scraped==')
    except:
        organization_name='NA'
        
        
        
    # organization type
    try:
        Org_Type=[]
        for i in range(len(x2)):
            if x2[i].text.startswith('Organization Type'):
                Org_Type.append(x2[i+1].text)
        organization_type=Org_Type
        print('==organization type scraped==')
    except:
        organization_type='NA'
    
    # other type of organization description
    try:
        other_Org_desc=[]
        for i in range(len(x2)):
            if x2[i].text.startswith('Description For Other Type Organization'):
                other_Org_desc.append(x2[i+1].text)
        other_org_description=other_Org_desc
        print('==description for other organization type scraped==')
    except:
        other_org_description='NA'
    # past experience    
    try:
        past_exp=[]
        for i in range(len(x2)):
            if x2[i].text.startswith('Do you have any Past Experience'):
                past_exp.append(x2[i+1].text)
        past_experience=past_exp
        print('==past_experience  scraped==')
    except:
        past_experience='NA'
    
    # Building name
    try:
        Build_name=[]
        for i in range(len(x2)):
            if x2[i].text.startswith('Building Name'):
                Build_name.append(x2[i+1].text)
        Building_Name=Build_name
        print('==Building name scraped==')
    except:
        Building_Name='NA'
    
    
    # Street Name
    try:
        Street_Name=[]
        for i in range(len(x2)):
            if x2[i].text.startswith('Street Name'):
                Street_Name.append(x2[i+1].text)
        street_Name=Street_Name
        print('==street name scraped==')
    except:
        street_Name='NA'
        
    
    # Locality
    try:
        Locality=[]
        for i in range(len(x2)):
            if x2[i].text.startswith('Locality'):
                Locality.append(x2[i+1].text)
        locality=Locality
        print('==locality scraped==')
    except:
        locality='NA'
    
    
    # land mark
    try:
        Landmark=[]
        for i in range(len(x2)):
            if x2[i].text.startswith('Land mark'):
                Landmark.append(x2[i+1].text)
            elif x2[i].text.startswith('Landmark'):
                Landmark.append(x2[i+1].text)
        landmark=Landmark
        print('==landmark scraped==')
    except:
        landmark='NA'
        
    # Locality
    try:
        Pin_Code=[]
        for i in range(len(x2)):
            if x2[i].text.startswith('Pin Code'):
                Pin_Code.append(x2[i+1].text)
        pin_code=Pin_Code
        print('==pin_code scraped==')
    except:
        pin_code='NA'
        
     # office_number
    try:
        Office_Number=[]
        for i in range(len(x2)):
            if x2[i].text.startswith('Office Number'):
                Office_Number.append(x2[i+1].text)
        office_number=Office_Number
        print('==office_number scraped==')
    except:
        office_number='NA'
    
    
     # Website URL
    try:
        Website_URL=[]
        for i in range(len(x2)):
            if x2[i].text.startswith('Website URL'):
                Website_URL.append(x2[i+1].text)
        website_URL=Website_URL
        print('==website_URL scraped==')
    except:
        website_URL='NA'
    ###############################################################################################
    x3=x[2].find_elements_by_css_selector('.col-md-3.col-sm-3')
    
    # Project Name
    try:
        Project_Name=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Project Name'):
                Project_Name.append(x3[i+1].text)
        project_name=Project_Name
        print('==project_name scraped==')
    except:
        project_name='NA'
        
    # Project Status
    try:
        Project_Status=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Project Status'):
                Project_Status.append(x3[i+1].text)
        project_status=Project_Status
        print('==project_status scraped==')
    except:
        project_status='NA'
    
    # Proposed Date of Completion
    try:
        Completion_date=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Proposed Date of Completion'):
                Completion_date.append(x3[i+1].text)
        completion_date=Completion_date
        print('==completion_date scraped==')
    except:
        completion_date='NA'
    
    # Litigations related to the project
    try:
        Litigations=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Proposed Date of Completion'):
                Litigations.append(x3[i+1].text)
        litigations=Litigations
        print('==litigations scraped==')
    except:
        litigations='NA'
    
    # Project Type
    try:
        Project_Type=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Project Type'):
                Project_Type.append(x3[i+1].text)
        project_type=Project_Type
        print('==project_type scraped==')
    except:
        project_type='NA'
    
    
    # Are there any Promoter(Land Owner/ Investor) (as defined by MahaRERA Order) in the project ?
    try:
        any_Promoter=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Are there any Promoter(Land Owner/ Investor) (as defined by MahaRERA Order) in the p'):
                any_Promoter.append(x3[i+1].text)
        Any_Promoter=any_Promoter
        print('==Any_Promoter scraped==')
    except:
        Any_Promoter='NA'
    
    # Plot Bearing No
    try:
        Plot_Bearing_No=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Plot Bearing No / CTS no / Survey Number/Final Plot no'):
                Plot_Bearing_No.append(x3[i+1].text)
        plot_bearing_no=Plot_Bearing_No
        print('==plot_bearing_no scraped==')
    except:
        plot_bearing_no='NA'
        
    
    #Boundaries East
    try:
        Boundaries_East=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Boundaries East'):
                Boundaries_East.append(x3[i+1].text)
        boundaries_east=Boundaries_East
        print('==boundaries_east scraped==')
    except:
        boundaries_east='NA'
        
    #Boundaries West
    try:
        Boundaries_West=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Boundaries West'):
                Boundaries_West.append(x3[i+1].text)
        boundaries_west=Boundaries_West
        print('==boundaries_west scraped==')
    except:
        boundaries_west='NA'
        
    #Boundaries North
    try:
        Boundaries_North=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Boundaries North'):
                Boundaries_North.append(x3[i+1].text)
        boundaries_north=Boundaries_North
        print('==boundaries_north scraped==')
    except:
        boundaries_north='NA' 
    
    
    #Boundaries South
    try:
        Boundaries_South=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Boundaries North'):
                Boundaries_South.append(x3[i+1].text)
        boundaries_south=Boundaries_South
        print('==boundaries_north scraped==')
    except:
        boundaries_south='NA' 
    
    #State/UT
    try:
        State_UT=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('State/UT'):
                State_UT.append(x3[i+1].text)
        state_ut=State_UT
        print('==state_ut scraped==')
    except:
        state_ut='NA' 
    
    #Division
    try:
        Division=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Division'):
                Division.append(x3[i+1].text)
        division=Division
        print('==division scraped==')
    except:
        division='NA' 
    
    
    #District
    try:
        District=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Division'):
                District.append(x3[i+1].text)
        district=District
        print('==district scraped==')
    except:
        district='NA' 
    
    
     #Taluka
    try:
        Taluka=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Taluka'):
                Taluka.append(x3[i+1].text)
        taluka=Taluka
        print('==taluka scraped==')
    except:
        taluka='NA' 
    
     # Project Village
    try:
        Project_Village=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Village'):
                Project_Village.append(x3[i+1].text)
        project_village=Project_Village
        print('==project_village scraped==')
    except:
        project_village='NA'
        
    #project Street    
    try:
        Project_Street=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Street'):
                Project_Street.append(x3[i+1].text)
        project_street=Project_Street
        print('==project_street scraped==')
    except:
        project_street='NA'
    
    #Project_Locality    
    try:
        Project_Locality=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Locality'):
                Project_Locality.append(x3[i+1].text)
        project_locality=Project_Locality
        print('==project_locality scraped==')
    except:
        project_locality='NA'
        
    #Pin Code    
    try:
        Project_Pin_Code=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Pin Code'):
                Project_Pin_Code.append(x3[i+1].text)
        project_pin_code=Project_Pin_Code
        print('==project_pin_code scraped==')
    except:
        project_pin_code='NA'
        
    #Area(In sqmts)   
    try:
        Area=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Area(In sqmts)'):
                Area.append(x3[i+1].text)
        area=Area
        print('==area scraped==')
    except:
        area='NA'
       
    #Total Building Count  
    try:
        Total_Building_Count=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Total Building Count'):
                Total_Building_Count.append(x3[i+1].text)
        total_building_count=Total_Building_Count
        print('==total_building_count scraped==')
    except:
        total_building_count='NA'
        
    #Is project plan sanctioned by MCGM?  
    try:
        Sanctioned_by_MCGM=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Is project plan sanctioned by MCGM?'):
                Sanctioned_by_MCGM.append(x3[i+1].text)
        sanctioned_by_MCGM=Sanctioned_by_MCGM
        print('==sanctioned_by_MCGM scraped==')
    except:
        sanctioned_by_MCGM='NA'    
    
    
    #Sanctioned_Buildings_Count 
    try:
        Sanctioned_Buildings_Count=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Sanctioned Buildings Count'):
                Sanctioned_Buildings_Count.append(x3[i+1].text)
        sanctioned_buildings_count=Sanctioned_Buildings_Count
        print('==sanctioned_buildings_count scraped==')
    except:
        sanctioned_buildings_count='NA'
    
    #Proposed But Not Sanctioned Buildings Count
    try:
        Not_Sanctioned_Buildings=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Proposed But Not Sanctioned Buildings Count'):
                Not_Sanctioned_Buildings.append(x3[i+1].text)
        not_sanctioned_buildings=Not_Sanctioned_Buildings
        print('==not_sanctioned_buildings scraped==')
    except:
        not_sanctioned_buildings='NA'
    
    #Aggregate area(In sqmts) of recreational open space
    try:
        Aggregate_area=[]
        for i in range(len(x3)):
            if x3[i].text.startswith('Aggregate area(In sqmts) of recreational open space'):
                Aggregate_area.append(x3[i+1].text)
        aggregate_area=Aggregate_area
        print('==aggregate_area scraped==')
    except:
        aggregate_area='NA'
        
    ############################################################################################################
    x4=x[4].find_elements_by_css_selector('.col-md-3.col-sm-3')
    
    
    #Built-up-Area as per Proposed FSI 
    try:
        Built_up_Area_as_per_Proposed_FSI=[]
        for i in range(len(x4)):
            if x4[i].text.startswith('Built-up-Area as per Proposed FSI '):
                Built_up_Area_as_per_Proposed_FSI.append(x4[i+1].text)
        built_up_Area_as_per_Proposed_FSI=Built_up_Area_as_per_Proposed_FSI
        print('==Built_up_Area_as_per_Proposed_FSI scraped==')
    except:
        built_up_Area_as_per_Proposed_FSI='NA'
    
    #Built-up-Area as per Approved FSI 
    try:
        Built_up_Area_as_per_Approved_FSI=[]
        for i in range(len(x4)):
            if x4[i].text.startswith('Built-up-Area as per Approved FSI'):
                Built_up_Area_as_per_Approved_FSI.append(x4[i+1].text)
        built_up_Area_as_per_Approved_FSI=Built_up_Area_as_per_Approved_FSI
        print('==Built_up_Area_as_per_Approved_FSI scraped==')
    except:
        built_up_Area_as_per_Approved_FSI='NA'
        
    
    #TotalFSI 
    try:
        TotalFSI=[]
        for i in range(len(x4)):
            if x4[i].text.startswith('TotalFSI'):
                TotalFSI.append(x4[i+1].text)
        totalFSI=TotalFSI
        print('==TotalFSI scraped==')
    except:
        totalFSI='NA'
        
    ##########################################################################################
    x5=x[5].find_elements_by_css_selector('.col-md-3.col-sm-3')
    
    #bank name
    try:
        Bank_Name=[]
        for i in range(len(x5)):
            if x5[i].text.startswith('Bank Name'):
                Bank_Name.append(x5[i+1].text)
        bank_name=Bank_Name
        print('==bank_name scraped==')
    except:
        bank_name='NA'
    
    #IFSC Code
    try:
        IFSC_Code=[]
        for i in range(len(x5)):
            if x5[i].text.startswith('IFSC Code'):
                IFSC_Code.append(x5[i+1].text)
        ifsc_Code=IFSC_Code
        print('==ifsc_Code scraped==')
    except:
        ifsc_Code='NA'
        
    detail={'rera_id':rera_id,'information_type':information_type,'organization_name':organization_name,'organization_type':
           organization_type,'other_org_description':other_org_description,'past_experience':past_experience,'Building_Name':
           Building_Name,'street_Name':street_Name,'locality':locality,'landmark':landmark,'pin_code':pin_code,
           'office_number':office_number,'website_URL':website_URL,'project_name':project_name,'project_status':project_status,
           'completion_date':completion_date,'litigations':litigations,'project_type':project_type,'Any_Promoter':
           Any_Promoter,'plot_bearing_no':plot_bearing_no,'boundaries_east':boundaries_east,'boundaries_west':boundaries_west,
           'boundaries_north':boundaries_north,'boundaries_south':boundaries_south,'state_ut':state_ut,'division':division,
           'district':district,'taluka':taluka,'project_street':project_street,'project_locality':project_locality,
           'project_pin_code':project_pin_code,'area':area,'total_building_count':total_building_count,'sanctioned_by_MCGM':
           sanctioned_by_MCGM,'sanctioned_buildings_count':sanctioned_buildings_count,'not_sanctioned_buildings':
           not_sanctioned_buildings,'aggregate_area':aggregate_area,'built_up_Area_as_per_Proposed_FSI':built_up_Area_as_per_Proposed_FSI,
           'built_up_Area_as_per_Approved_FSI':built_up_Area_as_per_Approved_FSI,'totalFSI':totalFSI,'bank_name':bank_name,
           'ifsc_Code':ifsc_Code}
    
    all_data.append(detail)
    df=pd.DataFrame(all_data)
    df.to_csv('rera.csv', mode='a', header=not os.path.exists('rera.csv'),index=False)
    print('==data saved==')
    driver.close()
    time.sleep(ra.choice(timme))
    driver.switch_to.window(driver.window_handles[0])

