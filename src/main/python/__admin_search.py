from __db_config import *
from datetime import datetime
from __config import *
import calendar
import json


def getAdminData(db, country, city, area, speciality_type, name, admin_id, member_id, patient_id):
    try:
        admin_data_list = []
        admin_time_data_list = []
        admin_data_json = {}
        cursor = db.cursor()
        if country != "ALL":
            country = "and aa.country='%s'"%(country) 
        else:
            country = "" 
        if city != "ALL":
            city = "and aa.city='%s'"%(city)
        else:
            city = ""
        if area != "ALL":
            area = "and aa.area='%s'"%(area)
        else:
            area =""
        if speciality_type != "ALL":
            speciality_type_new = "and ap.type='%s'"%(speciality_type)
        else:
            speciality_type_new = ""
        if name != "ALL":
            name = "and u.name like"+ "'%"+name+"%'"
        else:
            name = ""
        if admin_id == "0" and member_id == "0":
            query = "SELECT DISTINCT u.name, ap.admin_id, ap.experience, ap.specialties, ap.profile_picture_filename, ap.small_logo_filename, ap.large_logo_filename, ap.type, ap.subtype, ap.title, ap.qualification, ap.website, ap.fblink, ap.youtube_link, ap.insta_link, ap.per_visit_fee, ap.linkedin_link, ap.overall_rating, u.gender, u.contact, u.email, ap.address, ap.profile_data from admin_profile ap, users u, admin_areas aa WHERE u.id = ap.admin_id and u.id = aa.admin_id and ap.admin_id = aa.admin_id %s %s %s %s %s"%(country, city, area, speciality_type_new, name)
            cursor.execute(query)
            get_data = cursor.fetchone()
        else:
            if admin_id != "0" and member_id == "0":
                query = "SELECT u.name, ap.admin_id, ap.experience, ap.specialties, ap.profile_picture_filename, ap.small_logo_filename, ap.large_logo_filename, ap.type, ap.subtype, ap.title, ap.qualification, ap.website, ap.fblink, ap.youtube_link, ap.insta_link, ap.per_visit_fee, ap.linkedin_link, ap.overall_rating, u.gender, u.contact, u.email, ap.address, ap.profile_data from admin_profile ap, users u WHERE u.id = ap.admin_id and ap.admin_id = %d"%(int(admin_id))
                cursor.execute(query)
                get_data = cursor.fetchone()
            elif (member_id != "0" and admin_id == "0") or (member_id != "0" and admin_id != "0"):
                if speciality_type == "admin_blocked":
                    query = "select u.name, ap.admin_id, case when bt.member_id is null then 'true' when bt.member_id is not null then 'false' end as status, ap.type from admin_profile ap left join (select member_id from collab_wellness_expert_acceptance where admin_id = %d) bt on ap.admin_id = bt.member_id join users u on u.id=ap.admin_id and ap.admin_id not in (select admin_id from collab_wellness_expert_acceptance where member_id != %d) and ap.admin_id != %d"%(int(member_id), int(member_id), int(member_id))
                    cursor.execute(query)
                    get_data = cursor.fetchone()
                    while get_data is not None:
                        admin_data_json["name"] = get_data[0]
                        admin_data_json["member_id"] = get_data[1]
                        admin_data_json["status"] = get_data[2]
                        admin_data_json["type"] = get_data[3]
                        admin_data_list.append(admin_data_json)
                        admin_data_json = {}
                        get_data = cursor.fetchone()
                    return json.dumps({"admin_data" : admin_data_list})
                if speciality_type == "patient_admin_blocked":
                    #query = "select crp.admin_id, crp.member_id, coalesce(cpaw.referral_consent,'1') as referral_consent, u1.name as admin_name, u2.name as patient_name, u3.name as member_name, crp.patient_id, ap.type from collab_refer_patient crp left outer join collab_patient_wellness_blocked cpaw on crp.admin_id = cpaw.admin_id and crp.patient_id = cpaw.patient_id and crp.member_id = cpaw.member_id inner join users u1 on u1.id = crp.admin_id inner join users u2 on u2.id = crp.patient_id inner join users u3 on u3.id = crp.member_id inner join admin_profile ap on ap.admin_id=crp.member_id where crp.patient_id=%d"%(int(member_id))
                    query = "SELECT u.name, ap.admin_id as member_id, case when bt.member_id is null then 'false' when bt.member_id is not null then 'true' end as status, ap.type ,(select admin_id from collab_refer_patient where patient_id = %d and member_id=ap.admin_id order by timestamp desc limit 1) as admin_id from admin_profile ap left join (select member_id from collab_patient_wellness_blocked where patient_id = %d) bt on ap.admin_id = bt.member_id join users u on u.id=ap.admin_id"%(int(member_id), int(member_id))
                    cursor.execute(query)
                    get_data = cursor.fetchone()
                    while get_data is not None:
                        admin_data_json["admin_id"] = get_data[4]
                        admin_data_json["member_id"] = get_data[1]
                        if get_data[2] == "true":
                             get_data_list = list(get_data)
                             get_data_list[2] = True
                             get_data = tuple(get_data_list)
                        else:
                             get_data_list = list(get_data)
                             get_data_list[2] = False
                             get_data = tuple(get_data_list)
                        admin_data_json["member_name"] = get_data[0]
                        admin_data_json["member_type"] = get_data[3]
                        admin_data_json["status"] =get_data[2]
                        admin_data_list.append(admin_data_json)
                        admin_data_json = {}
                        get_data = cursor.fetchone()
                    return json.dumps({"admin_data":admin_data_list})
                if patient_id == "0":
                    query = "select u.name, ap.admin_id, ap.type, u.contact, u.email from admin_profile ap, users u where type='%s' and u.id = ap.admin_id and ap.admin_id != %d"%(str(speciality_type), int(member_id))
                    cursor.execute(query)
                    get_data = cursor.fetchone()
                    while get_data is not None:
                        admin_data_json["name"] = get_data[0]
                        admin_data_json["admin_id"] = get_data[1]
                        admin_data_json["type"] = get_data[2]
                        admin_data_json["contact"] = get_data[3]
                        admin_data_json["email"] = get_data[4]
                        admin_data_list.append(admin_data_json)
                        admin_data_json = {}
                        get_data = cursor.fetchone()
                    return json.dumps({"admin_data" : admin_data_list})

                else:
                    #query = "select u.name, ap.admin_id, ap.type from admin_profile ap, users u where type='%s' and u.id = ap.admin_id and ap.admin_id != %d and ap.admin_id not in (select member_id from collab_wellness_expert_acceptance where admin_id=%d) and ap.admin_id not in (select admin_id from collab_wellness_expert_acceptance where member_id = %d) and ap.admin_id not in (select member_id from collab_patient_wellness_blocked where patient_id = %d)"%(str(speciality_type), int(member_id), int(member_id), int(member_id), int(patient_id))
                    query = "select u.name, ap.admin_id, ap.type from admin_profile ap, users u where type='%s' and u.id = ap.admin_id and ap.admin_id != %d and (ap.admin_id in (select member_id from collab_wellness_expert_acceptance where admin_id=%d) or ap.admin_id in (select admin_id from collab_wellness_expert_acceptance where member_id=%d)) and ap.admin_id not in (select member_id from collab_patient_wellness_blocked where patient_id = %d)"%(str(speciality_type), int(member_id), int(member_id), int(member_id) ,int(patient_id))
                cursor.execute(query)
                get_data = cursor.fetchone()
                while get_data is not None:
                    admin_data_json["name"] = get_data[0]
                    admin_data_json["admin_id"] = get_data[1]
                    admin_data_json["type"] = get_data[2]
                    admin_data_list.append(admin_data_json)
                    admin_data_json = {}
                    get_data = cursor.fetchone()
                return json.dumps({"admin_data" : admin_data_list})
        while get_data is not None:
            admin_data_json["name"] = get_data[0]
            admin_data_json["admin_id"] = str(get_data[1])
            admin_data_json["experience"] = get_data[2]
            admin_data_json["specialties"] = get_data[3]
            admin_data_json["profile_picture_filename"] = str(get_data[4])
            admin_data_json["small_logo_filename"] = get_data[5]
            admin_data_json["large_logo_filename"] = get_data[6]
            admin_data_json["type"] = get_data[7]
            admin_data_json["subtype"] = get_data[8]
            admin_data_json["title"] = get_data[9]
            admin_data_json["qualification"] = get_data[10]
            admin_data_json["website"] = get_data[11]
            admin_data_json["fblink"] = get_data[12]
            admin_data_json["youtube_link"] = get_data[13]
            admin_data_json["insta_link"] = get_data[14]
            admin_data_json["per_visit_fee"] = get_data[15]
            admin_data_json["linkedin_link"] = get_data[16]
            admin_data_json["overall_rating"] = get_data[17]
            admin_data_json["gender"] = get_data[18]
            admin_data_json["contact"] = get_data[19]
            admin_data_json["email"] = get_data[20]
            admin_data_json["address"] = get_data[21]
            admin_data_json["profile_data"] = get_data[22]
            admin_id = admin_data_json.get("admin_id")
            admin_time_data_list = []
            if admin_id != "0":
                start_day, end_day = calendar.monthrange(int(datetime.now().strftime("%Y")), int(datetime.now().strftime("%m"))) 
                cursor_2 = db.cursor()
                query_1 = "SELECT DISTINCT atg.start_time, atg.end_time, atg.area, atg.city, aa.address, atg.admin_available_days from admin_time_granularity atg, admin_areas aa WHERE atg.admin_id=%d and aa.admin_id=%d and aa.area IS NOT NULL and atg.area IS NOT NULL and aa.area=atg.area and ('%d' BETWEEN atg.start_date and atg.end_date or '%d' BETWEEN atg.start_date and atg.end_date)"%(int(admin_id), int(admin_id), int((datetime.now().strftime("%Y%m")+str(start_day))), int((datetime.now().strftime("%Y%m")+str(end_day))))
                cursor_2.execute(query_1)
                get_time_data = cursor_2.fetchone()
                while get_time_data is not None:
                    if get_time_data[2] != None and get_time_data[3] != None:
                        admin_time = {"start_time" : get_time_data[0], "end_time": get_time_data[1], "area": get_time_data[2], "city": get_time_data[3], "address": get_time_data[4], "admin_available_days" : get_time_data[5]}
                        admin_time_data_list.append(admin_time)
                    get_time_data = cursor_2.fetchone()
            admin_data_json["admin_time_slot"] = admin_time_data_list 
            admin_data_list.append(admin_data_json)
            admin_data_json = {}
            get_data = cursor.fetchone()
        return json.dumps({"admin_data" : admin_data_list})
    except Exception as err:
        print ("error in getting admin search")
        print (err)

if __name__ == "__main__":
    init_db()
    db = get_db()
    if len(sys.argv) == 9:
        country = sys.argv[1]
        if country.lower() == "all":
            country = country.upper()
        city = sys.argv[2]
        if city.lower() == "all":
            city = city.upper()
        area = sys.argv[3]
        if area.lower() == "all":
            area = area.upper()
        speciality_type = sys.argv[4]
        name = sys.argv[5]
        admin_id = sys.argv[6]
        member_id = sys.argv[7]
        patient_id = sys.argv[8]
        print(getAdminData(db, country, city, area, speciality_type, name, admin_id, member_id, patient_id))
    else:
        print ("error in getting admin search")
