import os
import warnings
import json
warnings.filterwarnings('ignore')
from bs4 import BeautifulSoup
from tool_fun import file_list,html_object,tool,tool1

path=r"C:\Users\naveen.maurya\OneDrive - Aurum\scraped_data\rera\Goa_Rera_html\project"
file=file_list(path)
box=[]
for j in range(len(file)):
    html_object1=html_object(path=path,count=j,file=file)
    
    if tool(html_object=html_object1,selector='.reg:nth-child(2)') is not None:
        registration=tool(html_object=html_object1,selector='.reg:nth-child(2)')
    else:
        registration=tool(html_object=html_object1,selector='.reg+ .reg')
    
    
    # if registration=='Registration Type : Company':
    project_name=tool(html_object=html_object1,selector='.col-md-9 h1')
    
    project_location=tool(html_object=html_object1,selector='.col-md-9 h1+ p')
    rera_id=tool(html_object=html_object1,selector='b')
        
                                                                
    date_of_registration=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(1) .col-xs-6:nth-child(2) p')
                                                            
    total_area_of_project_land=tool(html_object=html_object1,selector='.row:nth-child(1) .col-xs-6:nth-child(4) p')
    project_type=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(2) .col-xs-6:nth-child(2) p')
    project_status=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(3) .col-xs-6:nth-child(4) p')
    project_start_date=tool(html_object=html_object1,selector='.row:nth-child(2) .col-xs-6:nth-child(4) p')       
    project_end_date=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(3) .col-xs-6:nth-child(2) p')
                    

    if tool(html_object=html_object1,selector='.row:nth-child(4) .col-xs-6:nth-child(1) .text-right')=='Completion Certificate:':
        
        chalta_number=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(5) .col-xs-6:nth-child(2) p')
                                                            
        pt_sheet_num=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(5) .col-xs-6:nth-child(4) p')
    
        total_open_area=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(6) .col-xs-6:nth-child(2) p')
                                                               
        total_covered_area=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(6) .col-xs-6:nth-child(4) p')
                                                              
        state=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(7) .col-xs-6:nth-child(2) p')  
                                                  
        district=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(7) .col-xs-6:nth-child(4) p')   
                                                      
        village=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(8) .col-xs-6:nth-child(2) p') 
                                                                                         
        estimated_cost=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(8) .col-xs-6:nth-child(4) p')
                                                            
        number_of_garage=tool(html_object=html_object1,selector='.row:nth-child(9) .col-xs-6:nth-child(2) p')   
                                                                                                            
        area_of_garage=tool(html_object=html_object1,selector='.row:nth-child(9) .col-xs-6:nth-child(4) p')  
                                                                   
        number_of_open_parking=tool(html_object=html_object1,selector='.row:nth-child(10) .col-xs-6:nth-child(2) p')  
                                                                                                                    
        area_of_open_parking=tool(html_object=html_object1,selector='.row:nth-child(10) .col-xs-6:nth-child(4) p')  
                                                                                                                    
        number_of_covered_parking=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(11) .col-xs-6:nth-child(2) p')
                                                                                                                    
        area_of_covered_parking=tool(html_object=html_object1,selector='.row:nth-child(11) .col-xs-6:nth-child(4) p')
                                                                    
        number_of_covered_parking_sold=tool(html_object=html_object1,selector='.row:nth-child(12) .col-xs-6:nth-child(2) p')
                                                                      
        number_of_open_parking_sold=tool(html_object=html_object1,selector='.row:nth-child(12) .col-xs-6:nth-child(4) p')
                                                                    
    else:
        chalta_number=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(4) .col-xs-6:nth-child(2) p')
       
        pt_sheet_num=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(4) .col-xs-6:nth-child(4) p')
        
        total_open_area=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(5) .col-xs-6:nth-child(2) p')
        
        total_covered_area=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(5) .col-xs-6:nth-child(4) p')
       
        state=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(6) .col-xs-6:nth-child(2) p')
        
        district=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(6) .col-xs-6:nth-child(4) p')
                                                        # .row:nth-child(6) .col-xs-6:nth-child(4) p
        village=tool(html_object=html_object1,selector='.row:nth-child(7) .col-xs-6:nth-child(2) p')
        # .row:nth-child(8) .col-xs-6:nth-child(2) p
        estimated_cost=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(7) .col-xs-6:nth-child(4) p')
        
        number_of_garage=tool(html_object=html_object1,selector='.row:nth-child(8) .col-xs-6:nth-child(2) p')
        
        area_of_garage=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(8) .col-xs-6:nth-child(4) p ')
        
        number_of_open_parking=tool(html_object=html_object1,selector='.row:nth-child(9) .col-xs-6:nth-child(2) p')
        
        area_of_open_parking=tool(html_object=html_object1,selector='.row:nth-child(9) .col-xs-6:nth-child(4) p')
        
        number_of_covered_parking=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(10) .col-xs-6:nth-child(2) p')
        
        area_of_covered_parking=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(10) .col-xs-6:nth-child(4) p')
        
        number_of_covered_parking_sold=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(11) .col-xs-6:nth-child(2) p')
        
        number_of_open_parking_sold=tool(html_object=html_object1,selector='.profile_detail .row:nth-child(11) .col-xs-6:nth-child(4) p')
    
    
    
    # AUTHORIZED PERSON DETAIL
    A_name=tool(html_object=html_object1,selector='.martop:nth-child(8) td:nth-child(1)')
    A_mobile=tool(html_object=html_object1,selector='.martop:nth-child(8) td:nth-child(2)')
    A_email=tool(html_object=html_object1,selector='.martop:nth-child(8) td:nth-child(3)')
    A_adress=tool(html_object=html_object1,selector='.martop:nth-child(8) td:nth-child(4)')
    
    # PROJECT MEMBER DETAIL
    member_name=tool(html_object=html_object1,selector='.martop:nth-child(12) td:nth-child(1)')
    member_type=tool(html_object=html_object1,selector='.martop:nth-child(12) td:nth-child(2)')
    adress=tool(html_object=html_object1,selector='.martop:nth-child(12) td:nth-child(3)')
    pincode=tool(html_object=html_object1,selector='.martop:nth-child(12) td:nth-child(4)')
    
    if "Inventory DetailsType of InventoryNo of Inventory" in tool(html_object=html_object1,selector='.martop+ .inner_wrapper'):
            projet_launch_in_last_5year=None
    else:
        projet_launch_in_last_5year=tool(html_object=html_object1,selector='.martop+ .inner_wrapper')
    
    # ANNUAL STATEMENT OF ACCOUNT
    financial_year=tool1(html_object=html_object1,selector='#collapseFYStatus1 td:nth-child(1)')
    financial_year_start=tool1(html_object=html_object1,selector='#collapseFYStatus1 td:nth-child(2)')
    financial_year_end=tool1(html_object=html_object1,selector='#collapseFYStatus1 td:nth-child(3)')
    update_date=tool1(html_object=html_object1,selector='#collapseFYStatus1 td:nth-child(5)')
    
    # PROJECT QUARTERLY APPROVAL
    
    approval_taken_from=tool1(html_object=html_object1,selector='#collapseQuarterlyStatus1 td:nth-child(1)')
    reference_number=tool1(html_object=html_object1,selector='#collapseQuarterlyStatus1 td:nth-child(2)')
    date=tool1(html_object=html_object1,selector='#collapseQuarterlyStatus1 td:nth-child(3)')
    updated_on=tool1(html_object=html_object1,selector='#collapseQuarterlyStatus1 td:nth-child(4)')
    
    # BUILDING DETAILS
    building_details=tool1(html_object=html_object1,selector='.col-lg-6')
    complete_percentage=tool1(html_object=html_object1,selector='#collapseFYStatus3 .col-lg-3')
    
    # QUARTERLY EXTERNAL DEVELOPMENT
    facility_amenities=tool1(html_object=html_object1,selector='.col-lg-3 .control-label')
    praposed=tool1(html_object=html_object1,selector='.col-lg-3+ div')
    workdone_percentage=tool1(html_object=html_object1,selector='.col-lg-2+ div.col-lg-2')
    details=tool1(html_object=html_object1,selector='.col-lg-5 label')
    
    if registration=='Registration Type : Company':
        
        project_description=tool(html_object=html_object1,selector='.drop_shadow~ p')
        
        # PROMOTER DETAIL
        type_of_promoter=tool(html_object=html_object1,selector='.martop:nth-child(4) td:nth-child(1)')
        name=tool(html_object=html_object1,selector='.martop:nth-child(4) td:nth-child(2)')
        email=tool(html_object=html_object1,selector='.martop:nth-child(4) td:nth-child(3)')
        mobile=tool(html_object=html_object1,selector='.martop:nth-child(4) td:nth-child(4)')
        
        # QUARTERLY STATUS OF PROJECT
        number_of_inventory_completed=tool1(html_object=html_object1,selector='.table-responsive+ .table-responsive td:nth-child(1)')
        number_of_inventory_booked=tool1(html_object=html_object1,selector='.table-responsive+ .table-responsive td:nth-child(2)')
        number_of_inventory_sold=tool1(html_object=html_object1,selector='.table-responsive:nth-child(2) td~ td+ td')  
        
        # INVENTORY DETAILS
        type_of_inventory=tool1(html_object=html_object1,selector='.table-responsive:nth-child(1) .drop_shadow+ .table-bordered td:nth-child(1)')
        number_of_inventory=tool1(html_object=html_object1,selector='.table-responsive:nth-child(1) .drop_shadow+ .table-bordered td:nth-child(2)')
        carpet_area=tool1(html_object=html_object1,selector='.table-responsive:nth-child(1) .drop_shadow+ .table-bordered td:nth-child(3)')
        area_of_exclusive_balcony=tool1(html_object=html_object1,selector='.drop_shadow+ .table-bordered td:nth-child(4)')
        area_of_exclusive_open_terrace=tool1(html_object=html_object1,selector='.drop_shadow+ .table-bordered td:nth-child(5)')
         
    else:
        project_description=tool(html_object=html_object1,selector='#site-content .col-md-8 p')
        
        # PROMOTER DETAIL
        # type_of_promoter=tool(html_object=html_object1,selector='.martop:nth-child(4) td:nth-child(1)')
        type_of_promoter=None
        name=tool(html_object=html_object1,selector='.martop td:nth-child(1)')
        email=tool(html_object=html_object1,selector='.martop td:nth-child(2)')
        mobile=tool(html_object=html_object1,selector='.martop td~ td+ td')
        
        # QUARTERLY STATUS OF PROJECT
        number_of_inventory_completed=tool1(html_object=html_object1,selector='.table-responsive:nth-child(2) td:nth-child(1)')
        number_of_inventory_booked=tool1(html_object=html_object1,selector='.table-responsive:nth-child(2) td:nth-child(2)')
        number_of_inventory_sold=tool1(html_object=html_object1,selector='.table-responsive:nth-child(2) td~ td+ td')  
        
        type_of_inventory=tool1(html_object=html_object1,selector='.search_detail_grid .inner_wrapper .inner_wrapper .table-responsive:nth-child(1) td:nth-child(1)')
        number_of_inventory=tool1(html_object=html_object1,selector='.search_detail_grid .inner_wrapper .inner_wrapper .table-responsive:nth-child(1) td:nth-child(2)')
        carpet_area=tool1(html_object=html_object1,selector='.search_detail_grid .inner_wrapper .inner_wrapper .table-responsive:nth-child(1) td:nth-child(3)')
        area_of_exclusive_balcony=tool1(html_object=html_object1,selector='.search_detail_grid .inner_wrapper .inner_wrapper .table-responsive:nth-child(1) td:nth-child(4)')
        area_of_exclusive_open_terrace=tool1(html_object=html_object1,selector='.search_detail_grid .inner_wrapper .inner_wrapper .table-responsive:nth-child(1) td:nth-child(5)')
        
                                                                            
    x={'registration':registration,'rera_id':rera_id,'project_location':project_location,'project_name':project_name,
    'date_of_registration':date_of_registration,'total_area_of_project_land':total_area_of_project_land,
    'project_type':project_type,'project_status':project_status,'project_start_date':project_start_date,
    "project_end_date":project_end_date,'chalta_number':chalta_number,'pt_sheet_num':pt_sheet_num,'total_open_area':total_open_area,
    'total_covered_area':total_covered_area,'state':state,"district":district,'village':village,'estimated_cost':estimated_cost,
    "number_of_garage":number_of_garage,'area_of_garage':area_of_garage,'number_of_open_parking':number_of_open_parking,
    "area_of_open_parking":area_of_open_parking,'number_of_covered_parking':number_of_covered_parking,'area_of_covered_parking':
    area_of_covered_parking,'number_of_covered_parking_sold':number_of_covered_parking_sold,'number_of_open_parking_sold':
    number_of_open_parking_sold,'project_description':project_description,"PROMOTER DETAIL":{'type_of_promoter':type_of_promoter,
    "name":name,'email':email,'mobile':mobile},"AUTHORIZED PERSON DETAIL":{"name":A_name,"mobile":A_mobile,"email":A_email,
    "adress":A_adress},"PROJECT MEMBER DETAIL":{"member_name":member_name,"member_type":member_type,"adress":adress,
    "pincode":pincode},'projet_launch_in_last_5year':projet_launch_in_last_5year,
    'QUARTERLY STATUS OF PROJECT':{'number_of_inventory_completed':number_of_inventory_completed,'number_of_inventory_booked':
    number_of_inventory_booked,'number_of_inventory_sold':number_of_inventory_sold},"ANNUAL STATEMENT OF ACCOUNT":{
    "financial_year":financial_year,'financial_year_start':financial_year_start,"financial_year_end":financial_year_end,
    "update_date":update_date},"PROJECT QUARTERLY APPROVAL":{"approval_taken_from":approval_taken_from,"reference_number":
    reference_number,"date":date,"updated_on":updated_on},
    "BUILDING_DETAILS":
    {'building_details':building_details,'complete_percentage':complete_percentage},
    "INVENTORY DETAILS":{'type_of_inventory':type_of_inventory,'number_of_inventory':number_of_inventory,'carpet_area':
    carpet_area,'area_of_exclusive_balcony':area_of_exclusive_balcony,'area_of_exclusive_open_terrace':area_of_exclusive_open_terrace},
    "QUARTERLY EXTERNAL DEVELOPMENT":{
    "facility_amenities":facility_amenities,"praposed":praposed, "workdone_percentage":workdone_percentage,"details":details}}
    
    box.append(x)
    with open('test.json','w') as f:
        json.dump(box,f)
    print('====='+str(j))
                                                                