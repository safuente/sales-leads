import streamlit as st
import json
import pandas as pd
from decouple import config, Csv, AutoConfig


def open_json(output_file):
    with open(output_file, 'r') as f:
        result = json.load(f)
    return result


config = AutoConfig(search_path='salesleads/spiders/')
st.title('Sales Leads Results')
st.write('This sales leads application shows the results of scrapy https://trends.builtwith.com for different \
         countries. ')


st.markdown("***")

location_site = st.selectbox(
    'Please choose a country to show stores data',
    config('COUNTRIES', cast=Csv()))

df = pd.read_json("salesleads/data/stores.json").sort_values("traffic", ascending=False)
df = df[df["location"] == location_site]
st.title(f"Stores ordered by web traffic in {location_site}")
st.dataframe(df, width=720)

