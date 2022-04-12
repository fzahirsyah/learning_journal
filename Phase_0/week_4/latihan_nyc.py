import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import datetime

st.set_option('deprecation.showPyplotGlobalUse', False) #biar gak muncul warning
@st.cache
def get_data():
    return pd.read_csv("http://data.insideairbnb.com/united-states/ny/new-york-city/2021-11-02/visualisations/listings.csv")

df = get_data()
# catatan: dalam streamlit h2= header, h3= subheader
st.markdown(
'''
<style>
h2   {background-color: #b7d7e8;
        color: #000000;
      font-family: "Arial";
      font-size: 40px;
      text-align: center;
      border-radius: 15px 50px;
      margin: 0px 0px 20px 0px;
      }

</style>
<h2>NYC Dataset</h2>
'''
,unsafe_allow_html=True)

st.subheader("Dataframe")
# checkbox 
show_df= st.checkbox("Show dataframe")
st.write(show_df)
if show_df:
  st.write(df)

st.header("Where are the most expensive properties located?")
st.subheader("On a map")
st.markdown("The following map shows the top 1% most expensive Airbnbs priced at $800 and above.")
st.map(df.query("price>=800")[["latitude", "longitude"]].dropna(how="any"))
st.subheader("In a table")
st.markdown("Following are the top five most expensive properties.")
st.write(df.query("price>=800").sort_values("price", ascending=False).head())

st.subheader("Selecting a subset of columns")
st.write(f"Out of the {df.shape[1]} columns, you might want to view only a subset. Streamlit has a [multiselect](https://streamlit.io/docs/api.html#streamlit.multiselect) widget for this.")
defaultcols = ["name", "host_name", "neighbourhood", "room_type", "price"]
cols = st.multiselect("Columns", df.columns.tolist(), default=defaultcols)
st.dataframe(df[cols].head(10))

st.header("Average price by room type")
st.write("You can also display static tables. As opposed to a data frame, with a static table you cannot sorting by clicking a column header.")

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

df_room_type = df.groupby("room_type").price.mean().reset_index()\
    .round(2).sort_values("price", ascending=True)\
    .assign(avg_price=lambda x: x.pop("price").apply(lambda y: "%.2f" % y))

# Display a static table
st.table(df_room_type)

df_room= df.groupby(['room_type'])['price'].mean()
st.table(df_room.reset_index().round(2).sort_values("price", ascending=True)\
    .assign(avg_price=lambda x: x.pop("price").apply(lambda y: "%.2f" % y)))

# plotly barchat horizontal
# fig = px.bar(df_room_type, x="room_type", y="avg_price", color="room_type",
#                 hover_data=["avg_price"])
# st.plotly_chart(fig)

#visualitation average price by room type using plotly
st.subheader("Average price by room type using plotly")
fig = px.bar(df_room_type, x="room_type", y="avg_price", color="room_type",
    labels={"price": "Average Price"},
    title="Average Price by Room Type")
st.plotly_chart(fig)

# plotly barchat vertical
fig = px.bar(x=df_room, y=df_room.index,color=df_room.index,
    orientation="h",
    labels={"y": "Room Type", "x": "Average Price"},
    title="Average Price by Room Type")
st.plotly_chart(fig)

# df_room= df.groupby(['room_type'])['price'].mean()
#visualitation average price by room type using matplotlib
st.subheader("Average price by room type using matplotlib")
plt.figure(figsize=(12,6))
plt.bar(df_room.index, df_room)
plt.title("Average Price by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Average Price")
plt.xticks(rotation=90)
st.pyplot()

#plot


# selectbox
st.subheader("Scatter plot of price vs. number of reviews")
room_type = st.selectbox("Room Type", df.room_type.unique())

# visualitation based on room type
fig = px.scatter(df.query("room_type==@room_type"), x="price", y="number_of_reviews",
    color="room_type", size="price",
    hover_data=["name", "host_name", "neighbourhood", "room_type", "price"])
st.plotly_chart(fig)

# visualitation based on room type
fig= px.histogram(df.query("room_type==@room_type"), x="number_of_reviews", nbins=20, title="Number of Reviews by Room Type")
st.plotly_chart(fig)


st.header("What is the distribution of property price?")
st.write("""Select a custom price range from the side bar to update the histogram below displayed as a Plotly chart using
[`st.plotly_chart`](https://streamlit.io/docs/api.html#streamlit.plotly_chart).""")

values = st.sidebar.slider("Price range", float(df.price.min()), float(df.price.clip(upper=1000.).max()), (50., 300.))
f = px.histogram(df.query(f"price.between{values}"), x="price", nbins=15, title="Price distribution")
f.update_xaxes(title="Price")
f.update_yaxes(title="No. of listings")
st.plotly_chart(f)


#radio button
st.subheader("Select a room type")
room_type_radio = st.radio("Room Type", df.room_type.unique())
st.write(f"The average price of {room_type_radio} is ${df.query('room_type==@room_type_radio').price.mean().round(2)}")


# time series
st.subheader("Time Series")
st.subheader('Time series ')

#set last_review_date to index time series
df_ts = df.copy()
df_ts['last_review_date'] = pd.to_datetime(df['last_review'])
df_ts['last_review_date'] = df_ts['last_review_date'].dt.date

#set last_review_date to index
df_ts.set_index('last_review_date', inplace=True)
df_ts.sort_index(inplace=True)
df_ts.loc[:, 'price']
# filter by date using loc from min to max
# df_ts_filtered = df_ts.loc[df_ts.index.min():df_ts.index.max()]
# start_date = "2019-01-01"
# end_date = "2021-10-20"
# after_start_date = df_ts["date"] >= start_date
# before_end_date = df_ts["date"] <= end_date
# between_two_dates = after_start_date & before_end_date
# filtered_dates = df_ts.loc[between_two_dates]
# filtered_dates



# start_date = st.date_input("Start Date", value=pd.to_datetime("2019-11-04", format="%Y-%m-%d"))
# end_date = st.date_input("End Date", value=pd.to_datetime("today", format="%Y-%m-%d"))

# # convert the dates to string
# start = start_date.strftime("%Y-%m-%d")
# end = end_date.strftime("%Y-%m-%d")

# # filter df_ts base on the date
# df_ts_filtered = df_ts.loc[start:end]
# df_ts_filtered







# options = np.array(df['last_review']).tolist()

# (start_time, end_time) = st.select_slider(" Please select the time series length ：",
#      options = options,
#      #value from date min last_review to date max last_review
#         value = (df['last_review'].min(), df['last_review'].max()))
# st.write(" Time series start time :",end_time)
# st.write(" Time series end time :",start_time)

# #setting index as date
# df['last_review'] = pd.to_datetime(df.Date, format = '%Y-%m-%d')
# df.index = df['last_reivew']

# df = df[start_time:end_time]
# st.dataframe(df)