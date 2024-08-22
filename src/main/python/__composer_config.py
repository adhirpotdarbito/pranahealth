import json

class ComposerConfig():
    def __init__(self):
        pass 

    def getJsonTemplate(self):
        with open("/opt/atman/bc/hyperledger_composer_config.json", "rb") as json_file:
            json_template = json.load(json_file) 
        return json_template

    def getHeader(self, template_file):
        header = template_file.get("header", "")
        return header

    def getPatientInfoTemplate(self, template_file):
        url = template_file.get("add_patient_url", "")
        data = template_file.get("add_patient_info", "")
        return data, url

    def getWellnessExpertTemplate(self, template_file):
        url = template_file.get("add_wellness_expert_url", "")
        data = template_file.get("add_wellness_expert_info", "")
        return data, url

    def getDataAccessorTemplate(self, template_file):
        url = template_file.get("add_data_accessor_url", "")
        data = template_file.get("add_data_accessor", "")
        return data, url

    def getAddAnthropometryDataTemplate(self, template_file):
        url = template_file.get("add_patient_anthropometry_data_url", "")
        data = template_file.get("add_patient_anthropometry_data", "")
        return data, url

    def getUpdateAnthropometryDataTemplate(self, template_file):
        url = template_file.get("update_patient_anthropometry_data_url", "")
        data = template_file.get("update_patient_anthropometry_data", "")
        return data, url

    def getAddBiochemicalDataTemplate(self, template_file):
        url = template_file.get("add_patient_biochemical_data_url", "")
        data = template_file.get("add_patient_biochemical_data", "")
        return data, url

    def getUpdateBiochemicalDataTemplate(self, template_file):
        url = template_file.get("update_patient_biochemical_data_url", "")
        data = template_file.get("update_patient_biochemical_data", "")
        return data, url

    def getAddClinicalDataTemplate(self, template_file):
        url = template_file.get("add_patient_clinical_data_url", "")
        data = template_file.get("add_patient_clinical_data", "")
        return data, url

    def getUpdateClinicalDataTemplate(self, template_file):
        url = template_file.get("update_patient_clinical_data_url", "")
        data = template_file.get("update_patient_clinical_data", "")
        return data, url

    def getAddDietaryAssessmentTemplate(self, template_file):
        url = template_file.get("add_patient_dietary_data_url", "")
        data = template_file.get("add_patient_dietary_data", "")
        return data, url

    def getUpdateDietaryAssessmentTemplate(self, template_file):
        url = template_file.get("update_patient_dietary_data_url", "")
        data = template_file.get("update_patient_dietary_data", "")
        return data, url

    def getAddFoodFrequencyTemplate(self, template_file):
        url = template_file.get("add_patient_food_frequency_data_url", "")
        data = template_file.get("add_patient_food_frequency_data", "")
        return data, url
    
    def getUpdateFoodFrequencyTemplate(self, template_file):
        url = template_file.get("update_patient_food_frequency_data_url", "")
        data = template_file.get("update_patient_food_frequency_data", "")
        return data, url

    def getAddFoodRecallTemplate(self, template_file):
        url = template_file.get("add_patient_food_recall_data_url", "")
        data = template_file.get("add_patient_food_recall_data", "")
        return data, url

    def getUpdateFoodRecallTemplate(self, template_file):
        url = template_file.get("update_patient_food_recall_data_url", "")
        data = template_file.get("update_patient_food_recall_data", "")
        return data, url

    def getAddFoodPrescriptionTemplate(self, template_file):
        url = template_file.get("add_patient_food_prescription_url", "")
        data = template_file.get("add_patient_food_prescription", "")
        return data, url

    def getUpdateFoodPrescriptionTemplate(self, template_file):
        url = template_file.get("update_patient_food_prescription_url", "")
        data = template_file.get("update_patient_food_prescription","")
        return data, url
    
    def getAddPathologyPrescritionTemplate(self, template_file):
        url = template_file.get("add_patient_pathology_prescription_url", "")
        data = template_file.get("add_patient_pathology_prescription", "")
        return data, url

    def getUpdatePathologyPrescriptionTemplate(self, template_file):
        url = template_file.get("update_patient_pathology_prescription_url", "")
        data = template_file.get("update_patient_pathology_prescription", "")
        return data, url

    def getAddPersonalHistoryTemplate(self, template_file):
        url = template_file.get("add_patient_personal_history_data_url", "")
        data = template_file.get("add_patient_personal_history_data", "")
        return data, url

    def getUpdatePersonalHistoryTemplate(self, template_file):
        url = template_file.get("update_patient_personal_history_data_url", "")
        data = template_file.get("update_patient_personal_history_data", "")
        return data, url
    
    def getAddLifestyleHabitsTemplate(self, template_file):
        url = template_file.get("add_patient_lifestyle_data_url","")
        data = template_file.get("add_patient_lifestyle_data", "")
        return data, url

    def getUpdateLifestyleHabitsTemplate(self, template_file):
        url = template_file.get("update_patient_lifestyle_data_url", "")
        data = template_file.get("update_patient_lifestyle_data", "")
        return data, url

    def getAddFamilyHistoryTemplate(self, template_file):
        url = template_file.get("add_patient_family_history_data_url", "")
        data = template_file.get("add_patient_family_history_data", "")
        return data, url

    def getUpdateFamilyHistoryTemplate(self, template_file):
        url = template_file.get("update_patient_family_history_data_url", "")
        data = template_file.get("update_patient_family_history_data","")
        return data, url

    def getAddMedicalHistoryTemplate(self, template_file):
        url = template_file.get("add_patient_medical_history_data_url", "")
        data = template_file.get("add_patient_medical_history_data", "")
        return data, url

    def getUpdateMedicalHistoryTemplate(self, template_file):
        url = template_file.get("update_patient_medical_history_data_url", "")
        data = template_file.get("update_patient_medical_history_data","")
        return data, url

    def getAddPatientFoodPrescriptionBasicTemplate(self, template_file):
        url = template_file.get("add_patient_food_prescription_basic_url", "")
        data = template_file.get("add_patient_food_prescription_basic", "")
        return data, url

    def getUpdateFoodPrescriptionBasicTemplate(self, template_file):
        url = template_file.get("update_patient_food_prescription_basic_url","")
        data = template_file.get("update_patient_food_prescription_basic","")
        return data, url

    def getAddPatientAppointmentsTemplate(self, template_file):
        url = template_file.get("add_patient_appointments_url", "")
        data = template_file.get("add_patient_appointments", "")
        return data, url

    def getUpdatePatientAppointmentTemplate(self, template_file):
        url = template_file.get("update_patient_appointments_url", "")
        data = template_file.get("update_patient_appointments", "")
        return data, url

    def getAddWellnessAppointmentSlotTemplate(self, template_file):
        url = template_file.get("add_appointment_slot_url", "")
        data = template_file.get("add_appointment_slot", "")   
        return data, url

    def getUpdateWellnessAppointmentSlotTemplate(self, template_file):
        url = template_file.get("update_appointment_slot_url", "")
        data = template_file.get("update_appointment_slot", "")
        return data, url

    def getAddWellnessInvitationTemplate(self, template_file):
        url = template_file.get("add_wellness_invitation_url", "")
        data = template_file.get("add_wellness_invitation")
        return data, url

    def getUpdateWellnessInvitaionTemlate(self, template_file):
        url = template_file.get("update_wellness_invitation_url", "") 
        data = template_file.get("update_wellness_invitation", "")
        return data, url
 
    def getAddWellnessPanelCollabTemplate(self, template_file):
        url = template_file.get("add_wellness_panel_collab_url", "")
        data = template_file.get("add_wellness_panel_collab", "")
        return data, url 

    def getUpdateWellnessPanelCollabTemplate(self, template_file):
        url = template_file.get("update_wellness_panel_collab_url", "")
        data = template_file.get("update_wellness_panel_collab", "")
        return data, url

    def getAddPatientReferralTemplate(self, template_file):
        url = template_file.get("add_patient_referral_url", "")
        data = template_file.get("add_patient_referral", "")
        return data, url

    def getUpdatePatientReferralTemplate(self, template_file):
        url = template_file.get("update_patient_referral_url", "")
        data = template_file.get("update_patient_referral", "")
        return data, url

    def getAddWellnessCollabChangeTemplate(self, template_file):
        url = template_file.get("add_wellness_collab_change_url", "")
        data = template_file.get("add_wellness_collab_change", "") 
        return data, url

    def getUpdateWellnessCollabChangeTemplate(self,template_file):
        url = template_file.get("update_wellness_collab_change_url", "")
        data = template_file.get("update_wellness_collab_change", "")
        return data, url

    def getAddPatientReferralChangeTemplate(self, template_file):
        url = template_file.get("add_patient_referral_change_url", "")
        data = template_file.get("add_patient_referral_change", "")
        return data, url

    def getUpdatePatientReferralChangeTemplate(self, template_file):
        url = template_file.get("update_patient_referral_change_url", "")
        data = template_file.get("update_patient_referral_change", "")
        return data, url

    def getWellnessPanelCollabByIdTemplate(self, template_file):
        url = template_file.get("get_wellness_panel_collab_data", "")
        return url
 
    def getPatientReferralByIdTemplate(self, template_file):
        url = template_file.get("get_patient_referral_data", "")
        return url

    def getWellnessCollabChangeByIdTemplate(self, template_file):
        url = template_file.get("get_wellness_collab_change_data", "")
        return url

    def getPatientReferralChangeByIdTemplate(self, template_file):
        url = template_file.get("get_patient_referral_change_data", "")
        return url

    def getPatientByIdTemplate(self, template_file):
        url = template_file.get("get_patient_by_id", "")
        return url

    def getWellnessExpertByIdTemplate(self, template_file):
        url = template_file.get("get_wellness_expert_id", "")
        return url

    def getDataAccessorByIdTemplate(self, template_file):
        url = template_file.get("get_data_accessor_id", "")
        return url

    def getPatientAnthropometryByIdTemplate(self, template_file):
        url = template_file.get("get_patient_anthropometry_data", "")
        return url
    
    def getPatientBiochemicalByIdTemplate(self, template_file):
        url = template_file.get("get_patient_biochemical_data", "")
        return url

    def getPatientClinicalByIdTemplate(self, template_file):
        url = template_file.get("get_patient_clinical_data", "")
        return url

    def getPatientDietaryAssessmentByIdTemplate(self, template_file):
        url = template_file.get("get_patient_dietary_data","")
        return url

    def getPatientFoodFrequencyByIdTempalte(self, template_file):
        url = template_file.get("get_patient_food_frequency_data", "")
        return url

    def getPatientFoodRecallByIdTempalte(self, template_file):
        url = template_file.get("get_patient_food_recall_data", "")
        return url

    def getPatientFoodPrescriptionByIdTemplate(self, template_file):
        url = template_file.get("get_patient_food_prescription", "")
        return url
    
    def getPatientPathologyPresecriptionByIdTemplate(self, template_file):
        url = template_file.get("get_patient_pathology_prescription", "")
        return url

    def getPatientPersonalHistoryByIdTemplate(self, template_file):
        url = template_file.get("get_patient_personal_history_data", "")
        return url

    def getPatientLifestyleHabitsByIdTemplate(self, template_file):
        url = template_file.get("get_patient_lifestyle_data", "")
        return url

    def getPatientMiscDataByIdTemplate(self, template_file):
        url = template_file.get("get_patient_misc_data", "")
        return url

    def getPatientFamilyHistoryByIdTemplate(self, template_file):
        url = template_file.get("get_patient_family_history_data", "")
        return url

    def getPatientMedicalHistoryByIdTemplate(self, template_file):
        url = template_file.get("get_patient_medical_history_data", "")
        return url

    def getPatientAppointmentByIdTemplate(self, template_file):
        url = template_file.get("get_patient_appointment", "")
        return url

    def getWellnessAppointmentSlotByIdTemplate(self, template_file):
        url = template_file.get("get_wellness_appointment_slot", "")
        return url
   
    def getWellnessInvitationByIdTemplate(self, template_file):
        url = template_file.get("get_wellness_invitation", "")
        return url
    
    def getPatientFoodPrescriptionBasicByIdTemplate(self, template_file):
        url = template_file.get("get_patient_food_prescription_basic", "") 
        return url
    
    def getAllPatientsTemplate(self, template_file):
        url = template_file.get("get_all_patients", "")
        return url

    def getAllWellnessExpertTemplate(self, template_file):
        url = template_file.get("get_all_wellness_expert","")
        return url

    def getAllPatientAnthropometryByDateTemplate(self, template_file):
        url = template_file.get("get_all_patients_anthropometry_by_date", "")
        return url
 
    def getAllPatientBiochemicalByDateTemplate(self, template_file):
        url = template_file.get("get_all_patients_biochemical_by_date", "") 
        return url

    def getAllPatientClinicalByDateTemplate(self, template_file):
        url = template_file.get("get_all_patients_clinical_data_by_date", "") 
        return url

    def getAllPatientFamilyHistoryByDateTemplate(self, template_file):
        url = template_file.get("get_all_patients_family_history_by_date", "") 
        return url

    def getAllPatientLifestyleHabitsByDateTemplate(self, template_file):
        url = template_file.get("get_all_patients_lifestyle_habits_by_date", "") 
        return url

    def getAllPatientMedicalHistoryByDateTemplate(self, template_file):
        url = template_file.get("get_all_patients_medical_history_by_date", "") 
        return url

    def getAllPatientDietaryAssessmentByDateTemplate(self, template_file):
        url = template_file.get("get_all_patients_dietary_assessment_by_date", "") 
        return url

    def getAllPatientPersonalHistoryByDateTemplate(self, template_file):
        url = template_file.get("get_all_patients_personal_history_by_date", "") 
        return url
 
    def getAllPatientFoodPrescriptionByDateTemplate(self, template_file):
        url = template_file.get("get_all_patients_food_prescription_by_date", "")
        return url

    def getAllPatientPathologyPrescriptionByDateTemplate(self, template_file):
        url = template_file.get("get_all_patients_pathology_prescription_by_date", "")
        return url

    def getAllPatientFoodRecallByDateTemplate(self, template_file):
        url = template_file.get("get_all_patients_food_recall_data", "")
        return url

    def getAllPatientFoodFrequencyByDateTemplate(self, template_file):
        url = template_file.get("get_all_patients_food_frequency_data", "")
        return url
 
    def getAllWellnessInvitationByDateTemplate(self, template_file):
        url = template_file.get("get_all_wellness_invitation_by_date", "")
        return url  
