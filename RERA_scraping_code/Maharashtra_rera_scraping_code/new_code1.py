import os
import warnings
import json
warnings.filterwarnings('ignore')
from bs4 import BeautifulSoup
from tool_fun import file_list,html_object,tool,tool1
path=r"C:\Users\naveen.maurya\Downloads\maha_rera_1"
file=file_list(path)
for j in range(len(file)):
    # if j>22174:
    html_object1=html_object(path=path,count=j,file=file)
            
    
    general_information={}
    #information type
    
    general_information['information_type']=tool(html_object=html_object1,selector="#divInfoType .col-sm-3+ .col-sm-3")
    
    # ORGANIZATION     
    organization={}
    try:
        organization['organization_name']=tool(html_object=html_object1,selector="#fldFirm .row:nth-child(1) .col-sm-3+ .col-sm-3")
    except:
        pass
    try:
        organization['organization_type']=tool(html_object=html_object1,selector="#fldFirm .row:nth-child(2) .col-sm-3:nth-child(2)")
    except:
        pass
    try:
        organization['other_description']=tool(html_object=html_object1,selector="#fldFirm .row:nth-child(2) .col-sm-3:nth-child(4)")
    except:
        pass
    try:
        organization['past_experience']=tool(html_object=html_object1,selector="#fldFirm .row:nth-child(3) .col-sm-3+ .col-sm-3")
    except:
        pass
    # ADDRESS DETAIL
    adress_detail={}
    try:
        adress_detail['block_number']=tool(html_object=html_object1,selector="#fldFirm .row:nth-child(7) .col-sm-3:nth-child(2)")
    except:
        pass
    adress_detail['building_name']=tool(html_object=html_object1,selector=".x_title+ .row .col-sm-3:nth-child(4)")
    try:
        adress_detail['street_name']=tool(html_object=html_object1,selector="#fldFirm .row:nth-child(8) .col-sm-3:nth-child(2)")
    except:
        pass
    try:
        adress_detail['locality']=tool(html_object=html_object1,selector="#fldFirm .row:nth-child(8) .col-sm-3:nth-child(4)")
    except:
        pass
    adress_detail['landmark']=tool(html_object=html_object1,selector='.row:nth-child(9) .col-sm-3:nth-child(2)')
    adress_detail['state']=tool(html_object=html_object1,selector=".row:nth-child(9) .col-sm-3:nth-child(4)")
    adress_detail['division']=tool(html_object=html_object1,selector=".row:nth-child(10) .col-sm-3:nth-child(2)")
    adress_detail['district']=tool(html_object=html_object1,selector=".row:nth-child(10) .col-sm-3:nth-child(4)")
    adress_detail['district']=tool(html_object=html_object1,selector=".row:nth-child(12) .col-sm-3+ .col-sm-3")
    adress_detail['taluka']=tool(html_object=html_object1,selector=".row:nth-child(11) .col-sm-3:nth-child(2)")
    adress_detail['village']=tool(html_object=html_object1,selector=".row:nth-child(11) .col-sm-3:nth-child(4)")
    adress_detail['pin_code']=tool(html_object=html_object1,selector=".row:nth-child(12) .col-sm-3+ .col-sm-3")
    
    # ORGANIZATION CONTACT DETAIL
    organization_contact={}
    organization_contact['office_number']=tool(html_object=html_object1,selector=".row:nth-child(14) .col-sm-3+ .col-sm-3")
    try:
        organization_contact['website_url']=tool(html_object=html_object1,selector=".clearfix~ .col-sm-3+ .col-sm-3")
    except:
        pass
    # PAST EXPERIENCE DETAIL
    past_exp_detail={}
    past_exp_detail['past_experience_detail']=[]
    
    # PROJECT
    project={}
    project['project_name']=tool(html_object=html_object1,selector="#DivProject .label-block:nth-child(2) > .row:nth-child(1) .col-sm-3:nth-child(2)")
    project['project_status']=tool(html_object=html_object1,selector='.label-block:nth-child(2) > .row:nth-child(1) .col-sm-3:nth-child(4)')
    project['date_of_completion']=tool(html_object=html_object1,selector='.label-block:nth-child(2) > .row:nth-child(2) .col-sm-3:nth-child(2)')
    project['litigation_related_to_project']=tool(html_object=html_object1,selector='.label-block .label-block .row:nth-child(1) .col-sm-3:nth-child(2)')
    project['project_type']=tool(html_object=html_object1,selector='.label-block .label-block .row:nth-child(1) .col-sm-3:nth-child(4)')
    project['are_there_any_promoter']=tool(html_object=html_object1,selector='.label-block .label-block .row:nth-child(2) .col-sm-3+ .col-sm-3')
    
    project['plot_bearing_number']=tool(html_object=html_object1,selector='#DivProject .row:nth-child(4) .col-sm-3:nth-child(2)')
    
    
    project['boundary_east']=tool(html_object=html_object1,selector='#DivProject .row:nth-child(4) .col-sm-3:nth-child(4)')
    
    project['boundasy_west']=tool(html_object=html_object1,selector='.label-block .label-block .row:nth-child(5) .col-sm-3:nth-child(2)')
    project['boundary_north']=tool(html_object=html_object1,selector='.label-block .label-block .row:nth-child(5) .col-sm-3:nth-child(4)')
    project['boundary_south']=tool(html_object=html_object1,selector='.label-block .label-block .row:nth-child(6) .col-sm-3:nth-child(2)')
    project['state']=tool(html_object=html_object1,selector='.row:nth-child(6) .col-sm-3:nth-child(4)')
    project['division']=tool(html_object=html_object1,selector='.label-block .label-block .row:nth-child(7) .col-sm-3:nth-child(2)')
    project['district']=tool(html_object=html_object1,selector='.label-block .label-block .row:nth-child(7) .col-sm-3:nth-child(4)')
    # .label-block .label-block .row:nth-child(7) .col-sm-3:nth-child(4)
    project['taluka']=tool(html_object=html_object1,selector='.label-block .label-block .row:nth-child(7) .col-sm-3:nth-child(4)')
    # .label-block .label-block .row:nth-child(8) .col-sm-3:nth-child(2)
    project['village']=tool(html_object=html_object1,selector='.row:nth-child(8) .col-sm-3:nth-child(4)')
    project['street']=tool(html_object=html_object1,selector='#DivProject .row:nth-child(9) .col-sm-3:nth-child(2)')
    project['locality']=tool(html_object=html_object1,selector='#DivProject .row:nth-child(9) .col-sm-3:nth-child(4)')
    project['pincode']=tool(html_object=html_object1,selector='.row:nth-child(12) .col-sm-3+ .col-sm-3')
    project['total_plot_area']=tool(html_object=html_object1,selector='.label-block+ .row .col-sm-3:nth-child(4)')
    project['total_number_of_praposed_bulding']=tool(html_object=html_object1,selector='.label-block~ .row:nth-child(6) .col-sm-3:nth-child(2)')
    project['sanction_by_MCGM']=[]
    project['sanctioned_building']=tool(html_object=html_object1,selector='.x_title+ .label-block .row:nth-child(7) .col-sm-3:nth-child(2)')
    project['praposed_but_not_sanctioned']=tool(html_object=html_object1,selector='#DivProject .x_title+ .label-block .row+ .row .col-sm-3:nth-child(4)')
    project['total_recreational_open_space']=tool(html_object=html_object1,selector='.x_title+ .label-block .row:nth-child(8) .col-sm-3+ .col-sm-3')
                                                    
    # FSI DETAIL
    fsi_detail={}
    fsi_detail['build_up_area_praposed_by_fsi']=tool(html_object=html_object1,selector='.label-block:nth-child(6) .row:nth-child(1) .col-sm-3:nth-child(2)')
    fsi_detail['permissible build up area']=tool(html_object=html_object1,selector=".row~ .x_title+ .label-block .col-sm-3:nth-child(4)")
    fsi_detail['sanctioned_build_up_area']=tool(html_object=html_object1,selector=".label-block:nth-child(6) .row+ .row .col-sm-3+ .col-sm-3")
    
    # BANK DETAIL
    bank_detail={}
    bank_detail['bank name']=tool(html_object=html_object1,selector=".label-block:nth-child(9) .row:nth-child(1) .col-sm-3+ .col-sm-3")
    bank_detail['IFSC code']=tool(html_object=html_object1,selector=".label-block:nth-child(9) .row+ .row .col-sm-3+ .col-sm-3")
    
    # PROJECT DETAIL
    project_detail={}
    project_detail['name']=tool1(html_object=html_object1,selector='#DivAmenities .table-striped:nth-child(1) td:nth-child(1)')
    project_detail['praposed']=tool1(html_object=html_object1,selector='#DivAmenities .table-striped:nth-child(1) td:nth-child(2)')
    project_detail['booked']=tool1(html_object=html_object1,selector='#DivAmenities .table-striped:nth-child(1) td:nth-child(3)')
    project_detail['work_done_percent']=tool1(html_object=html_object1,selector="#DivAmenities .table-striped:nth-child(1) td:nth-child(4)")
    
    # Development work
    development_work={}
    development_work['common_area_and_facilities']=tool1(html_object=html_object1,selector="#DivAmenities .x_title+ .table-striped td:nth-child(1)")
    development_work['available']=tool1(html_object=html_object1,selector="#DivAmenities .x_title+ .table-striped td:nth-child(2)")
    development_work['percent']=tool1(html_object=html_object1,selector="#DivAmenities .x_title+ .table-striped td:nth-child(3)")
    development_work['detail']=tool1(html_object=html_object1,selector="#DivAmenities .x_title+ .table-striped td:nth-child(4)")
    
    # Project professional information
    project_professional_info={}
    project_professional_info['professional_name']=tool1(html_object=html_object1,selector="#fldindtxt1 td:nth-child(1)")
    project_professional_info['maharera_certification_no']=tool1(html_object=html_object1,selector="#fldindtxt1 td:nth-child(2)")
    project_professional_info['professional_type']=tool1(html_object=html_object1,selector="#fldindtxt1 td~ td+ td")
    
    # Building detail
    box={}
    box['rera_id']=file[j][0:12]
    box['general_information']=general_information
    box['organization']=organization
    box['address_detail']=adress_detail
    box['organization_contact_detail']=organization_contact
    box['project']=project
    box['FSI_detail']=fsi_detail
    box['bank_detail']=bank_detail
    box['project_detail']=project_detail
    box['development_work']=development_work
    box['project_professional_information']=project_professional_info
    
    with open("test_rera.json","r") as f:
        emps=json.load(f)
        emps.append(box)
    with open("test_rera.json","w") as f1:
        emps=f1.write(json.dumps(emps))
        # print("SAVEDDDD")
    print('data_saved_up_to__'+str(j))   
                