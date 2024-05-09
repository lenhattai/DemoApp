
import skfuzzy as fuzz
import numpy as np
from skfuzzy import control as ctrl

def calBMI(height, weight ):
    return weight/(height* height)

def handleHealth(bmi, sleep, gym):
    BMI=ctrl.Antecedent(np.arange(16,35,0.1),'BMI')
    GYM=ctrl.Antecedent(np.arange(0,8,0.1),'GYM')
    SLEEP=ctrl.Antecedent(np.arange(0,10,0.1),'SLEEP')
    HEALTH=ctrl.Consequent(np.arange(0,5,0.1),'HEALTH')
    BMI['thin']=fuzz.trimf(BMI.universe,[16,16,18.5])
    BMI['fit']=fuzz.trimf(BMI.universe,[16,18.5,25])
    BMI['Ovw']=fuzz.trimf(BMI.universe,[18.5,25,30])
    BMI['fat']=fuzz.trimf(BMI.universe,[25,35,35])
    GYM['Less']=fuzz.trimf(GYM.universe,[0,0,2])
    GYM['Medium']=fuzz.trimf(GYM.universe,[0,2,4])
    GYM['More']=fuzz.trimf(GYM.universe,[3,7,7])
    SLEEP['Less']=fuzz.trimf(SLEEP.universe,[0,0,6])
    SLEEP['Good']=fuzz.trimf(SLEEP.universe,[0,6,8])
    SLEEP['More']=fuzz.trimf(SLEEP.universe,[7,10,10])
    HEALTH['Weak']=fuzz.trimf(HEALTH.universe,[0,0,2.5])
    HEALTH['Healthy']=fuzz.trimf(HEALTH.universe,[0,2.5,5])
    HEALTH['Good']=fuzz.trimf(HEALTH.universe,[2.5,5,5])
    r1=ctrl.Rule(BMI['thin']& GYM['Less']& SLEEP['Less'],HEALTH['Weak'])
    r2=ctrl.Rule(BMI['thin']& GYM['Less']& SLEEP['Good'],HEALTH['Healthy'])
    r3=ctrl.Rule(BMI['thin']& GYM['Less']& SLEEP['More'],HEALTH['Weak'])
    r4=ctrl.Rule(BMI['thin']& GYM['Medium']& SLEEP['Less'],HEALTH['Weak'])
    r5=ctrl.Rule(BMI['thin']& GYM['Medium']& SLEEP['Good'],HEALTH['Healthy'])
    r6=ctrl.Rule(BMI['thin']& GYM['Medium']& SLEEP['More'],HEALTH['Healthy'])
    r7=ctrl.Rule(BMI['thin']& GYM['More']& SLEEP['Less'],HEALTH['Weak'])
    r8=ctrl.Rule(BMI['thin']& GYM['More']& SLEEP['Good'],HEALTH['Good'])
    r9=ctrl.Rule(BMI['thin']& GYM['More']& SLEEP['More'],HEALTH['Healthy'])
    r10=ctrl.Rule(BMI['fit']& GYM['Less']& SLEEP['Less'],HEALTH['Weak'])
    r11=ctrl.Rule(BMI['fit']& GYM['Less']& SLEEP['Good'],HEALTH['Weak'])
    r12=ctrl.Rule(BMI['fit']& GYM['Less']& SLEEP['More'],HEALTH['Weak'])
    r13=ctrl.Rule(BMI['fit']& GYM['Medium']& SLEEP['Less'],HEALTH['Weak'])
    r14=ctrl.Rule(BMI['fit']& GYM['Medium']& SLEEP['Good'],HEALTH['Good'])
    r15=ctrl.Rule(BMI['fit']& GYM['Medium']& SLEEP['More'],HEALTH['Healthy'])
    r16=ctrl.Rule(BMI['fit']& GYM['More']& SLEEP['Less'],HEALTH['Weak'])
    r17=ctrl.Rule(BMI['fit']& GYM['More']& SLEEP['Good'],HEALTH['Good'])
    r18=ctrl.Rule(BMI['fit']& GYM['More']& SLEEP['More'],HEALTH['Healthy'])
    r19=ctrl.Rule(BMI['Ovw']& GYM['Less']& SLEEP['Less'],HEALTH['Weak'])
    r20=ctrl.Rule(BMI['Ovw']& GYM['Less']& SLEEP['Good'],HEALTH['Healthy'])
    r21=ctrl.Rule(BMI['Ovw']& GYM['Less']& SLEEP['More'],HEALTH['Weak'])
    r22=ctrl.Rule(BMI['Ovw']& GYM['Medium']& SLEEP['Less'],HEALTH['Weak'])
    r23=ctrl.Rule(BMI['Ovw']& GYM['Medium']& SLEEP['Good'],HEALTH['Healthy'])
    r24=ctrl.Rule(BMI['Ovw']& GYM['Medium']& SLEEP['More'],HEALTH['Healthy'])
    r25=ctrl.Rule(BMI['Ovw']& GYM['More']& SLEEP['Less'],HEALTH['Weak'])
    r26=ctrl.Rule(BMI['Ovw']& GYM['More']& SLEEP['Good'],HEALTH['Good'])
    r27=ctrl.Rule(BMI['Ovw']& GYM['More']& SLEEP['More'],HEALTH['Healthy'])
    r28=ctrl.Rule(BMI['fat']& GYM['Less']& SLEEP['Less'],HEALTH['Weak'])
    r29=ctrl.Rule(BMI['fat']& GYM['Less']& SLEEP['Good'],HEALTH['Healthy'])
    r30=ctrl.Rule(BMI['fat']& GYM['Less']& SLEEP['More'],HEALTH['Weak'])
    r31=ctrl.Rule(BMI['fat']& GYM['Medium']& SLEEP['Less'],HEALTH['Weak'])
    r32=ctrl.Rule(BMI['fat']& GYM['Medium']& SLEEP['Good'],HEALTH['Healthy'])
    r33=ctrl.Rule(BMI['fat']& GYM['Medium']& SLEEP['More'],HEALTH['Healthy'])
    r34=ctrl.Rule(BMI['fat']& GYM['More']& SLEEP['Less'],HEALTH['Weak'])
    r35=ctrl.Rule(BMI['fat']& GYM['More']& SLEEP['Good'],HEALTH['Good'])
    r36=ctrl.Rule(BMI['fat']& GYM['More']& SLEEP['More'],HEALTH['Healthy'])
    HEALTH_ctrl=ctrl.ControlSystem([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,r29,r30,r31,r32,r33,r34,r35,r36])

    HEALTHING=ctrl.ControlSystemSimulation(HEALTH_ctrl)

    HEALTHING.input['BMI']=bmi
    HEALTHING.input['SLEEP']=sleep
    HEALTHING.input['GYM']=gym
    HEALTHING.compute()
    res =  HEALTHING.output['HEALTH']
    print(res)
    return res

handleHealth(18,7,6)



    











