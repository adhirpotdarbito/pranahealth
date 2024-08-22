'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''
from __config import *
import numpy as np

BETA_MEN = np.array([3.25024, #log age
                     0.74711, #log bmi
                     0.57695, #Hypertension
                     0.59741, #Diabetes
                     0.68506, #Smoking
])
BETA_WOMEN = np.array([3.18736, #log age
                     0.72923, #log bmi
                     0.73404, #Hypertension
                     0.78285, #Diabetes
                     0.61608, #Smoking
])

S_MEN = 0.88434
S_WOMEN = 0.94679

CONST_MEN = 15.4710
CONST_WOMEN = 15.1252

CONST_MEN_BALANCER = 0.10
CONST_WOMEN_BALANCER = 0.12

def _calc_frs(X, b, surv, const):
    return 1 - surv** np.exp(X.dot(b) - const)

def frs_bmi(gender, time, age, bmi, htn, dia, smk):
    X = np.array([np.log(age), np.log(bmi), bool(htn), bool(dia), bool(smk)])
    if (gender == 'Male'):
        return _calc_frs(X,BETA_MEN,S_MEN,CONST_MEN)
    else:
        return _calc_frs(X,BETA_WOMEN,S_WOMEN,CONST_WOMEN)

def frs_cvd(gender, time, age, cvd):
    if (gender == 'Male'):

#get heart age by age and sex
def get_heart_age(age, sex):
    if (sex == 'Male'):
        X = BETA_MEN[0]*np.log(age) - CONST_MEN + CONST_MEN_BALANCER
        exp = np.exp(X)
        ln_cvd = np.log(1-cvd)/np.log(S_MEN)
        result = np.exp(((np.log(ln_cvd/exp))*(1/BETA_MEN[1])))
        return np.round(result)
    else:
        X = BETA_WOMEN[0]*np.log(age) - CONST_WOMEN + CONST_WOMEN_BALANCER
        exp = np.exp(X)
        ln_cvd = np.log(1-cvd)/np.log(S_WOMEN)
        result = np.exp(((np.log(ln_cvd/exp))*(1/BETA_WOMEN[1])))
        return np.round(result)

#get heart age by gender and bmi
def get_heart_age_by_gender_bmi(gender, age, bmi):
    '''
    gender : gender
    age : age
    bmi : bmi
    '''
    if (gender == 'Male'):
        X = BETA_MEN[0]*np.log(age) + BETA_MEN[1]*np.log(bmi) - CONST_MEN + CONST_MEN_BALANCER
        exp = np.exp(X)
        ln_cvd = np.log(1-cvd)/np.log(S_MEN)
        result = np.exp(((np.log(ln_cvd/exp))*(1/BETA_MEN[2])))
        return np.round(result)
    else:
        X = BETA_WOMEN[0]*np.log(age) + BETA_WOMEN[1]*np.log(bmi) - CONST_WOMEN + CONST_WOMEN_BALANCER
        exp = np.exp(X)
        ln_cvd = np.log(1-cvd)/np.log(S_WOMEN)
        result = np.exp(((np.log(ln_cvd/exp))*(1/BETA_WOMEN[2])))
        return np.round(result)

def heart_age_by_cvd_bmi(cvd,age,sex):
    '''
    cvd : cvd value
    age : age
    sex : sex
    '''
    #handle the condition wheere cvd is None
    if cvd is None:
        return 0
    if str(cvd) == n_a:
        return 0
    else:
        cvd = float(cvd)
    if (sex == 'Male'):
        X = BETA_MEN[1]*np.log(22) - CONST_MEN + CONST_MEN_BALANCER
        exp = np.exp(X)
        ln_cvd = np.log(1-cvd)/np.log(S_MEN)
        result = np.exp(((np.log(ln_cvd/exp))*(1/BETA_MEN[0])))
        return np.round(result)
    else
        X = BETA_WOMEN[1]*np.log(22) - CONST_WOMEN + CONST_WOMEN_BALANCER
        exp = np.exp(X)
        ln_cvd = np.log(1-cvd)/np.log(S_WOMEN)
        result = np.exp(((np.log(ln_cvd/exp))*(1/BETA_WOMEN[0])))
        return np.round(result)

#cvd = frs('Male',10,33,26.3,0,0,1)
#print heart_age_by_cvd(cvd,32,'Male')
