import os
from __config import *
from __db_config import *
from itertools import combinations

def getAdminInfo(db): 
    get_admin_data = []
    cursor = db.cursor()
    query = "select u.name, a.area, a.city, ap.type from users u, admin_areas a, admin_profile ap where u.id = a.admin_id and name not like '%isana%' and a.admin_id != 2 and a.admin_id=ap.admin_id" 
    cursor.execute(query) 
    get_data = cursor.fetchone()
    while get_data is not None:
        get_admin_data_dict = [get_data[0], get_data[1], get_data[2], get_data[3]]
        get_admin_data.append(get_admin_data_dict)
        get_data = cursor.fetchone()
    return get_admin_data
 
def generateSiteMap(admin_info, wellness_url):   
    if os.path.isfile('/opt/atman/bin/pranacare_sitemap.txt'):
       os.remove('/opt/atman/bin/pranacare_sitemap.txt') 
    for admin_data in admin_info:
        with open('/opt/atman/bin/pranacare_sitemap.txt','a') as file_new:
            file_new.write(wellness_url%("", admin_data[2].replace(" ", "%20"), "ALL", admin_data[0].replace(" ","%20")))
            file_new.write(wellness_url%("", admin_data[2].replace(" ", "%20"), admin_data[3].replace(" ", "%20"), admin_data[0].replace(" ","%20")))
            file_new.write(wellness_url%(admin_data[1].replace(" ", "%20")+",", admin_data[2].replace(" ","%20"), "ALL", admin_data[0].replace(" ","%20")))
            file_new.write(wellness_url%("", admin_data[2].replace(" ", "%20"), admin_data[3].replace(" ", "%20"),admin_data[0].replace(" ","%20")))
            file_new.write(wellness_url%(admin_data[1].replace(" ", "%20")+",", admin_data[2].replace(" ", "%20"), "ALL",""))  
            file_new.write(wellness_url%(admin_data[1].replace(" ", "%20")+",", admin_data[2].replace(" ", "%20"), admin_data[3].replace(" ", "%20"), admin_data[0].replace(" ","%20")))  
            file_new.write(wellness_url%(admin_data[1].replace(" ", "%20")+",", admin_data[2].replace(" ", "%20"), admin_data[3].replace(" ", "%20"), ""))  
            file_new.write(wellness_url%(admin_data[1].replace(" ", "%20")+",", admin_data[2].replace(" ", "%20"), "ALL", admin_data[0].replace(" ","%20")))  
    return 0
           
    
if __name__ == "__main__":
    init_db()
    db = get_db()
    wellness_url = "https://wellness.pranacare.co.in/%s%s/%s?q=%s\n"
    admin_info = getAdminInfo(db)
    generateSiteMap(admin_info, wellness_url)

