import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

connection = sqlite3.connect("data.db")

df = pd.read_sql_query("SELECT * FROM temperature", con=connection)

figure = px.line(x=df["date"], y=df["temperature"], labels={'x': "Date", 'y': "Temperature"})

st.plotly_chart(figure)