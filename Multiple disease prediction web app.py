"""
created on : 18:52:23 Wed 21 Feb 2024
@author : Arpit Patel
"""


import streamlit as st
from streamlit_option_menu import option_menu 
import numpy as np 
import pickle 
import time

diabetes_model=pickle.load(open("trained_diabetes_model.sav",'rb'))
heart_disease_model=pickle.load(open("trained_heat_disease_model.sav",'rb'))

def diabetes_prediction(input_data):
    input_data_as_nparr=np.asarray(input_data)
    reshaped_input_data=input_data_as_nparr.reshape(1,-1)
    prediction=diabetes_model.predict(reshaped_input_data)
    return prediction[0]

def heart_diseaase_prediction(input_data):
    input_data_as_nparr=np.asarray(input_data)
    reshaped_input_data=input_data_as_nparr.reshape(1,-1)
    prediction=heart_disease_model.predict(reshaped_input_data)
    return prediction[0]  


with st.sidebar:
    selected=option_menu("Multiple Disease prediction Using Machine Learning",['Diabetes Prediction','Heart Disease prediction'],icons=['heart','activity'],default_index=0)

if selected is 'Diabetes Prediction':
    st.title("Diabetes Prediction web App")
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnencies")
    with col2:
        Glucose = st.text_input("Glucose level")
    with col3:
        BloodPressure = st.text_input("Blood-pressure")
    with col1:
        SkinThickness = st.text_input("skin Thickness")
    with col2:
        Insulin= st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI (Body-Mass-Index)")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    with col2:
        Age = st.text_input("What is Your age ?")
    submitted=st.button("Check Result")
    if(submitted):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        result=diabetes_prediction(user_input)
        with st.spinner("Wait for it....."):
            time.sleep(2)
        if (result==1):
            st.info('The person is Diabetic!!!')
        else:
            st.info('The person is not Diabetic.')

else:
    st.title("Heart Disease prediction web App")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Enter your Age")
    with col2:
        sex = st.text_input("Gender")
    with col3:
        cp = st.text_input("Chest Pain types")
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    submitted=st.button("Check Result")
    if(submitted):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        result=heart_diseaase_prediction(user_input)
        with st.spinner("Wait for it....."):
            time.sleep(2)
        if (result==1):
            st.info('The person has Heart-Disease!!!')
        else:
            st.info("The person doesn't have Diabetic.")
    
    
    
