import json
import sys
import os
import ghostscript 
import re
import codecs
import nltk
import PyPDF2
from __db_config import *

class ReportParser():

    def __init__(self, file_name, password):
        try:
            self.output = os.path.splitext(os.path.basename(file_name))[0] + ".txt"
            if file_name.endswith("pdf"):
                if PyPDF2.PdfFileReader(file_name, strict=False).isEncrypted:
                    args = ["gs", "-q", "-sstdout=gs.log", "-dBatch", "-sDEVICE=txtwrite", "-dNOPAUSE", "-sPDFPassword="+password,  "-sOutputFile="+self.output, "-f", file_name]
                else:  
                    args = ["gs", "-q", "-sstdout=gs.log", "-dBatch", "-sDEVICE=txtwrite", "-dNOPAUSE", "-sOutputFile="+self.output, "-f", file_name]
                ghostscript.Ghostscript(*args)
                with codecs.open(self.output, 'rb', encoding='ascii', errors='ignore') as f:
                    self.report = f.readlines()
            else:
                self.report = []
            self.medical_report = {}
            self.parse_keys = []    
            self.key_tuple = ()
            self.key_list = []
            self.clean_text = []               
                       
        except Exception as err:
            print json.dumps({"parsing_failed" : "summary cannot be generated"}) 

    def cleanText(self, text):
        text = text.lower()
        text = text.replace(",", "")
        #print('oringial text:' , text)
        strip_unicode = re.compile("([^-_a-zA-Z0-9!@#%&=,/'\";:~`\$\^\*\(\)\+\[\]\.\{\}\|\?\<\>\\]+|[^\s]+)")
        text_updated = strip_unicode.sub('0', text)
        if text != text_updated:
            text = ""
        #print('post cleaning text:' , text)
        return text

    def reportList(self):
        for keys in range(len(self.report)):
            self.parse_keys.append(" ".join(self.report[keys].split()))
        for text in self.parse_keys:
            self.clean_text.append(self.cleanText(text))
	for key in range(len(self.clean_text)):
            #self.key_tuple += ((self.parse_keys[key],))
            self.key_list.append((self.clean_text[key].lower(),))
        return self.key_list


    def parseMedicalParameter(self, med_annot, parameter_name):
        annot = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        if parameter_name in ["apolipoprotein_a1", "hemoglobin a1c", "vitamin b12", "vitamin d"]:
            try:
                for i in range(len(self.key_list)):
                    if annot.search(str(self.key_list[i])) and re.search(r'[2-9]\d*',str(self.key_list[i])):
                        hba1c = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                        self.medical_report[parameter_name] = float(hba1c[1])
                        break
                    else:
                        self.medical_report[parameter_name] = None
                return 0

            except Exception as err:
                self.medical_report[parameter_name] = None
                return -1

        else:
            try:
                for i in range(len(self.key_list)):
                    if annot.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                        param = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                        self.medical_report[parameter_name] = float(param[0])
                        break
                    else:
                        self.medical_report[parameter_name] = None
                return 0

            except Exception as err:
                self.medical_report[parameter_name] = None
                return -1


    
    def parseBloodUreaNitrogen(self, med_annot):
        annot_urea = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_urea.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    urea = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["blood_urea"] = float(urea[0])
                    break
                else:
                    self.medical_report["blood_urea"] = None
            return 0 

        except Exception as err:
            self.medical_report["blood_urea"] = None

    def parseCreatinine(self, med_annot):
        annot_creat = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_creat.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    creat = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["creatinine"] = float(creat[0])
                    break
                else:
                    self.medical_report["creatinine"] = None
            return 0 

        except Exception as err:
            self.medical_report["creatinine"] = None
            return -1
    
    def parseUricAcid(self, med_annot):
        annot_uric = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_uric.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    uric = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["uric_acid"] = float(uric[0])
                    break
                else:
                    self.medical_report["uric_acid"] = None
            return 0 

        except Exception as err:
            self.medical_report["uric_acid"] = None
            return -1
    
    def parseAlbumin(self, med_annot):
        annot_album = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_album.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    album = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["albumin"] = float(album[0])
                    break
                else:
                    self.medical_report["albumin"] = None
            return 0 

        except Exception as err:
            self.medical_report["albumin"] = None
            return -1

    def parseGlobulin(self, med_annot):
        annot_glob = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_glob.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    glob = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["globulin"] = float(glob[0])
                    break
                else:
                    self.medical_report["globulin"] = None
            return 0 

        except Exception as err:
            self.medical_report["globulin"] = None
            return -1
    
    def parseBunCreatRatio(self, med_annot):
        annot_bun_creat = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_bun_creat.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    bun_creat = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["bun_creat_ratio"] = float(bun_creat[0])
                    break
                else:
                    self.medical_report["bun_creat_ratio"] = None
            return 0 

        except Exception as err:
            self.medical_report["bun_creat_ratio"] = None
            return -1
        
    def parseTotalProtein(self, med_annot):
        annot_tot_prot = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_tot_prot.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    tot_prot = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["total_protein"] = float(tot_prot[0])
                    break
                else:
                    self.medical_report["total_protein"] = None
            return 0 

        except Exception as err:
            self.medical_report["total_protein"] = None
            return -1

    def parseBilirubinTotal(self, med_annot):
        annot_bilr = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_bilr.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    bilr = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["bilirubin_total"] = float(bilr[0])
                    break
                else:
                    self.medical_report["bilirubin_total"] = None
            return 0 

        except Exception as err:
            self.medical_report["bilirubin_total"] = None
            return -1

    def parseBilirubinDirect(self, med_annot):
        annot_bilr_dir = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_bilr_dir.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    bilr_dir = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["bilirubin_direct"] = float(bilr_dir[0])
                    break
                else:
                    self.medical_report["bilirubin_direct"] = None
            return 0 

        except Exception as err:
            self.medical_report["bilirubin_direct"] = None
            return -1

    def parseBilirubinIndirect(self, med_annot):
        annot_bilr_indir = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_bilr_indir.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    bilr_indir = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["bilirubin_indirect"] = float(bilr_indir[0])
                    break
                else:
                    self.medical_report["bilirubin_indirect"] = None
            return 0 

        except Exception as err:
            self.medical_report["bilirubin_indirect"] = None
            return -1

    def parseAlbumGlobRatio(self, med_annot):
        annot_alb_glob = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_alb_glob.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    ratio = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["albumin_globulin_ratio"] = float(ratio[0])
                    break
                else:
                    self.medical_report["albumin_globulin_ratio"] = None
            return 0 

        except Exception as err:
            self.medical_report["albumin_globulin_ratio"] = None
            return -1

    def parseAspartateAminotransferase(self, med_annot):
        annot_ast = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_ast.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    ast = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["aspartate_aminotransferase"] = float(ast[0])
                    break
                else:
                    self.medical_report["aspartate_aminotransferase"] = None
            return 0 

        except Exception as err:
            self.medical_report["aspartate_aminotransferase"] = None
            return -1

    def parseGammaGlutamylTrans(self, med_annot):
        annot_ggt = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_ggt.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    ggt = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["gamma_glutamyl_transferase"] = float(ggt[0])
                    break
                else:
                    self.medical_report["gamma_glutamyl_transferase"] = None
            return 0 

        except Exception as err:
            self.medical_report["gamma_glutamyl_transferase"] = None
            return -1

    def parseAlkalinePhosphatase(self, med_annot):
        annot_alkaline = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_alkaline.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    alkaline = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["alkaline_phosphatase"] = float(alkaline[0])
                    break
                else:
                    self.medical_report["alkaline_phosphatase"] = None
            return 0 

        except Exception as err:
            self.medical_report["alkaline_phosphatase"] = None
            return -1

    def parseAlanineTransaminase(self, med_annot):
        annot_sgpt = re.compile(r'(?:{})'.format('|'.join(map(re.escape, med_annot))))
        try:
            for i in range(len(self.key_list)):
                if annot_sgpt.search(str(self.key_list[i])) and re.search(r'\d', str(self.key_list[i])):
                    sgpt = re.findall(r'[-+]?([0-9]*\.[0-9]+|[0-9]+)', str(self.key_list[i]))
                    self.medical_report["alanine_transaminase"] = float(sgpt[0])
                    break
                else:
                    self.medical_report["alanine_transaminase"] = None
            return 0 

        except Exception as err:
            self.medical_report["alanine_transaminase"] = None
            return -1



    def getMedicalParsedData(self):
       return self.medical_report 

