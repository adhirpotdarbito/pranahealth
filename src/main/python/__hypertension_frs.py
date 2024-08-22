
'''
   
    Copyright (C) 2018-2019 AtmanCare India Private Limited
    
    This source code is owned and maintained by AtmanCare India Private Limited
    and not allowed to be used or to be distributed without prior written
    permission of AtmanCare India Private Limited.
   
'''

# import required libraries
import numpy as np

# define Factors
AGE = -0.15641
SEX = -0.20293
SBP = -0.05933
DBP = -0.12847
SMOKING = -0.19073
PARENTAL_HTN = -0.16612
BMI = -0.03388
AGE_DBP = 0.00162
CONST = 22.94954


def calc_risk_hypertension(year,age,sex,sbp,dbp,smk,parental_htn,bmi):
    """
        Function to calculate hypertension risk from user inputs parameters year,age,sex,sbp,dbp,smk,parental_htn,bmi
    """
    X = 0
    # in case of women we take sex 1 for men 0 in our calculation
    if (sex == 'Female'):
        X = AGE*age + SEX + SBP*sbp + DBP*dbp + SMOKING*smk + PARENTAL_HTN*parental_htn + BMI*bmi + AGE_DBP*age*dbp
    else:
        X = AGE*age + SBP*sbp + DBP*dbp + SMOKING*smk + PARENTAL_HTN*parental_htn + BMI*bmi + AGE_DBP*age*dbp
    
    inter = ((np.log(year) -(CONST + X))/0.87692)
    result = 1 - np.exp(-np.exp(inter))

    return result

#ret = calc_risk_hypertension(4,60,'Male',110,70,0,0,22)
#print ret

#ret = calc_risk_hypertension(4,60,'Female',110,70,0,0,22)
#print ret

# SBP 110
# DBP 70
# BMI 22
