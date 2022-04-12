import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.error import URLError
import plotly.express as px


st.title('my first streamlit app')

st.subheader('matplotlib')
arr = np.random.normal(1,1,100)
arr

fig, axes = plt.subplots(figsize=(10,5))
axes.hist(arr, bins=20)
st.pyplot(fig)

st.subheader('seaborn')
fig1, axes1 = plt.subplots(figsize=(10,5))
sns.histplot(arr,bins=20)
st.pyplot(fig1)

st.subheader('plotly')
df = px.data.gapminder().query("country=='Canada'")
fig3 = px.line(df, x="year", y="lifeExp", title="Canada Life Expectancy")

st.plotly_chart(fig3)

@st.cache
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/streamlit/demo-data/master/olympics.csv')
    return df



st.write(df.head())

st.subheader('basic viz')

fig4 , axes4 = plt.subplots(figsize=(10,5))
sns.histplot(df['lifeExp'])
st.pyplot(fig4)

selected = st.selectbox('select a country', df['country'].unique())

fig5 ,axes5 = plt.subplots(figsize=(10,5))
sns.histplot(df[df['country']==selected]['lifeExp'])
st.pyplot(fig5)
