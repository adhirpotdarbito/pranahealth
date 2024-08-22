import requests
import logging


def insertPatient(patient_id, wellness_id, template_file, __composer_config, header):
    data, url = __composer_config.getPatientInfoTemplate(template_file)
    __data = data%(patient_id, wellness_id)
    PostData(__data, url, header)

def insertWellnessExpert(wellness_id, wellness_type, wellness_info, template_file, __composer_config, header):
    data, url = __composer_config.getWellnessExpertTemplate(template_file)
    __data = data%(wellness_id, wellness_type, wellness_info)
    PostData(__data, url, header)

def insertDataAccessor(wellness_id, wellness_type, template_file, __composer_config, header):
    data, url = __composer_config.getDataAccessorTemplate(template_file)
    __data = data%(wellness_id, wellness_type)
    PostData(__data, url, header)

def insertPatientAnthropometryData(patient_id, wellness_id, date, anthropometry, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddAnthropometryDataTemplate(template_file)
    __data = data%(patient_id, wellness_id, date, anthropometry, accessor)
    PostData(__data, url, header)

def updatePatientAnthropometryData(patient_id, date, anthropometry, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateAnthropometryDataTemplate(template_file)
    __data = data%(patient_id, date, anthropometry)
    PostData(__data, url, header)

def insertPatientBiochemicalData(patient_id, wellness_id, date, biochemical, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddBiochemicalDataTemplate(template_file)
    __data = data%(patient_id, wellness_id, date, biochemical, accessor)
    PostData(__data, url, header)

def updatePatientBiochemicalData(patient_id, date, biochemical, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateBiochemicalDataTemplate(template_file)
    __data = data%(patient_id, date, biochemical)
    PostData(__data, url, header)

def insertPatientClinicalData(patient_id, wellness_id, date, clinical, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddClinicalDataTemplate(template_file)
    __data = data%(patient_id, wellness_id, date, clinical, accessor)
    PostData(__data, url, header)

def updatePatientClinicalData(patient_id, wellness_id, date, clinical, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateClinicalDataTemplate(template_file)
    __data = data%(patient_id, date, clinical)
    PostData(__data, url, header)

def insertPatientDietaryAssessmentData(patient_id, wellness_id, date, dietary_assessment, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddDietaryAssessmentTemplate(template_file)
    __data = data%(patient_id, wellness_id, date, dietary_assessment, accessor)
    PostData(__data, url, header)

def updatePatientDietaryAssessment(patient_id, date, dietary_assessment, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateDietaryAssessmentTemplate(template_file)
    __data = data%(patient_id, date, dietary_assessment)
    PostData(__data, url, header)

def insertPatientFoodFrequency(patient_id, wellness_id, date, food_frequency, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddFoodFrequencyTemplate(template_file)
    __data = data%(patient_id, wellness_id, date, food_frequency, accessor)
    PostData(__data, url, header)
    
def updatePatientFoodFrequency(patient_id, date, food_frequency, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateFoodFrequencyTemplate(template_file)
    __data = data%(patient_id, date, food_frequency)
    PostData(__data, url, header)

def insertPatientFoodRecall(patient_id, wellness_id, date, food_recall, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddFoodRecallTemplate(template_file)
    __data = data%(patient_id, wellness_id, date, food_recall, accessor)
    PostData(__data, url, header)

def updatePatientFoodRecall(patient_id, date, food_recall, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateFoodRecallTemplate(template_file)
    __data = data%(patient_id, date, food_recall)
    PostData(__data, url, header)

def insertPatientFoodPrescription(patient_id, wellness_id, date, food_prescription, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddFoodPrescriptionTemplate(template_file)
    __data = data%(patient_id, wellness_id, date, food_prescription, accessor)
    PostData(__data, url, header)

def updatePatientFoodPrescription(patient_id, date, food_prescription, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateFoodPrescriptionTemplate(template_file)
    __data = data%(patient_id, date, food_prescription)
    PostData(__data, url, header)

def insertPatientPathologyPrescription(patient_id, wellness_id, date, path_prescription, accessor, template_file, __composer_config, header):
     data, url = __composer_config.getAddPathologyPrescritionTemplate(template_file)
     __data = data%(patient_id, wellness_id, date, path_prescription, accessor)
     PostData(__data, url, header)

def updatePatientPathologyPrescription(patient_id, date, path_prescription, template_file, __composer_config, header):
    data, url = __composer_config.getUpdatePathologyPrescriptionTemplate(template_file)
    __data = data%(patient_id, date, path_prescription)
    PostData(__data, url, header)

def insertPatientPersonalHistory(patient_id, wellness_id, date, personal_history, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddPersonalHistoryTemplate(template_file)
    __data = data%(patient_id, wellness_id, date, personal_history, accessor)
    PostData(__data, url, header) 

def updatePatientPersonalHistory(patient_id, date, personal_history, template_file, __composer_config, header):
    data, url = __composer_config.getUpdatePersonalHistoryTemplate(template_file)
    __data = data%(patient_id, date, personal_history)
    PostData(__data, url, header)

def insertPatientLifestyleHabits(patient_id, wellness_id, date, lifestyle_habit, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddLifestyleHabitsTemplate(template_file)
    __data = data%(patient_id, wellness_id, date, lifestyle_habit, accessor)
    PostData(__data, url, header)

def updatePatientLifestyleHabits(patient_id, date, lifestyle_habit, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateLifestyleHabitsTemplate(template_file)
    __data = data%(patient_id, date, lifestyle_habit)
    PostData(__data, url, header)

def insertPatientFamilyHistory(patient_id, wellness_id, date, family_history, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddFamilyHistoryTemplate(template_file)
    __data = data%(patient_id, wellness_id, date, family_history, accessor)
    PostData(__data, url, header) 

def updatePatientFamilyHistory(patient_id, date, family_history, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateFamilyHistoryTemplate(template_file)
    __data = data%(patient_id, date, family_history)
    PostData(__data, url, header)

def insertPatientMedicalHistory(patient_id, wellness_id, date, medical_history, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddMedicalHistoryTemplate(template_file)
    __data = data%(patient_id, wellness_id, date, medical_history, accessor)
    PostData(__data, url, header) 

def updatePatientMedicalHistory(patient_id, date, medical_history, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateMedicalHistoryTemplate(template_file)
    __data = data%(patient_id, date, medical_history)
    PostData(__data, url, header)

def insertPatientAppointments(patient_id, date, status, appointments, wellness_id, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddPatientAppointmentsTemplate(template_file)
    __data = data%(patient_id, date, status, appointments, wellness_id, accessor) 
    PostData(__data, url, header)
  
def updatePatientAppointments(patient_id, date, status, appointments, wellness_id, template_file, __composer_config, header):
    data, url = __composer_config.getUpdatePatientAppointmentTemplate(template_file)
    __data = data%(patient_id, date, status, appointments, wellness_id)
    PostData(__data, url, header)

def insertWellnessAppointmentSlot(wellness_id, date, status, appointment_slot, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddWellnessAppointmentSlotTemplate(template_file)
    __data = data%(wellness_id, date, status, appointment_slot, accessor)
    PostData(__data, url, header)

def updateWellnessAppointmentSlot(wellness_id, date, status, appointment_slot, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateWellnessAppointmentSlotTemplate(template_file)
    __data = data%(wellness_id, date, status, appointment_slot)
    PostData(__data, url, header)

def insertPatientFoodPrescriptionBasic(patient_id, wellness_id, date, food_prescription_basic, accessor, template_file, __composer_config, header):
    data, url = __composer_config.getAddPatientFoodPrescriptionBasicTemplate(template_file)
    __data = data%(patient_id, wellness_id, date, food_prescription_basic, accessor)
    PostData(__data, url, header)

def updatePatientFoodPrescriptionBasic(patient_id, date, food_prescription_basic, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateFoodPrescriptionBasicTemplate(template_file)
    __data = data%(patient_id, date, food_prescription_basic)
    PostData(__data, url, header)

def insertWellnessInvitaion(wellness_id, admin_details, date, member_type, member_contact, member_email, member_gender, member_city, member_country, member_name, message, password, terms_condition, status, terms, template_file, __composer_config, header):
    data, url = __composer_config.getAddWellnessInvitationTemplate(template_file)
    __data = data%(wellness_id, admin_details, date, member_type, member_contact, member_email, member_gender, member_city, member_country, member_name,message, password, terms_condition, status, terms, wellness_id)
    PostData(__data, url, header)    

def updateWellnessInvitation(wellness_id, date, member_type, member_contact, member_email, member_gender, member_city, member_country, member_name, message, password, terms_condition, status, terms, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateWellnessInvitaionTemlate(template_file)
    __data = data%(wellness_id, date, member_type, member_contact, member_email, member_gender, member_city, member_country, member_name, message, password, terms_condition, status, terms)
    PostData(__data, url, header)

def insertWellnessPanelCollab(wellness_id, panel_id, panel_name, panel_description, date, admin_id, member_id, member_consent, wellness_type, wellness_contact, wellness_email, wellness_gender, wellness_city, wellness_country, member_type, member_contact, member_email, member_gender, member_city, member_country, template_file, __composer_config, header):
    data, url = __composer_config.getAddWellnessPanelCollabTemplate(template_file)
    __data = data%(wellness_id, panel_id, panel_name, panel_description, date, admin_id, member_id, member_consent, date, wellness_type, wellness_contact, wellness_email, wellness_gender, wellness_city, wellness_country, date, member_type, member_contact, member_email, member_gender, member_city, member_country)
    PostData(__data, url, header)

def updateWellnessPanelCollab(wellness_id, date, admin_id, member_id, member_consent, wellness_type, wellness_contact, wellness_email, wellness_gender, wellness_city, wellness_country, member_type, member_contact, member_email, member_gender, member_city, member_country, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateWellnessPanelCollabTemplate(template_file)
    __data = data%(wellness_id, date, admin_id, member_id, member_consent, date, wellness_type, wellness_contact, wellness_email, wellness_gender, wellness_city, wellness_country,date, member_type, member_contact, member_email, member_gender, member_city, member_country)
    PostData(__data, url, header)

def insertPateintReferral(patient_id, panel_id, panel_name, panel_description, date, admin_id, member_id, datashare_consent, referral_consent, referral_notes, patient_type, patient_contact, patient_email, patient_gender, patient_city, patient_country, patient_age, wellness_type, wellness_contact, wellness_email, wellness_gender, wellness_city, wellness_country, member_type, member_contact, member_email, member_gender, member_city, member_country, template_file, __composer_config, header):
    data, url = __composer_config.getAddPatientReferralTemplate(template_file)
    __data = data%(patient_id, panel_id, panel_name, panel_description, date, admin_id, member_id, datashare_consent, referral_consent, referral_notes,  date, patient_type, patient_contact, patient_email, patient_gender, patient_city, patient_country, patient_age, date, wellness_type, wellness_contact, wellness_email, wellness_gender, wellness_city, wellness_country, date, member_type, member_contact, member_email, member_gender, member_city, member_country)
    PostData(__data, url, header)

def updatePatientReferral(patient_id, date, admin_id, member_id, datashare_consent,referral_consent, referral_notes, patient_type, patient_contact, patient_email, patient_gender, patient_city, patient_country, patient_age, wellness_type, wellness_contact, wellness_email, wellness_gender, wellness_city, wellness_country, member_type, member_contact, member_email, member_gender, member_city, member_country, template_file, __composer_config, header):
    data, url = __composer_config.getUpdatePatientReferralTemplate(template_file)
    __data = data%(patient_id, date, admin_id, member_id, datashare_consent, referral_consent, referral_notes, date, patient_type, patient_contact, patient_email, patient_gender, patient_city, patient_country, patient_age, date, wellness_type, wellness_contact, wellness_email, wellness_gender, wellness_city, wellness_country, date, member_type, member_contact, member_email, member_gender, member_city, member_country)
    PostData(__data, url, header)

def insertWellnessCollabChange(wellness_id, date, member_id, template_file, __composer_config, header):
    data, url = __composer_config.getAddWellnessCollabChangeTemplate(template_file)
    __data = data%(wellness_id, date, wellness_id, member_id)
    PostData(__data, url, header)


def updateWellnessCollabChange(wellness_id, date, member_id, template_file, __composer_config, header):
    data, url = __composer_config.getUpdateWellnessCollabChangeTemplate(template_file)
    __data = data%(wellness_id, date, wellness_id, member_id)
    PostData(__data, url, header)

def insertPatientReferralChange(patient_id, date, wellness_id, member_id, collaboration, template_file, __composer_config, header):
    data, url = __composer_config.getAddPatientReferralChangeTemplate(template_file)
    __data = data%(patient_id, date, wellness_id, patient_id, member_id, collaboration)
    PostData(__data, url, header)

def updatePatientReferralChange(patient_id, date, wellness_id, member_id, collaboration, template_file, __composer_config, header):
    data, url = __composer_config.getUpdatePatientReferralChangeTemplate(template_file)
    __data = data%(patient_id, date, wellness_id, patient_id, member_id, collaboration)
    PostData(__data, url, header)

def getWellnessCollab(wellness_id, template_file, __composer_config):
    url = __composer_config.getWellnessPanelCollabByIdTemplate(template_file)
    return GetData(url%wellness_id)

def getPatientCollab(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientReferralByIdTemplate(template_file)
    return GetData(url%patient_id)

def getWellnessCollabChange(wellness_id, template_file, __composer_config):
    url = __composer_config.getWellnessCollabChangeByIdTemplate(template_file)
    return GetData(url%wellness_id)

def getPatientReferralChange(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientReferralChangeByIdTemplate(template_file)
    return GetData(url%patient_id)

def getPatientById(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientByIdTemplate(template_file)
    return GetData(url%patient_id)

def getWellnessExpertById(wellness_id, template_file, __composer_config):
    url = __composer_config.getWellnessExpertByIdTemplate(template_file)
    return GetData(url%wellness_id)

def getDataAccessorById(wellness_id, template_file, __composer_config):
    url = __composer_config.getDataAccessorByIdTemplate(template_file)
    return GetData(url%wellness_id)

def getPatientAnthropometryData(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientAnthropometryByIdTemplate(template_file)
    return GetData(url%patient_id)

def getPatientBiochemicalData(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientBiochemicalByIdTemplate(template_file)
    return GetData(url%patient_id)

def getPatientClinicalData(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientClinicalByIdTemplate(template_file)
    return GetData(url%patient_id)

def getPatientDietaryAssessment(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientDietaryAssessmentByIdTemplate(template_file)
    return GetData(url%patient_id)

def getPatientFoodFrequency(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientFoodFrequencyByIdTempalte(template_file)
    return GetData(url%patient_id)

def getPatientFoodRecall(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientFoodRecallByIdTempalte(template_file)
    return GetData(url%patient_id)

def getPatientFoodPrescription(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientFoodPrescriptionByIdTemplate(template_file)
    return GetData(url%patient_id)

def getPatientPathologyPrescription(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientPathologyPresecriptionByIdTemplate(template_file)
    return GetData(url%patient_id)

def getPatientPersonalHistory(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientPersonalHistoryByIdTemplate(template_file)
    return GetData(url%patient_id)

def getPatientLifestyleHabit(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientLifestyleHabitsByIdTemplate(template_file)
    return GetData(url%patient_id)

def getPatientMiscData(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientMiscDataByIdTemplate(template_file)
    return GetData(url%patient_id)

def getPatientFamilyHistory(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientFamilyHistoryByIdTemplate(template_file)
    return GetData(url%patient_id)

def getPatientMedicalHistory(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientMedicalHistoryByIdTemplate(template_file)
    return GetData(url%patient_id)

def getPatientAppointments(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientAppointmentByIdTemplate(template_file)
    return GetData(url%patient_id)

def getWellnessAppointmentSlot(wellness_id, template_file, __composer_config):
    url = __composer_config.getWellnessAppointmentSlotByIdTemplate(template_file)
    return GetData(url%wellness_id)

def getWellnessInvitationById(wellness_id, template_file, __composer_config):
    url = __composer_config.getWellnessInvitationByIdTemplate(template_file)
    return GetData(url%wellness_id) 

def getPatientFoodPrescriptionBasic(patient_id, template_file, __composer_config):
    url = __composer_config.getPatientFoodPrescriptionBasicByIdTemplate(template_file)
    return GetData(url%patient_id)

def getAllPatients(template_file, __composer_config):
    url = __composer_config.getAllPatientsTemplate(template_file)
    return GetDataQuery(url)

def getAllWellnessExpert(template_file, __composer_config):
    url = __composer_config.getAllWellnessExpertTemplate(template_file)
    return GetDataQuery(url)

def getAllPatientAnthropometryByDate(template_file, __composer_config, start_date, end_date):
    url = __composer_config.getAllPatientAnthropometryByDateTemplate(template_file)
    return GetDataQuery(url%(start_date, end_date))

def getAllPatientBiochemicalByDate(template_file, __composer_config, start_date, end_date):
    url = __composer_config.getAllPatientBiochemicalByDateTemplate(template_file)
    return GetDataQuery(url%(start_date, end_date))

def getAllPatientClinicalByDate(template_file, __composer_config, start_date, end_date):
    url = __composer_config.getAllPatientClinicalByDateTemplate(template_file)
    return GetDataQuery(url%(start_date, end_date))

def getAllPatientFamilyHistoryByDate(template_file, __composer_config, start_date, end_date):
    url = __composer_config.getAllPatientFamilyHistoryByDateTemplate(template_file)
    return GetDataQuery(url%(start_date, end_date)) 

def getAllPatientLifestyleHabitsByDate(template_file, __composer_config, start_date, end_date):
    url = __composer_config.getAllPatientLifestyleHabitsByDateTemplate(template_file)
    return GetDataQuery(url%(start_date, end_date)) 

def getAllPatientMedicalHistoryByDate(template_file, __composer_config, start_date, end_date):
    url = __composer_config.getAllPatientMedicalHistoryByDateTemplate(template_file)
    return GetDataQuery(url%(start_date, end_date)) 

def getAllPatientDietaryAssessmentByDate(template_file, __composer_config, start_date, end_date):
    url = __composer_config.getAllPatientDietaryAssessmentByDateTemplate(template_file)
    return GetDataQuery(url%(start_date, end_date))

def getAllPatientPersonalHistoryByDate(template_file, __composer_config, start_date, end_date):
    url = __composer_config.getAllPatientPersonalHistoryByDateTemplate(template_file)
    return GetDataQuery(url%(start_date, end_date))

def getAllPatientFoodPrescriptionByDate(template_file, __composer_config, start_date, end_date):
    url = __composer_config.getAllPatientFoodPrescriptionByDateTemplate(template_file)
    return GetDataQuery(url%(start_date, end_date))

def getAllPatientPathologyPrescriptionByDate(template_file, __composer_config, start_date, end_date):
    url = __composer_config.getAllPatientPathologyPrescriptionByDateTemplate(template_file)
    return GetDataQuery(url%(start_date, end_date))    

def getAllPatientFoodFrequencyByDate(template_file, __composer_config, start_date,  end_date):
    url = __composer_config.getAllPatientFoodFrequencyByDateTemplate(template_file)
    return GetDataQuery(url%(start_date, end_date))

def getAllPatientFoodRecallByDate(template_file, __composer_config, start_date, end_date):
    url = __composer_config.getAllPatientFoodRecallByDateTemplate(template_file)
    return GetDataQuery(url%(start_date, end_date))
 
def getAllWellnessInvitationByDate(template_file, __composer_config, start_date, end_date):
    url = __composer_config.getAllWellnessInvitationByDateTemplate(template_file)
    return GetDataQuery(url%(start_date, end_date))

def GetData(url):
    response = requests.get(url)
    return response.status_code

def GetDataQuery(url):
    response = requests.get(url)
    #response.status_code
    return response.content

def PostData(data, url, header):
    print data
    response = requests.post(url, headers=header, data=data)
    if response.status_code == 200:
        print ("Post Successful")
        logging.info("Post Successful")
    elif response.status_code in [400, 500, 404]:
        print ("Post Unsuccessful")
        logging.info("Post Unsuccessful")
