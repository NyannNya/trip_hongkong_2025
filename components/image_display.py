# image_display.py
import streamlit as st
from PIL import Image
import os

def display_images(image_folder):
    # 取得圖片檔案清單
    image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    # 每 5 張圖片一列
    for i in range(0, len(image_files), 5):
        cols = st.columns(5)  # 建立 5 個欄位
        for col, img_path in zip(cols, image_files[i:i+5]):  # 取 5 張圖片
            image = Image.open(img_path)
            col.image(image, use_column_width=True)

