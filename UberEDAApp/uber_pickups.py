import streamlit as st
import numpy as np
import pandas as pd

st.title('Uber pickups in NYC')

DATE_COLUMN='date/time'
DATA_PATH='https://raw.githubusercontent.com/OmarEltouny78/UberStreamlit/main/UberEDAApp/Datasets/uber-raw-data-sep14.csv'


@st.cache_data
def load_data(nrows,DATAPATH='https://raw.githubusercontent.com/OmarEltouny78/UberStreamlit/main/UberEDAApp/Datasets/uber-raw-data-sep14.csv'):
    data=pd.read_csv(DATA_PATH,nrows=nrows)
    lowercase=lambda x: str(x).lower()
    data.rename(lowercase,axis='columns',inplace=True)
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state=st.text('Loading data......')

data=load_data(1000)

data_load_state.text('Data loaded ... Done')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.dataframe(data)




st.subheader('Number of pickups per hour')
hist_values=np.histogram(data[DATE_COLUMN].dt.hour,bins=24,range=(0,24))[0]

st.bar_chart(hist_values)

hour_to_filter=st.slider('hour',0,23,17)

filtered_data=data[data[DATE_COLUMN].dt.hour==hour_to_filter]



st.subheader(f'Map of all pickups at {hour_to_filter}:00')

st.map(filtered_data)

