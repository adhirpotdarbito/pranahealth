import logging
import re
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from __composer_config import *
from __composer_insert_data import *
from __user_queue_data import *
from __message_queue import *
from __message import *
from __config import *
from __notification_utils import *


class ComposerConsumer(QueueData):
    def __init__(self):
        super(ComposerConsumer, self).__init__()
        logging.basicConfig(filename='/var/log/atman/composer_consumer.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        handler = TimedRotatingFileHandler('/var/log/atman/composer.log',when='midnight',interval=1,backupCount=5)
        logger.addHandler(handler)
        return None

    def callback(self, ch, method, properties, body):
        #print(body)
        self.processingFunction(body)

    def processingFunction(self, message_recieved):
        __composer_config = ComposerConfig()
        template_file = __composer_config.getJsonTemplate()
        header = json.loads(__composer_config.getHeader(template_file))
        _message_recieved = json.loads(message_recieved)
        date = datetime.now().strftime("%Y%m%d %H:%M:%S")
        file_name = "/opt/atman/bin/blockchain_info_"+datetime.now().strftime("%Y%m%d")+".csv"
        if _message_recieved.get("parameter_type") != WELLNESS_COLLABORATION:
            patient_user_id = _message_recieved.get("user_id", "")
            patient_id = _message_recieved.get("user_email_id", "")
            wellness_id = _message_recieved.get("wellness_email_id", "")
            wellness_type = _message_recieved.get("wellness_type", "")
            wellness_info = _message_recieved.get("wellness_info", "")
            wellness_name = _message_recieved.get("wellness_name", None)
            if getWellnessExpertById(wellness_id, template_file, __composer_config) != 200 and _message_recieved.get("parameter_type", "") != ANONYMOUS_TOKEN and wellness_id != patient_id:
                print("Adding wellness Expert "+wellness_id+": "+ date)
                logging.info("Adding Wellness Expert " + wellness_id)
                insertWellnessExpert(wellness_id, wellness_type, wellness_info, template_file, __composer_config, header)
                logging.info("Added Wellness Expert " + wellness_id)
                print("Added wellness Expert "+wellness_id+": "+ date)
            if getPatientById(patient_id, template_file, __composer_config) != 200 and _message_recieved.get("parameter_type", "") != ANONYMOUS_TOKEN and wellness_id != patient_id:
                print("Adding Patient "+patient_id)
                logging.info("Adding Patient " + patient_id)
                insertPatient(patient_id, wellness_id, template_file, __composer_config, header)
                logging.info("Added Patient " + patient_id)
            if getDataAccessorById(wellness_id, template_file, __composer_config) != 200 and _message_recieved.get("parameter_type", "") != ANONYMOUS_TOKEN and wellness_id != patient_id:
                print("Adding Data Accessor " + wellness_id)
                logging.info("Adding Data Accessor " + wellness_id)
                insertDataAccessor(wellness_id, wellness_type, template_file, __composer_config, header)
                logging.info("Added Data Accessor " + wellness_id)
            if _message_recieved.get("parameter_type", "") == "User Misc Data":
                asset_keys = json.loads(_message_recieved.get("message", {}).get("miscData", {}))
                _asset_keys = asset_keys.keys()
                for asset in _asset_keys:
                    if asset == "Personal_History":
                        personal_history = str(asset_keys.get(asset, {}))
                        if getPatientPersonalHistory(patient_id,template_file, __composer_config) == 200:
                            print (asset + " appending for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            updatePatientPersonalHistory(patient_id, date, personal_history, template_file, __composer_config, header)
                            logging.info("Updated data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Updated", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Updated", date)
                        else:
                            print (asset + " inserting for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            insertPatientPersonalHistory(patient_id, wellness_id, date, personal_history, wellness_id, template_file, __composer_config, header)
                            logging.info("Inserted data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Inserted", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Inserted", date)
                    elif asset == "BioChemical":
                        biochemical = str(asset_keys.get(asset, {}))
                        if getPatientBiochemicalData(patient_id,template_file, __composer_config) == 200:
                            print (asset + " appending for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            updatePatientBiochemicalData(patient_id, date, biochemical, template_file, __composer_config, header)
                            logging.info("Updated data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Updated", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Updated", date)
                        else:
                            print (asset + " inserting for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            insertPatientBiochemicalData(patient_id, wellness_id, date, biochemical, wellness_id, template_file, __composer_config, header)
                            logging.info("Inserted data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Inserted", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Inserted", date)
                    elif asset == "Food_Frequency":
                        food_frequency = str(asset_keys.get(asset, {}))
                        if getPatientFoodFrequency(patient_id,template_file, __composer_config) == 200:
                            print (asset + " appending for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            updatePatientFoodFrequency(patient_id, date, food_frequency, template_file, __composer_config, header)
                            logging.info("Updated data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Updated", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Updated", date)
                        else:
                            print (asset + " inserting for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            insertPatientFoodFrequency(patient_id, wellness_id, date, food_frequency, wellness_id, template_file, __composer_config, header)
                            logging.info("Inserted data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Inserted", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Inserted", date)
                    elif asset == "Lifestyle":
                        lifestyle_habit = str(asset_keys.get(asset, {}))
                        if getPatientLifestyleHabit(patient_id,template_file, __composer_config) == 200:
                            print (asset + " appending for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            updatePatientLifestyleHabits(patient_id, date, lifestyle_habit, template_file, __composer_config, header)
                            logging.info("Updated data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Updated", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Updated", date)
                        else:
                            print (asset + " inserting for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            insertPatientLifestyleHabits(patient_id, wellness_id, date, lifestyle_habit, wellness_id, template_file, __composer_config, header)
                            logging.info("Inserted data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Inserted", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Inserted", date)
                    elif asset == "Anthropometry":
                        anthropometry = str(asset_keys.get(asset, {}))
                        if getPatientAnthropometryData(patient_id,template_file, __composer_config) == 200:
                            print (asset + " appending for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            updatePatientAnthropometryData(patient_id, date, anthropometry, template_file, __composer_config, header)
                            logging.info("Updated data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Updated", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Updated", date)
                        else:
                            print (asset + " inserting for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            insertPatientAnthropometryData(patient_id, wellness_id, date, anthropometry, wellness_id, template_file, __composer_config, header)
                            logging.info("Inserted data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Inserted", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Inserted", date)
                    elif asset == "Clinical":
                        clinical = str(asset_keys.get(asset, {}))
                        if getPatientClinicalData(patient_id,template_file, __composer_config) == 200:
                            print (asset + " appending for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            updatePatientClinicalData(patient_id, wellness_id, date, clinical, template_file, __composer_config, header)
                            logging.info("Updated data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Updated", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Updated", date)
                        else:
                            print (asset + " inserting for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            insertPatientClinicalData(patient_id, wellness_id, date, clinical, wellness_id, template_file, __composer_config, header)
                            logging.info("Inserted data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Inserted", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Inserted", date)
                    elif asset == "Dietary_Assessment":
                        dietary_assessment = str(asset_keys.get(asset, {}))
                        if getPatientDietaryAssessment(patient_id,template_file, __composer_config) == 200:
                            print (asset + " appending for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            updatePatientDietaryAssessment(patient_id, date, dietary_assessment, template_file, __composer_config, header)
                            logging.info("Updated data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Updated", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Updated", date)
                        else:
                            print (asset + " inserting for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            insertPatientDietaryAssessmentData(patient_id, wellness_id, date, dietary_assessment, wellness_id, template_file, __composer_config, header)
                            logging.info("Inserted data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Inserted", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Inserted", date)
                    elif asset == "Food_Recall":
                        food_recall = str(asset_keys.get(asset, {}))
                        if getPatientFoodRecall(patient_id,template_file, __composer_config) == 200:
                            print (asset + " appending for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            updatePatientFoodRecall(patient_id, date, food_recall, template_file, __composer_config, header)
                            logging.info("Updated data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Updated", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Updated", date)
                        else:
                            print (asset + " inserting for " + patient_id + ": " + date)
                            logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+asset)
                            insertPatientFoodRecall(patient_id, wellness_id, date, food_recall, wellness_id, template_file, __composer_config, header)
                            logging.info("Inserted data from " + wellness_id + " for "+ patient_id +": "+asset)
                            logging.info("Writing data to CSV file")
                            if wellness_name == None:
                                createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, asset, "Inserted", date)
                            else:
                                createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, asset, "Inserted", date)
            if _message_recieved.get("parameter_type", "") == "Food Prescription":
                _food_prescription = _message_recieved.get("message", {}).get("food_prescription_template_instance", [])
                if _food_prescription != []:
                    food_prescription = json.dumps(_food_prescription[0].get("instance", ""))[1:-1]
                else:
                    _food_prescription = _message_recieved.get("message", {}).get("admin_patient_food_data", [])
                    if _food_prescription != []:
                        food_prescription = json.dumps(_food_prescription[0].get("foodPrescription", {}))[1:-1]
                if getPatientFoodPrescription(patient_id, template_file, __composer_config) == 200:
                    print ("Food_Prescription appending for " + patient_id + ": " + date)
                    logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+"Food Prescription")
                    updatePatientFoodPrescription(patient_id, date, food_prescription, template_file, __composer_config, header)
                    logging.info("Updated data from " + wellness_id + " for "+ patient_id +": "+"Food Prescription")
                    logging.info("Writing data to CSV file")
                    if wellness_name == None: 
                        createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, "Food Prescription", "Updated", date)
                    else: 
                        createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, "Food Prescription", "Updated", date)
                else:
                    print ("Food_Prescription inserting for " + patient_id + ": " + date)
                    logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+"Food Prescription")
                    insertPatientFoodPrescription(patient_id, wellness_id, date, food_prescription, wellness_id, template_file, __composer_config, header)
                    logging.info("Inserted data from " + wellness_id + " for "+ patient_id +": "+"Food Prescription")
                    logging.info("Writing data to CSV file")
                    if wellness_name == None:
                        createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, "Food Prescription", "Inserted", date)
                    else:
                        createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, "Food Prescription", "Inserted", date)
            if _message_recieved.get("parameter_type", "") == "Pathology Prescription":
                _pathology_prescription = _message_recieved.get("message", {}).get("admin_patient_pathology_prescription", [])
                if _pathology_prescription != []:
                    pathology_prescription = json.dumps(_pathology_prescription[0].get("pathoPrescription", ""))[1:-1]
                    if getPatientPathologyPrescription(patient_id, template_file, __composer_config) == 200:
                        print ("Pathology_Prescription appending for " + patient_id + ": " + date)
                        logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+"Pathology Prescription")
                        updatePatientPathologyPrescription(patient_id, date, pathology_prescription, template_file, __composer_config, header)
                        logging.info("Updated data from " + wellness_id + " for "+ patient_id +": "+"Pathology Prescription")
                        logging.info("Writing data to CSV file")
                        if wellness_name == None:
                            createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, "Pathology Prescription", "Updated", date)
                        else:
                            createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, "Pathology Prescription", "Updated", date)
                    else:
                        print ("Pathology_Prescription inserting for " + patient_id + ": " + date)
                        logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+"Pathology Prescription")
                        insertPatientPathologyPrescription(patient_id, wellness_id, date, pathology_prescription, wellness_id, template_file, __composer_config, header)
                        logging.info("Inserted data from " + wellness_id + " for "+ patient_id +": "+"Pathology Prescription")
                        logging.info("Writing data to CSV file")
                        if wellness_name == None:
                            createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, "Pathology Prescription", "Inserted", date)
                        else:
                            createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, "Pathology Prescription", "Inserted", date)
            if _message_recieved.get("parameter_type", "") == "User Family History":
                family_history = _message_recieved.get("message", {})
                if getPatientFamilyHistory(patient_id, template_file, __composer_config) == 200:
                    print ("User Family History appending for " + patient_id + ": " + date)
                    logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+"Family History")
                    updatePatientFamilyHistory(patient_id, date, family_history, template_file, __composer_config, header)
                    logging.info("Updated data from " + wellness_id + " for "+ patient_id +": "+"Family History")
                    logging.info("Writing data to CSV file")
                    if wellness_name == None:
                        createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, "Family History", "Updated", date)
                    else: 
                        createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, "Family History", "Updated", date)
                else:
                    print ("User Family History inserting for " + patient_id + ": " + date)
                    logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+"Family History")
                    insertPatientFamilyHistory(patient_id, wellness_id, date, family_history, wellness_id, template_file, __composer_config, header)
                    logging.info("Inserted data from " + wellness_id + " for "+ patient_id +": "+"Family History")
                    logging.info("Writing data to CSV file")
                    if wellness_name == None:
                        createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, "Family History", "Inserted", date)
                    else:
                        createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, "Family History", "Inserted", date)
            if _message_recieved.get("parameter_type", "") == "User Medical Data":
                medical_history = _message_recieved.get("message", {})
                if getPatientMedicalHistory(patient_id, template_file, __composer_config) == 200:
                    print ("Medical History appending for " + patient_id + ": " + date)
                    logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+"Medical History")
                    updatePatientMedicalHistory(patient_id, date, medical_history, template_file, __composer_config, header)
                    logging.info("Updated data from " + wellness_id + " for "+ patient_id +": "+"Medical History")
                    logging.info("Writing data to CSV file")
                    if wellness_name == None:
                        createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, "Medical History", "Updated", date)
                    else:
                        createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, "Medical History", "Updated", date)
                else:
                    print ("Medical History inserting for " + patient_id + ": " + date)
                    logging.info("Storing data from " + wellness_id + " for "+ patient_id +": "+"Medical History")
                    insertPatientMedicalHistory(patient_id, wellness_id, date, medical_history, wellness_id, template_file, __composer_config, header)
                    logging.info("Inserted data from " + wellness_id + " for "+ patient_id +": "+"Medical History")
                    logging.info("Writing data to CSV file")
                    if wellness_name == None:
                        createCsvBlockchainInfo(file_name, wellness_id, patient_user_id, "Medical History", "Inserted", date)
                    else:
                        createCsvBlockchainInfo(file_name, wellness_name, patient_user_id, "Medical History", "Inserted", date)

        if _message_recieved.get("parameter_type", "") in ["Admin Slot Created", "Admin Slot Updated", "Admin Slot Deleted"]:
            wellness_id = _message_recieved.get("wellness_email_id", "")
            status = _message_recieved.get("parameter_type", "")
            appointment_slot = _message_recieved.get("message", {}).get("slot_data", "")
            if getWellnessAppointmentSlot(wellness_id, template_file, __composer_config) == 200:
                logging.info("Updating Wellness Appointment Slot for wellness  "+ wellness_id)
                updateWellnessAppointmentSlot(wellness_id, date, status, appointment_slot, template_file, __composer_config, header)
                logging.info("Updated Wellness Appointment Slot for wellness  "+ wellness_id + ": " + status)
                print("Updated Wellness Appointment Slot for wellness  "+ wellness_id + ": " + status)
            else:
                logging.info("Storing Wellness Appointment slot for wellness " + wellness_id + ": " + status)
                insertWellnessAppointmentSlot(wellness_id, date, status, appointment_slot, wellness_id, template_file, __composer_config, header)
                print("Inserted Wellness Appointment Slot for wellness  "+ wellness_id + ": " + status)
        
        if _message_recieved.get("parameter_type", "") in ["Appointment Booked/Requested", "Appointment Updated", "Appointment Cancelled"]:
            patient_id = _message_recieved.get("user_email_id", "") 
            wellness_id = _message_recieved.get("wellness_email_id", "")
            status = _message_recieved.get("parameter_type", "")
            appointment = _message_recieved.get("message", {}).get("appointment_data", "")
            if getPatientAppointments(patient_id, template_file, __composer_config) == 200:
                logging.info("Updating Patient appointment for "+ patient_id+ ": "+ status)
                updatePatientAppointments(patient_id, date, status, appointment, wellness_id, template_file, __composer_config, header) 
                logging.info("Updated Patient appointment for "+ patient_id+ ": "+ status)
                print("Updated Patient appointment for "+ patient_id+ ": "+ status)
            else:
                logging.info("Storing Patient appointment for "+ patient_id+ ": "+ status)
                insertPatientAppointments(patient_id, date, status, appointment, wellness_id, wellness_id, template_file, __composer_config, header) 
                logging.info("Inserted Patient appointment for "+ patient_id+ ": "+ status)
                print("Inserted Patient appointment for "+ patient_id+ ": "+ status)
                
        if _message_recieved.get("parameter_type", "") == WELLNESS_COLLABORATION:
            if _message_recieved.get("message", "").get("collaboration_type", "") == WELLNESS_PANEL:
                wellness_id = _message_recieved.get("message", {}).get("admin", {}).get("email", "")
                member_id = _message_recieved.get("message", {}).get("member", {}).get("email", "")
                wellness_type = _message_recieved.get("wellness_type", "")
                wellness_contact = _message_recieved.get("message", {}).get("admin", {}).get("contact", "")
                wellness_gender = _message_recieved.get("message", {}).get("admin", {}).get("gender", "")
                wellness_city = _message_recieved.get("message", {}).get("admin", {}).get("city", "")
                wellness_country = _message_recieved.get("message", {}).get("admin", "").get("country", "")
                member_type = _message_recieved.get("message", {}).get("member", {}).get("member_type", "")
                member_contact = _message_recieved.get("message", {}).get("member", {}).get("contact", "")
                member_gender = _message_recieved.get("message", {}).get("member", {}).get("gender", "")
                member_city = _message_recieved.get("message", {}).get("member", {}).get("city", "")
                member_country = _message_recieved.get("message", {}).get("member", "").get("country", "")
                panel_id = _message_recieved.get("message", {}).get("wellnss_panel_collaboration", "").get("panelId", "")
                member_consent = _message_recieved.get("message", {}).get("wellnss_panel_collaboration", "").get("memberConsent", "")
                panel_name = _message_recieved.get("message", {}).get("wellnss_panel_collaboration", {}).get("panelName", "")
                panel_description = _message_recieved.get("message", {}).get("wellnss_panel_collaboration", {}).get("panelDescription", "")
                if getWellnessCollab(wellness_id, template_file, __composer_config) == 200:
                    updateWellnessPanelCollab(wellness_id, date, wellness_id, member_id, member_consent, wellness_type, wellness_contact, wellness_id, wellness_gender, wellness_city, wellness_country, member_type, member_contact, member_id, member_gender, member_city, member_country, template_file, __composer_config, header)
                    logging.info("Updated wellness panel collaboration data for wellnessId: " + wellness_id + " with member_id: " + member_id)
                else:
                    logging.info("Storing wellness panel Collaboration Data for wellnessId: "+ wellness_id + " with member_id: " + member_id)
                    insertWellnessPanelCollab(wellness_id, panel_id, panel_name, panel_description, date, wellness_id, member_id, member_consent, wellness_type, wellness_contact, wellness_id, wellness_gender, wellness_city, wellness_country, member_type, member_contact, member_id, member_gender, member_city, member_country, template_file, __composer_config, header)
                    logging.info("Inserted wellness collab data for wellnessId: " + wellness_id +", with member_id: " +member_id)

            if _message_recieved.get("message", {}).get("collaboration_type", "") == REFER_PATIENT:
                wellness_id = _message_recieved.get("message", {}).get("admin", {}).get("email", "")
                member_id = _message_recieved.get("message", {}).get("member", {}).get("email", "")
                wellness_type = _message_recieved.get("wellness_type", "")
                wellness_contact = _message_recieved.get("message", {}).get("admin", {}).get("contact", "")
                wellness_gender = _message_recieved.get("message", {}).get("admin", {}).get("gender", "")
                wellness_city = _message_recieved.get("message", {}).get("admin", {}).get("city", "")
                wellness_country = _message_recieved.get("message", {}).get("admin", "").get("country", "")
                member_type = _message_recieved.get("message", {}).get("member", {}).get("memberType", "")
                member_contact = _message_recieved.get("message", {}).get("member", {}).get("contact", "")
                member_gender = _message_recieved.get("message", {}).get("member", {}).get("gender", "")
                member_city = _message_recieved.get("message", {}).get("member", {}).get("city", "")
                member_country = _message_recieved.get("message", {}).get("member", "").get("country", "")
                panel_id = _message_recieved.get("message", {}).get("patient_refer", "").get("panelId", "")
                panel_name = _message_recieved.get("message", {}).get("patient_refer", {}).get("panelName", "")
                panel_description = _message_recieved.get("message", {}).get("patient_refer", {}).get("panelDescription", "")
                refer_consent = _message_recieved.get("message", {}).get("patient_refer", {}).get("patientReferConsent", "")
                referral_notes = json.loads(_message_recieved.get("message", {}).get("patient_refer", {}).get("referalNote", ""))
                data_share_consent = _message_recieved.get("message", {}).get("patient_refer", {}).get("patientDataSharingConsent", "")
                patient_id = _message_recieved.get("message", {}).get("patient", {}).get("email", "")
                patient_type = json.loads(_message_recieved.get("message").get("patient_refer", {}).get("patientDetails", {})).get("category", "")
                patient_contact = _message_recieved.get("message", {}).get("patient", {}).get("Contact", "")
                patient_gender = _message_recieved.get("message", {}).get("patient", {}).get("gender", "")
                patient_city = _message_recieved.get("message", {}).get("patient", {}).get("city", "")
                patient_country = _message_recieved.get("message", {}).get("patient", {}).get("country", "")
                patient_age = json.loads(_message_recieved.get("message", {}).get("patient_refer", {}).get("patientDetails", {})).get("age", "")
                if getPatientCollab(patient_id, template_file, __composer_config) == 200:
                    logging.info("Updating patient referral data for patientId: " + patient_id + " with adminId: " + wellness_id + " and memberId: " + member_id) 
                    updatePatientReferral(patient_id, date, wellness_id, member_id, data_share_consent, refer_consent, referral_notes, patient_type, patient_contact, patient_id, patient_gender, patient_city, patient_country, patient_age, wellness_type, wellness_contact, wellness_id, wellness_gender, wellness_city, wellness_country, member_type, member_contact, member_id, member_gender, member_city, member_country, template_file, __composer_config, header)
                    logging.info("Updated patient referral data for patientId: " + patient_id + " with adminId: " + wellness_id + "and memberId: " + member_id)
                else:
                    logging.info("Storing patient referral data for patientId: " + patient_id + " with adminId: " + wellness_id + " with memberId: " + member_id) 
                    insertPateintReferral(patient_id, panel_id, panel_name, panel_description, date, wellness_id, member_id, data_share_consent, refer_consent, referral_notes, patient_type, patient_contact, patient_id, patient_gender, patient_city, patient_country, patient_age, wellness_type, wellness_contact, wellness_id, wellness_gender, wellness_city, wellness_country, member_type, member_contact, member_id, member_gender, member_city, member_country, template_file, __composer_config, header)
                    logging.info("Inserted patient referral data for patient_id: " + patient_id + " with adminId: " + wellness_id + " with memberId: "+ member_id)
            if _message_recieved.get("message", {}).get("collaboration_type", "") == ADMIN_WELLNESS_ACCEPTANCE:
                wellness_id = _message_recieved.get("message", {}).get("admin", {}).get("email", "")
                member_id = _message_recieved.get("message", {}).get("member", {}).get("email", "")
                if getWellnessCollabChange(wellness_id, template_file, __composer_config) == 200:
                    logging.info("Updating wellness collaboration acceptance data for adminId: " + wellness_id + " for member_id: " + member_id)
                    updateWellnessCollabChange(wellness_id, date, member_id, template_file, __composer_config, header)    
                    logging.info("Updated wellness collaboration acceptance data for adminId: " + wellness_id + " for member_id: " + member_id)
                else:
                    logging.info("Storing wellness collaboration acceptance data for adminId: " + wellness_id + " for member_id: " + member_id)
                    insertWellnessCollabChange(wellness_id, date, member_id, template_file, __composer_config, header)
                    logging.info("Inserted wellness collaboration acceptance data for adminId: " + wellness_id + " for member_id: " + member_id)

            if _message_recieved.get("message", {}).get("collaboration_type", "") == PATIENT_WELLNESS_BLOCKED:
                patient_id = _message_recieved.get("message", {}).get("patient", {}).get("email", "")
                wellness_id = _message_recieved.get("message", {}).get("admin", {}).get("email", "")
                member_id = _message_recieved.get("message", {}).get("member", {}).get("email", "")
                collaboration = _message_recieved.get("message", {}).get("patient_wellness_blocked", {}).get("referralConsent", "")
                if getPatientReferralChange(patient_id, template_file, __composer_config) == 200:
                    logging.info("Updating patient referral blocked data for patientId: " + patient_id + " with adminId: " + wellness_id + " and memberId: " + member_id)
                    updatePatientReferralChange(patient_id, date, wellness_id, member_id, collaboration, template_file, __composer_config, header)
                    logging.info("patient referral blocked data for patientId: " + patient_id + " with adminId: " + wellness_id + " and memberId: " + member_id)
                else:
                    logging.info("Storing patient referral blocked data for patientId: " + patient_id + " with adminId: " + wellness_id + " and memberId: " + member_id)
                    insertPatientReferralChange(patient_id, date, wellness_id, member_id, collaboration, template_file, __composer_config, header)
                    logging.info("Inserted patient referral blocked data for patientId: " + patient_id + " with adminId: " + wellness_id + " and memberId: " + member_id)

        if _message_recieved.get("parameter_type", "") == WELLNESS_INVITATION_CREATED: 
            wellness_id = _message_recieved.get("wellness_email_id", "")
            admin_details = _message_recieved.get("message", {}).get("adminDetails", "")       
            member_detail_json = json.loads(_message_recieved.get("message", {}).get("memberDetails", '{}'))
            member_name = member_detail_json.get("name", "")
            member_type = member_detail_json.get("type", "")
            member_contact = member_detail_json.get("contact", "")
            member_email = member_detail_json.get("email", "")
            member_city = member_detail_json.get("city", "")
            member_country = member_detail_json.get("country", "")
            member_gender = member_detail_json.get("gender", "")
            member_password = member_detail_json.get("password", "")
            terms_condition = member_detail_json.get("termsConditions", "")
            member_info = {'member_name': member_name, 'member_type':member_type, 'member_contact':member_contact, 'member_email':member_email, 'member_city' : member_city, 'member_country':member_country, 'member_gender':member_gender}
            _terms = member_detail_json.get("terms", "")
            terms = repr(re.sub("[^a-zA-Z0-9 \n\.]", '', _terms))
            _message = member_detail_json.get("message", "")
            status = _message_recieved.get("message", {}).get("inviteStatus", "")
            if getWellnessInvitationById(wellness_id, template_file, __composer_config) == 200:
                logging.info("Updating Wellness Invitation from: " + wellness_id + " to member: " + member_email + " with status: " + status)
                updateWellnessInvitation(wellness_id, date, member_type, member_contact, member_email, member_gender, member_city, member_country, member_name, _message, member_password ,terms_condition, status, terms, template_file, __composer_config, header)              
                logging.info("Updated Wellness Invitation from: " + wellness_id + " to member: " + member_email + " with status: " + status)
            else:
                logging.info("Storing Wellness Invitation from: " + wellness_id + " to member: " + member_email + " with status: " + status)
                insertWellnessInvitaion(wellness_id, admin_details, date, member_type, member_contact, member_email, member_gender, member_city, member_country, member_name, _message, member_password, terms_condition, status, terms, template_file, __composer_config, header)
                logging.info("Stored Wellness Invitation from: " + wellness_id + " to member: " + member_email + " with status: " + status)
            if status == 'accepted':
                if getWellnessExpertById(member_email, template_file, __composer_config) != 200:
                    print("Adding wellness Expert "+member_email+": "+ date)
                    logging.info("Adding Wellness Member to Wellness Expert " + member_email)
                    insertWellnessExpert(member_email, member_type, member_info, template_file, __composer_config, header)
                    logging.info("Added Wellness Member to Wellness Expert " + member_email)
                    print("Added wellness Expert "+member_email+": "+ date)
                
        print("======================================================================================================")
        logging.info("======================================================================================================")

    def consumeUserData(self):
        # call module name and message queue object from config file.
        super(ComposerConsumer, self).consumeUserData()
        module = __import__(getAtmanConfigParamValue("MESSAGE_QUEUE_FILE_NAME"))
        message_queue = getattr(module, getAtmanConfigParamValue("MESSAGE_QUEUE_CLASS"))()
        message_queue.connectServer()
        message_queue.createChannel()
        callback = self.callback
        message_queue.consumeData(callback, queue_name_blockchain)


if __name__ == "__main__":
    __composer_consumer = ComposerConsumer()
    __composer_consumer.consumeUserData()
 
