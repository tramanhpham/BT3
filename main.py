import streamlit as st
import pickle as pkl
import numpy as np

class_list = {'0': 'Negative', '1': 'Neutral', '2': 'Positive'}

st.title('Sentiment analysis from Vietnamese students\' feedback')

input_ec = open('ec_vsfc.pkl', 'rb')
encoder = pkl.load(input_ec)

input_md = open('lrc_vsfc.pkl', 'rb')
model = pkl.load(input_md)

st.header('Write a feedback')
txt = st.text_area('', '')
