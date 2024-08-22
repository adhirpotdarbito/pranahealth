# -*- coding: utf-8 -*-
import sys
import json
import codecs
from googletrans import Translator
from io import BytesIO
from reportlab.pdfgen import canvas
from nested_lookup import get_all_keys, nested_lookup
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter,A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from ast import literal_eval

class LanguageTranslate(object):
    def __init__(self):
        with open("/opt/atman/bin/__prescription.json") as f:
            self.dest = ""
            self.json_file = json.load(f)
            self.json_file_pod = self.json_file.get("principles_of_diet")
            self.json_file_meal = self.json_file.get("meal_plans")
            self.json_file_guide = self.json_file.get("guidelines")
            self.translated_json = {}

    def translateText(self, language):
        keys_pod = get_all_keys(self.json_file_pod)
        keys_meal = get_all_keys(self.json_file_meal)
        keys_guideline = get_all_keys(self.json_file_guide)
        #print(nested_lookup('planType', self.json_file_meal, with_keys=True))
        translator = Translator()
        if language == 'Marathi':
            self.dest = 'mr'
        elif language == 'Gujrati':
            self.dest = 'gu'
        else:
            self.dest = 'hi'
        json_string_pod = json.dumps(self.json_file_pod)
        #nutrients = self.json_file_pod.get("nutrients")
        #energy = nutrients.get("energy")
        #protein = nutrients.get("protein")
        json_string_mode = self.json_file_meal.get("meal_plan_mode")
        json_string_meal = self.json_file_meal.get("meal_types")
        meal_type_list = []
        #styles = getSampleStyleSheet()
        #styles.add(ParagraphStyle(name="TableHeader",alignment='center',))
        meal_type_table = [('Meal Plan', 'Meal Time', 'Details',)]
        for meal_dict in json_string_meal:
            meal_type_dict = {}
            food_prescription = meal_dict.get("foodPrescription")
            meal_type_translate = translator.translate(unicode(str(food_prescription),errors='ignore'), src='en', dest=self.dest).text
            meal_type_list.append(meal_type_translate)

        for meal_types in meal_type_list[1:]:
            meal_types = {x.replace(' ', ''): unicode(json.dumps(v)).encode('utf-8').decode('unicode-escape') for x, v in eval(meal_types).items()}
            print meal_types
            #plan_type = json.dumps(eval(meal_types).get("meal_type"))
            #meal_comment = json.dumps(eval(meal_types).get("meal_comments"))
            plan_type = meal_types.get("meal_type")
            meal_comment = meal_types.get("meal_comments")
            meal_time = meal_types.get("meal_time").replace(": 0", ":00")
            print meal_type_table
            meal_type_table.append((plan_type, meal_time, meal_comment,))
        #json.dumps(meal_type_list).encode('utf-8').decode("unicode-escape")
        json_string_guide = json.dumps(self.json_file_guide)
        _json_string_pod = unicode(json_string_pod, errors='replace')
        _json_string_guide = unicode(json_string_guide, errors='replace')
        __principal_of_diet = translator.translate(_json_string_pod, src='en', dest=self.dest).text
        __guidelines = translator.translate(_json_string_guide, src='en', dest=self.dest).text
        #self.translated_json["principles_of_diet"] = self.json_file.get("principles_of_diet")
        #self.translated_json["guidelines"] = __guidelines
        #meal_plans = {"meal_types": meal_type_list}
        #self.translated_json["meal_plans"] = meal_plans
        #self.translated_json["meal_plans"]["meal_plan_mode"] = json_string_mode
        with codecs.open("__prescription_translated.txt", "w") as outfile:
            _translated = unicode(json.dumps(self.translated_json)).encode('utf-8')
            _translated_text = _translated.decode('unicode-escape')
            pdfmetrics.registerFont(TTFont('gargi', '/home/isana/Downloads/gargi.ttf'))
            c = canvas.Canvas("test.pdf", pagesize=letter)
            c.setFont("gargi", 8)
            s = meal_type_table[0][0]
            c.drawString(500,300, _translated_text)
            #json.dump(_translated_text, outfile)
            #outfile.write(str(_translated_text.encode('utf-8')))
            #f = BytesIO()
            #textobj = c.beginText()
            #textobj.setTextOrigin(2.54, 20 * 2.54)
            #c.drawCentredString(415, 500, str(_translated_text.encode('utf-8')))
            #c = canvas.Canvas("/opt/atman/bin/sample.pdf")
            #c.setFont('Times-Bold',16)
            #c.drawCentredString(800, 800, "Principle Of Diet")
            #c.showPage()
            #c.save()
            doc = SimpleDocTemplate("test.pdf", pagesize=A4)
            t=Table(meal_type_table)
            t.setStyle(TableStyle([('ALIGN', (1,1), (-1,-1), 'CENTER'),('GRID',(0,0),(-1,-1),0.25,colors.black), ('FONTNAME', (0,0), (-1,-1), 'gargi'), ('TEXTCOLOR',(0,0),(2,0), colors.green),('ALIGN', (0,1), (0,-1), 'RIGHT'), ('ALIGN', (0,0), (2,0), 'CENTER')]))
            elements = []
            elements.append(t)
            doc.build(elements) 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("python __language_translate.py <language>")
    else:
        language = sys.argv[1]
        language_translate = LanguageTranslate() 
        translated_text = language_translate.translateText(language)

