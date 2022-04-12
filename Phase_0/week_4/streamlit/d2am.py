import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import plotly.express as px

st.title('My First App-Pokemon')

@st.cache
def load_data():
    data = pd.read_csv('../../week_1/data/Pokemon.csv')
    return data

df = load_data()

st.subheader('basic-viz')

fig, ax = plt.subplots(figsize=[12,7])
sns.histplot(df['Attack'])
st.pyplot(fig)

st.subheader('callback')

selected_gen = st.selectbox('Select Generation', options=(1, 2, 3, 4, 5, 6), index=4)

fig1, ax1 = plt.subplots(figsize=[12,7])
sns.histplot(df[df['Generation']==selected_gen]['Attack'])
st.pyplot(fig1)

st.subheader('callback-pairplot')
selected_type = st.radio(label='Choose Type 1', options=df['Type 1'].unique())

fig2, ax2 = plt.subplots(figsize=[12,7])
sns.scatterplot(df[df['Type 1']==selected_type]['Attack'], df[df['Type 1']==selected_type]['Speed'])
st.pyplot(fig2)

st.write(df[df['Type 1']=='Flying'])