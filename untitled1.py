# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 23:12:43 2020

@author: Onur
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/Onur/Desktop/salary_project/chromedriver"
df = gs.get_jobs('data scientist',15,False,path,15)

