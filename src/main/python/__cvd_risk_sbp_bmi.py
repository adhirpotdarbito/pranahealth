'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

from __config import *
import numpy as np

BETA_MEN_HT = np.array([3.11296, #log age
                        0.79277, #log bmi
                        1.92672, #log sbp treated
                        0.53160, #diabetes
                        0.70953, #smoking
])
BETA_MEN_NON_HT = np.array([3.11296, #log age
                        0.79277, #log bmi
                        1.85508, #log sbp not treated
                        0.53160, #diabetes
                        0.70953, #smoking
])
BETA_WOMEN_HT = np.array([2.72107, # log AGE
                        0.51125, # log bmi
                        2.88267, # log SBP treated
                        0.77763, # Diabetes
                        0.61868, # Smoking
])
BETA_WOMEN_NON_HT = np.array([2.72107, # log AGE
                        0.51125, # log bmi
                        2.81291, # log SBP not treated
                        0.77763, # Diabetes
                        0.61868, # Smoking
])

S_MEN = 0.88431
S_WOMEN = 0.94833

CONST_MEN = 23.9388
CONST_WOMEN = 26.0145

def _calc_frs(X, b, surv, const):
    return 1 - surv** np.exp(X.dot(b) - const)

def frs_sbp_bmi(gender, time, age, bmi, sbp, dia, smk, bp_treated):
    if sbp <= 0:
        return n_a
    X = np.array([np.log(age), np.log(bmi), np.log(sbp), bool(dia), bool(smk)])
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

def heart_age_by_cvd_sbp_bmi(cvd_risk,age,sex):
    X = 0
    if str(cvd_risk) == n_a:
        return 0
    if (sex == 'Male'):
        if (age < 60):
            X = BETA_MEN_NON_HT[1]*np.log(22) + (BETA_MEN_NON_HT[2]*np.log(125)) -CONST_MEN
        else:
            X = BETA_MEN_NON_HT[1]*np.log(22) + (BETA_MEN_NON_HT[2]*np.log(130)) -CONST_MEN
        exp = np.exp(X)
        ln_cvd = np.log(1-cvd_risk)/np.log(S_MEN)
        result = np.exp(((np.log(ln_cvd/exp))*(1/BETA_MEN_NON_HT[0])))
        return np.round(result)

    else:
        if (age < 60):
            X = BETA_WOMEN_NON_HT[1]*np.log(22) + (BETA_WOMEN_NON_HT[2]*np.log(125)) -CONST_WOMEN
        else:
            X = BETA_WOMEN_NON_HT[1]*np.log(22) + (BETA_WOMEN_NON_HT[2]*np.log(130)) -CONST_WOMEN
        exp = np.exp(X)
        ln_cvd = np.log(1-cvd_risk)/np.log(S_WOMEN)
        result = np.exp(((np.log(ln_cvd/exp))*(1/BETA_WOMEN_NON_HT[0])))
        return np.round(result)

#cvd =  frs('Female',10,32,29,139,0,1,0)
#print cvd
#print heart_age_by_cvd(cvd,32,'Female')
