# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 02:01:57 2025

@author: welcome
"""

import json
import requests

#for here the url gping to ml terminal in navigator and type uvicorn ml_api:app

url = '/diabetes_prediction'

input_data_for_model = {
    
    'Pregnancies' : 5,
    'Glucose' : 166,
    'BloodPressure' : 72,
    'SkinThickness' : 19,
    'Insulin' : 175,
    'BMI' : 25.8,
    'DiabetesPedigreeFunction' : 0.587,
    'Age' : 51
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)
print(response.text)