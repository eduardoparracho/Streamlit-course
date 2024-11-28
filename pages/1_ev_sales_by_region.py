import streamlit as st 
import pandas as pd
from utils import load_data

st.title("EV Adoption Tracker")
st.subheader("EV Sales Data")

df_sales = load_data()[0]

country = st.selectbox("Filter country:",df_sales["region"].unique())

st.bar_chart(df_sales[df_sales.region == country], x="year", y="value",color="powertrain")

st.divider()

st.subheader("Top Sales by Country & Powertrain")

country_selection = st.multiselect("Filter country:",df_sales["region"].unique())
powertrain = st.selectbox("Filter powertrain:",df_sales["powertrain"].unique())

st.line_chart(df_sales[(df_sales.region.isin(country_selection)) & (df_sales.powertrain == powertrain)], x="year", y="value",color="region")