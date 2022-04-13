import streamlit as st
import json
import pandas as pd

def open_json(output_file):
    with open(output_file,'r') as f:
        result = json.load(f)
    return result

#TODO
st.title('Sales Leads Results')
st.write('This Streamlit application shows the results of scrapy https://trends.builtwith.com for Spain')

df = pd.read_json("salesleads/data/stores.json").sort_values("traffic", ascending=False)
st.title("Stores ordered by web traffic in Spain")
st.dataframe(df, width=720)

