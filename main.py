# main.py
import streamlit as st
from components.sidebar import display_sidebar
from components.itinerary_display import display_itinerary
from data.itinerary_data import itinerary
from data import page_title

# 設定頁面
st.set_page_config(
    page_title=page_title.name, 
    page_icon="✈️", 
    layout="wide"
    )

# 導入側邊欄
dates = list(itinerary.keys())
selected_date = display_sidebar(dates[0], dates)
display_itinerary(selected_date.strftime("%Y-%m-%d"))
