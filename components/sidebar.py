# sidebar.py
import streamlit as st
from data import flight_data
from data import price_data
from datetime import datetime

def display_sidebar(selected_date, dates):
    # 確保 dates 是 datetime 格式
    dates = [datetime.strptime(date, "%Y-%m-%d") if isinstance(date, str) else date for date in dates]
    
    st.sidebar.header("航班資訊")
    st.sidebar.subheader("去程")
    st.sidebar.write(f"""
    **出發**: {flight_data.departure_info["departure_time"]} - {flight_data.departure_info["from"]}  
    **到達**: {flight_data.departure_info["arrival_time"]} - {flight_data.departure_info["to"]}  
    **航班時間**: {flight_data.departure_info["duration"]}  
    """)
    
    st.sidebar.subheader("回程")
    st.sidebar.write(f"""
    **出發**: {flight_data.return_info["departure_time"]} - {flight_data.return_info["from"]}  
    **到達**: {flight_data.return_info["arrival_time"]} - {flight_data.return_info["to"]}  
    **航班時間**: {flight_data.return_info["duration"]}  
    """)
    
    # 日期範圍滑桿
    selected_date = st.sidebar.slider(
        "選擇日期以查看行程", 
        min_value=dates[0], 
        max_value=dates[-1], 
        value=dates[0]
    )    

    # st.sidebar.markdown("---")
    # st.sidebar.subheader("預算表")

    # st.sidebar.table(price_data.budget_table)
    # st.sidebar.write(price_data.total_text)
    
    return selected_date
