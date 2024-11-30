# itinerary_display.py

import os
import streamlit as st
from components.image_display import display_images
from data.itinerary_data import itinerary

def display_itinerary(date):
    day_data = itinerary.get(date, {})
    if not day_data:
        st.write("無行程資料")
        return
    
    st.subheader(f"{day_data['title']}")
    
    for period, details in day_data.items():
        if period != "title":
            st.markdown(f"### {details['attraction']}")
            if "alias" in details:
                st.write(f"#️⃣ {details['alias']}")
            st.write(f"⏲️ 開始時間：{details['start_time']}")
            if "end_time" in details:
                st.write(f"⏲️ 結束時間：{details['end_time']}")
            if "duration" in details:
                st.write(f"⏰ 停留時間：{details['duration']}")
            if "transport" in details:
                st.write(f"🚕 {details['transport']}")

            if "description" in details:
                with st.expander("✨ 詳細介紹", expanded=True):
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.write(details['description'])
           
            # 顯示圖片
            if "file" in details:                
                file = os.path.join(os.getcwd(), "image", details["file"])
                if os.path.isdir(file):
                    with st.expander("🖼️ 更多圖片", expanded=True):
                        st.markdown("<br>", unsafe_allow_html=True)
                        display_images(file)
                else:
                    st.error(f"File is not found : {file}")
            st.markdown("---")
