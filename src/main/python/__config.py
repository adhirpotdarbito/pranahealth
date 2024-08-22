#!/usr/bin/python

'''
    
    Copyright (C) 2018-2020 Isana Systems India Private Limited
    
    This source code is owned and maintained by Isana Systems India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of Isana Systems India Private Limited.
    
'''

import sys
import json

  
# Object to hold all the constant values
class _Const(object):
    ATMAN_CONFIG_FILE_NAME = '/opt/atman/config/atman_config.json'
    PRANACARE_EMAIL_FILE = '/opt/atman/config/pranacare_email_config.json'
    LIFESTYLE_ACTIVITY_MODEL_HYPERTENSION = '/opt/atman/config/activity_model_ht.json'
    HEALTH_SCORE_CONFIG_FILE_NAME = '/opt/atman/config/health_score_config.json'
    STRESS_IMPACTING_DISEASES = 'stress_impacting_diseases'
    EXERCISE_IMPACTING_DISEASES = 'exercise_impacting_diseases'
    CHOLESTEROL_IMPACTING_DISEASES = 'cholesterol_impacting_diseases'
    SMOKING_IMPACTING_DISEASES = 'smoking_impacting_diseases'
    ALCOHOL_IMPACTING_DISEASES = 'alcohol_impacting_diseases'
    PARENTS_DISEASES_MAPPINGS = 'parents_diseases_mappings'
    PARENTS_WEIGHTS_MAPPINGS = 'parents_weights_mappings'
    LIFESTYLE_HABITS_METADATA = 'lifestyle_habits_metadata'
    HEALTH_RISK_LEVELS = 'health_risk_levels'

    HEALTH_SCORE_CONFIG_FILE_NAME = '/opt/atman/config/health_score_config.json'
    STRESS_IMPACTING_DISEASES = 'stress_impacting_diseases'
    EXERCISE_IMPACTING_DISEASES = 'exercise_impacting_diseases'
    CHOLESTEROL_IMPACTING_DISEASES = 'cholesterol_impacting_diseases'
    SMOKING_IMPACTING_DISEASES = 'smoking_impacting_diseases'
    ALCOHOL_IMPACTING_DISEASES = 'alcohol_impacting_diseases'
    PARENTS_DISEASES_MAPPINGS = 'parents_diseases_mappings'
    PARENTS_WEIGHTS_MAPPINGS = 'parents_weights_mappings'
    LIFESTYLE_HABITS_METADATA = 'lifestyle_habits_metadata'
    HEALTH_RISK_LEVELS = 'health_risk_levels'

class AtmanConfigManager:
    #JSON Configuration
    atmanConfigJSON = ''
    atmanConfigData = {}
    pranacareEmailConfigData = {}
    healthScoreConfigJSON = ''
    healthScoreConfigData = {}
    stressImpactingDiseases = []
    exerciseImpactingDiseases = []
    cholesterolImpactingDiseases = []
    smokingImpactingDiseases = []
    alcoholImpactingDiseases = []
    parentsDiseasesMappings = {}
    parentsWeightsMappings = {}
    lifestyleHabitsMetadata = {}
    healthRiskLevels = {}
    

    healthScoreConfigJSON = ''
    healthScoreConfigData = {}
    stressImpactingDiseases = []
    exerciseImpactingDiseases = []
    cholesterolImpactingDiseases = []
    smokingImpactingDiseases = []
    alcoholImpactingDiseases = []
    parentsDiseasesMappings = {}
    parentsWeightsMappings = {}
    lifestyleHabitsMetadata = {}
    healthRiskLevels = {}


    # Default Constructor 
    def __init__(self):
        try:
            CONST = _Const()
            with open(CONST.ATMAN_CONFIG_FILE_NAME) as fileObject:
                self.atmanConfigJSON = fileObject.read()
                #print (self.atmanConfigJSON)
            with open(CONST.PRANACARE_EMAIL_FILE) as fileObject:
                self.pranacareEmailConfigData = json.load(fileObject)
            with open(CONST.ATMAN_CONFIG_FILE_NAME) as fileObject:
                self.atmanConfigData = json.load(fileObject)
                #print (self.atmanConfigData)
            with open(CONST.HEALTH_SCORE_CONFIG_FILE_NAME) as fileObject:
                self.healthScoreConfigJSON = fileObject.read()
                #print (self.healthScoreConfigJSON)
            with open(CONST.HEALTH_SCORE_CONFIG_FILE_NAME) as fileObject:
                self.healthScoreConfigData = json.load(fileObject)
                #print (self.healthScoreConfigData)
                self.stressImpactingDiseases = self.healthScoreConfigData.get(CONST.STRESS_IMPACTING_DISEASES, [])
                #print (self.stressImpactingDiseases)
                self.exerciseImpactingDiseases = self.healthScoreConfigData.get(CONST.EXERCISE_IMPACTING_DISEASES, [])
                #print (self.exerciseImpactingDiseases)
                self.cholesterolImpactingDiseases = self.healthScoreConfigData.get(CONST.CHOLESTEROL_IMPACTING_DISEASES, [])
                #print (self.cholesterolImpactingDiseases)
                self.smokingImpactingDiseases = self.healthScoreConfigData.get(CONST.SMOKING_IMPACTING_DISEASES, [])
                #print (self.smokingImpactingDiseases)
                self.alcoholImpactingDiseases = self.healthScoreConfigData.get(CONST.ALCOHOL_IMPACTING_DISEASES, [])
                #print (self.alcoholImpactingDiseases)
                self.parentsDiseasesMappings = self.healthScoreConfigData.get(CONST.PARENTS_DISEASES_MAPPINGS, {})
                #print (self.parentsDiseasesMappings)
                self.parentsWeightsMappings = self.healthScoreConfigData.get(CONST.PARENTS_WEIGHTS_MAPPINGS, {})
                #print (self.parentsWeightsMappings)
                self.lifestyleHabitsMetadata = self.healthScoreConfigData.get(CONST.LIFESTYLE_HABITS_METADATA, {})
                #print (self.lifestyleHabitsMetadata)
                self.healthRiskLevels = self.healthScoreConfigData.get(CONST.HEALTH_RISK_LEVELS, {})
                #print (self.healthRiskLevels)
        except Exception as err:
            print (Exception,err)
            self.atmanConfigJSON = ''
            self.atmanConfigData = {}
            self.pranacareEmailConfigData = {}
            self.healthScoreConfigJSON = ''
            self.healthScoreConfigData = {}
            self.stressImpactingDiseases = []
            self.exerciseImpactingDiseases = []
            self.cholesterolImpactingDiseases = []
            self.smokingImpactingDiseases  = []
            self.alcoholImpactingDiseases = []
            self.parentsDiseasesMappings = {}
            self.parentsWeightsMappings = {}
            self.lifestyleHabitsMetadata = {}
            self.healthRiskLevels = {}

    #get methods
    def getConfigParamValue(self, configParam):
        return self.atmanConfigData.get(configParam, '')

    def getPranaEmailValue(self, value):
        return self.pranacareEmailConfigData.get(value, '')

    def getStressImpactingDiseases(self):
        return self.stressImpactingDiseases

    def getExerciseImpactingDiseases(self):
        return self.exerciseImpactingDiseases

    def getCholesterolImpactingDiseases(self):
        return self.cholesterolImpactingDiseases

    def getSmokingImpactingDiseases(self):
        return self.smokingImpactingDiseases

    def getAlcoholImpactingDiseases(self):
        return self.alcoholImpactingDiseases

    def getParentsDiseasesMappings(self):
        return self.parentsDiseasesMappings

    def getParentsWeightsMappings(self):
        return self.parentsWeightsMappings

    def getLifestyleHabitsMetadata(self):
        return self.lifestyleHabitsMetadata

    def getHealthRiskLevel(self):
        return self.healthRiskLevels

    def getLifeStyleActivityModelHyperTension(self):
        CONST = _Const()
        return CONST.LIFESTYLE_ACTIVITY_MODEL_HYPERTENSION
    
atmanConfigManager = AtmanConfigManager()

#Helper method to return value for given config parameter
def getAtmanConfigParamValue(configParam):
    return atmanConfigManager.getConfigParamValue(configParam)

def getPranaEmailParameters(value):
    return atmanConfigManager.getPranaEmailValue(value)

def getLifeStyleActivityModelHyperTension():
    return atmanConfigManager.getLifeStyleActivityModelHyperTension()

def getConfigParamValue(configParam):
    return atmanConfigManager.atmanConfigData.get(configParam, '')

def getStressImpactingDiseases():
    return atmanConfigManager.getStressImpactingDiseases()

def getExerciseImpactingDiseases():
    return atmanConfigManager.getExerciseImpactingDiseases()

def getCholesterolImpactingDiseases():
    return atmanConfigManager.getCholesterolImpactingDiseases()

def getSmokingImpactingDiseases():
    return atmanConfigManager.getSmokingImpactingDiseases()

def getAlcoholImpactingDiseases():
    return atmanConfigManager.getAlcoholImpactingDiseases()

def getParentsDiseasesMappings():
    return atmanConfigManager.getParentsDiseasesMappings()

def getParentsWeightsMappings():
    return atmanConfigManager.getParentsWeightsMappings()

def getLifestyleHabitsMetadata():
    return atmanConfigManager.getLifestyleHabitsMetadata()

def getHealthRiskLevel():
    return atmanConfigManager.getHealthRiskLevel()

#call functions which returns dictionary of key and value  
lifestyle_habit = getLifestyleHabitsMetadata()
parents_disease = getParentsDiseasesMappings()
parents_weight = getParentsWeightsMappings()
risk_level = getHealthRiskLevel()
stress_disease = getStressImpactingDiseases()
exercise_impact_disease = getExerciseImpactingDiseases()
cholesterol_disease = getCholesterolImpactingDiseases()
smoking_disease = getSmokingImpactingDiseases()
alcohol_disease = getAlcoholImpactingDiseases()

# assign constants for parameters value
both = parents_weight.get("both", "2")
father = parents_weight.get("father", "1")
mother = parents_weight.get("mother", "0")
regular = lifestyle_habit.get("ls_habit_param_value_regular")
occasional = lifestyle_habit.get("ls_habit_param_value_ocassional")
n_a = lifestyle_habit.get("ls_habit_param_value_na")
intense = lifestyle_habit.get("ls_habit_exercise_level_intense")
moderate = lifestyle_habit.get("ls_habit_exercise_level_moderate")
mild = lifestyle_habit.get("ls_habit_exercise_level_mild")
Low = risk_level.get("health_risk_level_low").title()
Fair = risk_level.get("health_risk_level_fair").title()
Moderate = risk_level.get("health_risk_level_moderate").title()
High = risk_level.get("health_risk_level_high").title()
host = getAtmanConfigParamValue("PRANA_CARE_MESSAGE_QUEUE_HOST")
port = getAtmanConfigParamValue("PRANA_CARE_MESSAGE_QUEUE_PORT")
queue_name_blockchain = getAtmanConfigParamValue("PRANA_CARE_QUEUE_NAME_BLOCKCHAIN")
queue_name_db = getAtmanConfigParamValue("PRANA_CARE_QUEUE_NAME_DB")
queue_name_notification = getAtmanConfigParamValue("PRANA_CARE_QUEUE_NAME_NOTIFICATION") 
GENERAL_REMINDER = getAtmanConfigParamValue("GENERAL_REMINDER")
APPOINTMENT_REMINDER = getAtmanConfigParamValue("APPOINTMENT_REMINDER")
APPOINTMENT_REMINDER_DIETITIAN = getAtmanConfigParamValue("APPOINTMENT_REMINDER_DIETITIAN")
FOOD_PRESCRIPTION = getAtmanConfigParamValue("FOOD_PRESCRIPTION")
PATHOLOGY_PRESCRIPTION = getAtmanConfigParamValue("PATHOLOGY_PRESCRIPTION")
PATIENT_ENQUIRY = getAtmanConfigParamValue("PATIENT_ENQUIRY")
email_host = getPranaEmailParameters("server")
email_port = getPranaEmailParameters("port")
email_name = getPranaEmailParameters("email")
email_password = getPranaEmailParameters("password")
DIETITION_ACL = getAtmanConfigParamValue("DIETITIAN_ROLE")
USER_ACL = getAtmanConfigParamValue("USER_ROLE")
DIETITIAN = getAtmanConfigParamValue("DIETITIAN")
GROUP_NOTIFICATION = getAtmanConfigParamValue("GROUP_NOTIFICATION")
SCHEDULED_NOTIFICATION = getAtmanConfigParamValue("SCHEDULED_NOTIFICATION")
mongodb_connect = getAtmanConfigParamValue("MONGODB_CONNECT")
bigchain_connect = getAtmanConfigParamValue("BIGCHAIN")
flag_email = getAtmanConfigParamValue("FLAG_EMAIL")
flag_whatsapp = getAtmanConfigParamValue("FLAG_WHATSAPP")
rabbitmq_user = getAtmanConfigParamValue("RABBITMQ_USER")
rabbitmq_pass = getAtmanConfigParamValue("RABBITMQ_PASS")
USER_REGISTER = getAtmanConfigParamValue("USER_REGISTER")
CHANGE_MAIL = getAtmanConfigParamValue("CHANGE_MAIL")
#APPOINTMENT_REQUESTED = getAtmanConfigParamValue("APPOINTMENT_REQUESTED")
APPOINTMENT_REQUESTED_BOOKED = getAtmanConfigParamValue("APPOINTMENT_REQUESTED_BOOKED") 
APPOINTMENT_REQUESTED_CONFIRMED = getAtmanConfigParamValue("APPOINTMENT_REQUESTED_CONFIRMED")
APPOINTMENT_BOOKED_PATIENT = getAtmanConfigParamValue("APPOINTMENT_BOOKED_PATIENT")
APPOINTMENT_BOOKED_DIETITIAN = getAtmanConfigParamValue("APPOINTMENT_BOOKED_DIET")
APPOINTMENT_REQUESTED_DIET = getAtmanConfigParamValue("APPOINTMENT_REQUESTED_DIET")
APPOINTMENT_REQUESTED_PATIENT = getAtmanConfigParamValue("APPOINTMENT_REQUESTED_PATIENT") 
APPOINTMENT_BOOKED_CANCELLED_PATIENT = getAtmanConfigParamValue("APPOINTMENT_BOOKED_CANCELLED_PATIENT")
APPOINTMENT_BOOKED_CANCELLED_DIET = getAtmanConfigParamValue("APPOINTMENT_BOOKED_CANCELLED_DIET")
APPOINTMENT_UPDATED = getAtmanConfigParamValue("APPOINTMENT_UPDATED")
APPOINTMENT_REMINDER_MAIL = getAtmanConfigParamValue("APPOINTMENT_REMINDER_MAIL") 
APPOINTMENT_REQUESTED_CANCELLED_PATIENT = getAtmanConfigParamValue("APPOINTMENT_REQUESTED_CANCELLED_PATIENT")
APPOINTMENT_REQUESTED_CANCELLED_DIET = getAtmanConfigParamValue("APPOINTMENT_REQUESTED_CANCELLED_DIET")
ANONYMOUS_TOKEN = getAtmanConfigParamValue("ANONYMOUS_TOKEN")
FORGET_PASSWORD = getAtmanConfigParamValue("FORGET_PASSWORD")
NOTIFICATION_BIOCHEMICAL = getAtmanConfigParamValue("NOTIFICATION_BIOCHEMICAL")
PATIENT_REFER = getAtmanConfigParamValue("PATIENT_REFER")
PATIENT_REFER_ADMIN = getAtmanConfigParamValue("PATIENT_REFER_ADMIN")
PATIENT_REFER_MEMBER = getAtmanConfigParamValue("PATIENT_REFER_MEMBER")
APPOINTMENT_COMPLETED = getAtmanConfigParamValue("APPOINTMENT_COMPLETED")
WELLNESS_COLLABORATION = getAtmanConfigParamValue("WELLNESS_COLLABORATION")
WELLNESS_PANEL = getAtmanConfigParamValue("WELLNESS_PANEL")
ADMIN_WELLNESS_ACCEPTANCE = getAtmanConfigParamValue("ADMIN_WELLNESS_ACCEPTANCE")
PATIENT_WELLNESS_BLOCKED = getAtmanConfigParamValue("PATIENT_WELLNESS_BLOCKED")
REFER_PATIENT = getAtmanConfigParamValue("REFER_PATIENT")
WELLNESS_INVITATION = getAtmanConfigParamValue("WELLNESS_INVITATION")
WELLNESS_INVITATION_CREATED = getAtmanConfigParamValue("WELLNESS_INVITATION_CREATED")
CREATE_USER_WELLNESS = getAtmanConfigParamValue("CREATE_USER_WELLNESS")
COLLABORATION_CONFIRM = getAtmanConfigParamValue("COLLABORATION_CONFIRM")
CUSTOM_FORM_DATA = getAtmanConfigParamValue("CUSTOM_FORM_DATA")
USER_AUDIT_TRAIL_LOGIN = getAtmanConfigParamValue("USER_AUDIT_TRAIL_LOGIN")
DIET_AUDIT_TRAIL_LOGIN = getAtmanConfigParamValue("DIET_AUDIT_TRAIL_LOGIN")
USER_AUDIT_TRAIL_LOGOUT = getAtmanConfigParamValue("USER_AUDIT_TRAIL_LOGOUT")
USER_AUDIT_TRAIL_FORGOT_PASSWORD_TOKEN = getAtmanConfigParamValue("USER_AUDIT_TRAIL_FORGOT_PASSWORD_TOKEN")
USER_AUDIT_TRAIL_FORGOT_PASSWORD_VERIFY = getAtmanConfigParamValue("USER_AUDIT_TRAIL_FORGOT_PASSWORD_VERIFY")
USER_AUDIT_TRAIL_OTP_GENERATION = getAtmanConfigParamValue("USER_AUDIT_TRAIL_OTP_GENERATION")
USER_AUDIT_TRAIL_OTP_VERIFICATION = getAtmanConfigParamValue("USER_AUDIT_TRAIL_OTP_VERIFICATION")
USER_AUDIT_TRAIL_USER_UPDATE = getAtmanConfigParamValue("USER_AUDIT_TRAIL_USER_UPDATE")
OTP_GENERATION = getAtmanConfigParamValue("OTP_GENERATION")
OTP_VERIFICATION = getAtmanConfigParamValue("OTP_VERIFICATION")
USER_LOGIN = getAtmanConfigParamValue("USER_LOGIN")
USER_LOGOUT = getAtmanConfigParamValue("USER_LOGOUT")
USER_UPDATE = getAtmanConfigParamValue("USER_UPDATE")	
FORGOT_PASSWORD = getAtmanConfigParamValue("FORGOT_PASSWORD")
