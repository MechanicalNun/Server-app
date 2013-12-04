import pandas as pd
import numpy as np
from collections import defaultdict, Counter

def add_records_to_json():
    data = pd.read_csv('sins.csv', sep=',')
    df = pd.DataFrame(data)

    sin2subsin = {
                      "Q1_1": ["Q2", 40, "Q11"],
                      "Q1_2": ["Q3", 20, "Q12"],
                      "Q1_3": ["Q7", 25, "Q13"],
                      "Q1_4": ["Q8", 20, "Q14"],
                      "Q1_5": ["Q9", 16, "Q15"],
                      "Q1_6": ["Q10", 16, "Q16"],
                      "Q1_7": ["Q17", 28, "Q18"],
                    }  
    Q2sin = {
                "Q1_1": "wrath",
                "Q1_2": "sloth",
                "Q1_3": "lust",
                "Q1_4": "Gluttony",
                "Q1_5": "envy",
                "Q1_6": "greed",
                "Q1_7": "pride",
                }                 

    poll = []
    for cnt in range(len(df)):
        print cnt
        if cnt >1:
            sins = [l for l in  ["Q1_%d"%l for l in range(1,8)] if not isNaN(df.ix[cnt][l])]
            
            for sin in sins:
                subsins = [df[l][cnt] for l in ["%s_%d"%(sin2subsin[sin][0],d) for d in range(1,sin2subsin[sin][1])] if not isNaN(df[l][cnt])]
                if not isNaN(df[sin2subsin[sin][2]][cnt]):
                    subsins.append(df[sin2subsin[sin][2]][cnt]) 
                
                for subsin in subsins:
                    record = {
                        "age": df.ix[cnt]['Q5'],
                        "sex": df.ix[cnt]['Q4'],
                        "times_committed": 1,
                        "commit_again": None,
                        "sin":Q2sin[sin],
                        "sub_sin":subsin,
                        "lat": None,
                        "lon": None, 
                        'neighborhood': df.ix[cnt]['Q21'],
                        'timestamp' : df.ix[cnt]['V8']
                        }

                    poll.append(record)    
    return poll        


def isNaN(num):
    return num != num

# make a table of sins per neighborhood:
def summarise_poll():
    poll = add_records_to_json()

    sin_hoods = {}
    sin_sex = {}
    sin_age = {}

    # Count all unique sins hoods sex and age groups: 
    sins_uniq = Counter([i['sin'] for i in poll])
    hoods_uniq = Counter([i['neighborhood'] for i in poll])
    # sex_uniq = Counter([i['sex'] for i in poll])
    sex_uniq =['Male', "Female"]
    age_uniq = Counter([i['age'] for i in poll])

        # create a default dict for sins and attach to each neighborhood: 
    for hood in hoods_uniq:
        sin_hoods[hood] = dict((sin,0) for sin in sins_uniq.keys())

    for sex in sex_uniq:
        sin_sex[sex] = dict((sin,0) for sin in sins_uniq.keys())    

    for age in age_uniq:
        sin_age[age] = dict((sin,0) for sin in sins_uniq.keys())        

        # Populate the nested dictionary:
    for record in poll:
        Sin = record['sin']
        Hood = record['neighborhood']
        Sex = record['sex']
        Age = record['age']
        sin_hoods[Hood][Sin]+=1 
        sin_sex[Sex][Sin]+=1 
        sin_age[Age][Sin]+=1 

    # make it a table using a DataFrame: 
    sins_hood_table = pd.DataFrame(sin_hoods)
    sins_sex_table = pd.DataFrame(sin_sex)    
    sins_age_table = pd.DataFrame(sin_age)
    
    return sins_hood_table, sins_sex_table, sins_age_table        

def get_greed():
    sins_hood, sins_sex, sins_age = summarise_poll()
    greed = sins_hood.T['greed']
    new_vals = sins_hood.T['greed'].values/float(sins_hood.T['greed'].max())
    temp = dict((greed.keys()[l], new_vals[l]) for l in range(len(greed)))
    template = {"fillOpacity": 0.1, "fillColor": '#4cb8dc', "strokeColor": '#009ACD', "strokeOpacity": 1, "strokeWeight": 1,}
    live = {}

    for k,v in temp.iteritems():
        live[k] = dict(template)
        live[k]['fillOpacity'] = v
        if float(v) > 0:
            live[k]['strokeWeight'] = 2

    return live    





