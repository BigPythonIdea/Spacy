# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 21:45:30 2021

@author: Mooncat
"""

import pandas as pd
import sys
import os



merged = "<Your Path>"
merge = "<Your merged path>"
new_path = "<Your new store path>"

p = "<Folder name>"
name = "<stock name>"



def move(col):
    dt = list(pdf[col])
    dt.insert( 0, "nan")
    return dt
    
    
try:
    df = pd.read_csv(merged+"\\"+name+".CSV",index_col=0)
except:
    with open(new_path+"\\error.csv",'a+') as f:
        f.write(p+" "+name+"\n")
    print("Code -1")
    sys.exit()
    
    
try:
    del df["Spacy_Similar_score"]
except:
    pass

no = df["Similar_score"] == -2

for i in no:
    if i == True:
        with open(new_path+"\\error2.csv",'a+') as f:
            f.write(p+" "+name+"\n")
        print("This stock have -2")
        sys.exit()
       
pdf = pd.read_csv(merge+"\\"+name+"_sp.CSV",index_col=0)
ds = move("0")

df["Similar_score"] = pd.DataFrame(ds)

df.to_csv("<store path>",index=False)


print("code 0")


