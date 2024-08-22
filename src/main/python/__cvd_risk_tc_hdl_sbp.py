'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''
from __config import *
import numpy as np

BETA_MEN_HT = np.array([3.06117, # log AGE
                        1.12370, # log TOT
                        -0.93263, # log HDL
                        1.99881, # log SBP
                        0.57367, # Diabetes
                        0.65451, # Smoking
])

BETA_MEN_NON_HT = np.array([3.06117, # log AGE
                        1.12370, # log TOT
                        -0.93263, # log HDL
                        1.93303, # log SBP
                        0.57367, # Diabetes
                        0.65451, # Smoking
])
BETA_WOMEN_HT = np.array([2.32888, # log AGE
                        1.20904, # log TOT
                        -0.70833, # log HDL
                        2.82263, # log SBP
                        0.69154, # Diabetes
                        0.52873, # Smoking
])
BETA_WOMEN_NON_HT = np.array([2.32888, # log AGE
                        1.20904, # log TOT
                        -0.70833, # log HDL
                        2.76157, # log SBP
                        0.69154, # Diabetes
                        0.52873, # Smoking
])

S_MEN = 0.88936
S_WOMEN = 0.95012

CONST_MEN = 23.9802
CONST_WOMEN = 26.1931

def _calc_frs(X, b, surv, const):
    return 1 - surv** np.exp(X.dot(b) - const)

def frs_tc_hdl_sbp(gender, time, age, tot, hdl, sbp, dia, smk, bp_treated):
    if tot <= 0.0 or hdl <= 0.0 or sbp <= 0:
        return n_a
    X = np.array([np.log(age), np.log(tot), np.log(hdl), np.log(sbp), bool(dia), bool(smk)])
    if (gender == 'Male'):
        if (bp_treated):
            return _calc_frs(X,BETA_MEN_HT,S_MEN,CONST_MEN)
        else:
            return _calc_frs(X,BETA_MEN_NON_HT,S_MEN,CONST_MEN)

    else:
        if (bp_treated):
            return _calc_frs(X,BETA_WOMEN_HT,S_WOMEN,CONST_WOMEN)
        else:
            return _calc_frs(X,BETA_WOMEN_NON_HT,S_WOMEN,CONST_WOMEN)




def heart_age_by_cvd_tc_hdl_sbp(cvd_risk,age,sex):
    X = 0
    if str(cvd_risk) == n_a:
        return 0
    if (sex == 'Male'):
        if (age < 60):
            X = BETA_MEN_NON_HT[1]*np.log(180) + (BETA_MEN_NON_HT[2]*np.log(45)) + BETA_MEN_NON_HT[3]*np.log(125) -CONST_MEN
        else:
            X = BETA_MEN_NON_HT[1]*np.log(180) + (BETA_MEN_NON_HT[2]*np.log(45)) + BETA_MEN_NON_HT[3]*np.log(130) -CONST_MEN
        exp = np.exp(X)
        ln_cvd = np.log(1-cvd_risk)/np.log(S_MEN)
        result = np.exp(((np.log(ln_cvd/exp))*(1/BETA_MEN_NON_HT[0])))
        return np.round(result)

    else:
        if (age < 60):
            X = BETA_WOMEN_NON_HT[1]*np.log(180) + (BETA_WOMEN_NON_HT[2]*np.log(45)) + BETA_WOMEN_NON_HT[3]*np.log(125) -CONST_WOMEN
        else:
            X = BETA_WOMEN_NON_HT[1]*np.log(180) + (BETA_WOMEN_NON_HT[2]*np.log(45)) + BETA_WOMEN_NON_HT[3]*np.log(130) -CONST_WOMEN
        exp = np.exp(X)
        ln_cvd = np.log(1-cvd_risk)/np.log(S_WOMEN)
        result = np.exp(((np.log(ln_cvd/exp))*(1/BETA_WOMEN_NON_HT[0])))
        return np.round(result)


#cvd = frs('Male',10,32,300,30,139,0,1,0)
#print heart_age_by_cvd(cvd,32,'Male')


# Female/Male Normal
# SBP 125
# HDL 45
# TC 180
# BMI 22.5

# Female/Male Optimal
# SBP 110
# HDL 60
# TC 160
# BMI 22
