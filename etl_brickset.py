# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:14:03 2015

@author: michael
"""

import pandas as pd
sets = pd.read_csv("~/Data/brickset/starwars.sets.csv")
parts = pd.read_csv("~/Data/brickset/starwars.parts.csv")

#Create SetNumber : Number+'-'+Variant
sets['SetNumber'] = sets.Number.map(str) + '-' + sets.Variant.map(str)

#Save the csv files
sets.to_csv("sets.csv",index_label="id")
parts.to_csv("parts.csv", index_label="id")



