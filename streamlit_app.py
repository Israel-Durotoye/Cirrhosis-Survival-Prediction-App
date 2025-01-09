import streamlit as st
import pandas as pd
import joblib

# Load the trained model pipeline
model = joblib.load('Cirrhosis_Patient_Survival_Model.pkl')

# Streamlit app
st.title('Cirrhosis Patient Survival Prediction')

st.sidebar.header('Patient Data')
def user_input_features():
    Drug = st.sidebar.selectbox('Drug', ['D-penicillamine', 'Placebo'])
    Sex = st.sidebar.selectbox('Sex', ['M', 'F'])
    Ascites = st.sidebar.selectbox('Ascites', ['N', 'Y'])
    Hepatomegaly = st.sidebar.selectbox('Hepatomegaly', ['N', 'Y'])
    Spiders = st.sidebar.selectbox('Spiders', ['N', 'Y'])
    Edema = st.sidebar.selectbox('Edema', ['N', 'S', 'Y'])
    Bilirubin = st.sidebar.slider('Bilirubin', 0.0, 50.0, 1.0)
    Cholesterol = st.sidebar.slider('Cholesterol', 0.0, 1000.0, 200.0)
    Albumin = st.sidebar.slider('Albumin', 0.0, 5.0, 3.0)
    Copper = st.sidebar.slider('Copper', 0.0, 500.0, 100.0)
    Prothrombin = st.sidebar.slider('Prothrombin', 0.0, 20.0, 10.0)
    Age = st.sidebar.slider('Age', 0, 100000, 20000)
    Alk_Phos = st.sidebar.slider('Alk_Phos', 0.0, 5000.0, 1000.0)
    SGOT = st.sidebar.slider('SGOT', 0.0, 500.0, 100.0)
    Tryglicerides = st.sidebar.slider('Tryglicerides', 0.0, 500.0, 100.0)
    Platelets = st.sidebar.slider('Platelets', 0.0, 1000.0, 200.0)
    N_Days = st.sidebar.slider('N_Days', 0, 5000, 1000)
    Stage = st.sidebar.slider('Stage', 1.0, 4.0, 1.0)
    
    data = {'Drug': Drug,
            'Sex': Sex,
            'Ascites': Ascites,
            'Hepatomegaly': Hepatomegaly,
            'Spiders': Spiders,
            'Edema': Edema,
            'Bilirubin': Bilirubin,
            'Cholesterol': Cholesterol,
            'Albumin': Albumin,
            'Copper': Copper,
            'Prothrombin': Prothrombin,
            'Age': Age,
            'Alk_Phos': Alk_Phos,
            'SGOT': SGOT,
            'Tryglicerides': Tryglicerides,
            'Platelets': Platelets,
            'N_Days': N_Days,
            'Stage': Stage}
    features = pd.DataFrame(data, index=[0])
    return features

# Collect user input
input_data = user_input_features()

# Display user input
st.subheader('Patient Data')
st.write(input_data)

# Predict the survival status
prediction = model.predict(input_data)

# Map the prediction to its corresponding label
status = {0: 'Death', 1: 'Censored', 2: 'Censored due to liver transplantation'}

# Display the prediction result
st.subheader('Prediction')
st.write(f"Predicted Outcome: **{status[prediction[0]]}**")
