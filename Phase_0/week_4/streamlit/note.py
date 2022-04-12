import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.error import URLError

st.title("My First Streamlit Apps")

st.write("Here's our first attempt at using data to create a table:")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.dataframe(df)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

if st.checkbox('Show map'):
    st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option


options = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', options

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

selected_radio = st.radio("What is your favorite color?", ("Red", "Blue", "Green"),2)

if selected_radio == "Red":
    st.write("Red is the best color")
elif selected_radio == "Blue":
    st.write("Blue is the best color")
else:
    st.write("Green is the best color")

st.header('this is select number')
st.selectbox(label="Select a number", options=[1, 2, 3, 4, 5],index=2)

st.header('this is multiple secelct')
multi = st.multiselect(label="Select a food", options=["noodle","pizza","burger","rice","pasta"],default=["noodle","pizza"])

st.write(multi)

if len(multi) >1:
    st.write("You selected:",multi)


st.header("this is sillider")
st.slider(label="Select a number", min_value=0, max_value=10, value=5)

st.header('this is range slider')
st.slider("select range",0.0,100.0,(20.0,80.0))

st.header("this is date input")
date1 = st.date_input("Select a date", value=pd.Timestamp("2022-01-01"))
st.write('your booking will arrive in :',date1)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

number = st.number_input('Insert a number')
st.write('The current number is ', number)

txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (
    ''')

st.write(txt)

txt1 =  '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (
    '''
st.write(txt1)

st.sidebar.header('this is sidebar')