import numpy as np
import pandas as pd



class MappingData():

    def mapping_AGE(self,x):
        if x in [1,2]:
            return '12-17 years old'
        elif x in [3,4,5]:
            return '18-29 years old'
        elif x in [6,7]:
            return '30-39 years old'
        elif x in [8,9]:
            return '40-49 years old'
        elif x in [10,11]:
            return '50-64 years old'
        elif x in [12]:
            return '65+ years old'
        


    def mapping_GENDER(self,x):
        if x == 1:
            return 'Male'
        elif x == 2:
            return 'Female'


    def mapping_RACE(self,x):
        if x == 1:
            return 'Alaska Native'
        elif x == 2:
            return 'American Indian'
        elif x == 3 or x == 9:
            return 'Hawaii, Pacific Islander'
        elif x == 4:
            return 'Black'
        elif x == 5:
            return 'White'
        elif x == 6:
            return 'Asian'
        elif x == 7:
            return 'Other race'
        elif x == 8:
            return 'Two or more races'
        

    def mapping_ETHNIC(self,x):
        if x in [1,2,3,5]:
            return "Hispanic"
        elif x in [4]:
            return "Not Hispanic"
        



    def mapping_MARSTAT(self,x):
        if x == 1:
            return "Never married"
        elif x == 2:
            return "Now married"
        elif x == 3:
            return "Separated"
        elif x == 4:
            return 'Divorced/widowed'
        

    def mapping_EDUC(self,x):
        if x == 1:
            return "No schooling"
        elif x == 2:
            return "Grades 9-11"
        elif x == 3:
            return "Grade 12"
        elif x == 4:
            return '1-3 years of college'
        elif x ==5:
            return '4 years of college, BA/BS, or more'
        

    def mapping_EMPLOY(self,x):
        if x == 1:
            return 'Full-time'
        elif x == 2:
            return "Part-time"
        elif x == 3:
            return "Unemployed"
        elif x == 4:
            return 'Not in labor force'
        


    def mapping_PREG(self,x):
        if x == 1:
            return 'Pregnant'
        elif x == 2:
            return "Not pregnant"
        

    def mapping_VET(self,x):
        if x == 1:
            return 'Veteran'
        elif x == 2:
            return "Not veteran"
        



    def mapping_LIVARAG(self,x):
        if x == 1:
            return 'Homeless'
        elif x == 2:
            return "Dependent living"
        elif x == 3:
            return "Independent living"
        

    def mapping_PRIMINC(self,x):
        if x == 1:
            return 'Wages/salary'
        elif x == 2:
            return "Public assistance"
        elif x == 3:
            return "Retirement/pension, disability"
        elif x == 4:
            return 'Other'
        elif x == 5:
            return 'None'
        



    def mapping_ARRESTS(self,x):
        if x == 0:
            return 'None'
        elif x == 1:
            return "Once"
        elif x == 2:
            return "Two or more times"
    


    def mapping_DIVISION(self,x):
        if x== 0:
            return 'U.S. territories'
        elif x == 1:
            return 'New England'
        elif x == 2:
            return 'Middle Atlantic'
        elif x == 3:
            return 'East North Central'
        elif x == 4:
            return 'West North Central'
        elif x == 5:
            return 'South Atlantic'
        elif x == 6:
            return 'East South Central'
        elif x == 7:
            return 'West South Central'
        elif x == 8:
            return 'Mountain'
        elif x == 9:
            return 'Pacific'
        


    def mapping_SERVICES(self,x):
        if x in [1,2]:
            return 'Detox'
        elif x in [3,4,5]:
            return 'Rehab/residential'
        elif x in [6,7,8]:
            return 'Ambulatory'
        

    def mapping_DAYWAIT(self,x):
        if x in [0,1,2]:
            return '0-14 days'
        elif x in [3]:
            return '15-30 days'
        elif x in [4]:
            return '31+ days'
        


    def mapping_PSOURCE(self,x):
        if x == 1:
            return 'Individual'
        elif x == 2:
            return 'Alcohol/drug provider'
        elif x == 3:
            return 'Other Health Care provider'
        elif x == 4:
            return 'School'
        elif x == 5:
            return 'Employer'
        elif x == 6:
            return 'Community'
        elif x == 7:
            return 'Court'
        


    def mapping_SUB(self,x):
        if x == 2:
            return 'Alcohol'
        elif x == 3:
            return 'Cocaine/Crack'
        elif x == 4:
            return 'Marijuana/Hashish'
        elif x == 5:
            return 'Heroin'
        elif x == 6 or x == 7:
            return 'Opiates or Methadone'
        elif x == 10:
            return 'Methamphetamine'
        elif x == 11 or x == 12:
            return 'Other Amphetamines or Stimulants'
        elif x == 13 or x == 14:
            return 'Benzodiazepines or Tranquilizers'
        elif x == 8 or x == 9:
            return 'PCP or Other Hallucinogens'
        elif x >= 15 & x <= 20:
            return 'Other'
        

    def mapping_FREQ(self,x):
        if x == 1:
            return 'No use in the past month'
        elif x == 2:
            return 'Some use'
        elif x == 3:
            return 'Daily use'



    def mapping_FRSTUSE(self,x):
        if x == 1:
            return '11 years and under'
        elif x == 2 or x == 3:
            return '12-17 years'
        elif x == 4 or x == 5:
            return '18-24 years'
        elif x == 6:
            return '25-29 years'
        elif x == 7:
            return '30 years and older'
        


    def mapping_PSYPROB(self,x):
        if x == 1:
            return 'Yes'
        elif x == 2:
            return 'No'
        


    def mapping_HLTHINS(self,x):
        if x in [1,2,3]:
            return 'Yes'
        elif x == 4:
            return 'No'
        


    def mapping_FREQ_ATND_SELF_HELP(self,x):
        if x == 1:
            return 'No'
        elif x in [2,3,4,5] :
            return 'Yes'
        


    def mapping_NOPRIOR(self,x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        

    def mapping_NUM_SUBS(self,x):
        if x == 0:
            return 'Zero sub'
        elif x == 1:
            return 'One sub'
        elif x == 2:
            return 'Two sub'
        elif x == 3:
            return 'Three sub'