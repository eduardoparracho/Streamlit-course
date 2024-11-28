import streamlit as st 
import pandas as pd
from utils import load_data

##################### PAGE SETUP #####################
st.set_page_config(
    page_title="EV Adoption Tracker",
    layout="centered", # or wide
    page_icon="🚗", # choose your favorite icon
    initial_sidebar_state="expanded" # or expanded
)

df_sales, df_charge = load_data()

st.title("Summary")
st.subheader("Overall EV Adoption Data")
st.expander("Data exctracted from IEA API")

current_year_delta = round((df_sales[df_sales.year == 2022].value.sum() - df_sales[df_sales.year == 2021].value.sum())/df_sales[df_sales.year == 2021].value.sum()*100,2)
current_year_sales = round(df_sales[df_sales.year == 2022].value.sum()/1000000,2)
last_year_sales = round(df_sales[df_sales.year == 2021].value.sum()/1000000,2)

current_year_chargers = round(df_charge[df_charge.year == 2022].value.sum()/1000000,2)
last_year_chargers = round(df_charge[df_charge.year == 2021].value.sum()/1000000,2)
charger_delta = round((current_year_chargers - last_year_chargers)/last_year_chargers *100,2)

col1, col2, col3 = st.columns(3)

card1 = col1.container(border=True)
card2 = col2.container(border=True)
card3 = col3.container(border=True)


card1.metric(label="World EV sales (current year)", value=str(current_year_sales)+"M",delta=str(current_year_delta)+"%")
card2.metric(label="World EV sales Growth", value=str(round(current_year_sales-last_year_sales,2))+"M",delta=str(current_year_delta)+"%")
card3.metric(label="World Charging Ports (current year)", value=str(current_year_chargers)+"M",delta=str(charger_delta)+"%")

st.title("World EV Adoption:")

st.bar_chart(df_sales, x="year", y="value")

st.divider()
st.title("EV Adoption Tracker")
st.subheader("EV Sales Data")

country = st.selectbox("Filter country:",df_sales["region"].unique())

st.bar_chart(df_sales[df_sales.region == country], x="year", y="value",color="powertrain")

st.divider()

st.subheader("Top Sales by Country & Powertrain")

country_selection = st.multiselect("Filter country:",df_sales["region"].unique())
powertrain = st.selectbox("Filter powertrain:",df_sales["powertrain"].unique())

st.line_chart(df_sales[(df_sales.region.isin(country_selection)) & (df_sales.powertrain == powertrain)], x="year", y="value",color="region")