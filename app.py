import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Number Division

This app divides one number by another
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    input_dividend_first_number = st.number_input("INPUT_DIVIDEND")
    input_divisor_second_number = st.number_input("INPUT_DIVISOR")
    
    data = {'INPUT_DIVIDEND': input_dividend_first_number,
            'INPUT_DIVISOR': input_divisor_second_number,
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

quotient = input_dividend_first_number/input_divisor_second_number
st.subheader('User Input parameters')
st.write(df.to_dict())


st.subheader('Quotient')
st.write(quotient)
