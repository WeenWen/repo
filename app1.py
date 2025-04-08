# -*- coding: utf-8 -*-
"""app1.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nWgNos2MAWshxO_cxB-Pfz28iOzlL_bK
"""

import streamlit as st
import math
from datetime import datetime

st.set_page_config(page_title="Python 菜鳥工具包", layout="centered")

st.title("📱 Python 菜鳥工具小網站")
st.markdown("以下是 10 個基礎功能，請從左側選單選擇。")

# 選單
page = st.sidebar.selectbox("請選擇功能", [
    "1. BMI 計算機",
    "2. 攝氏 / 華氏轉換",
    "3. 圓面積計算",
    "4. 三角形面積計算",
    "5. 判斷奇數或偶數",
    "6. 判斷是否為閏年",
    "7. 成績等級判斷",
    "8. 數字加總器",
    "9. 登入驗證模擬",
    "10. 簡單計算機"
])

# 功能 1
if page == "1. BMI 計算機":
    st.header("BMI 計算")
    height = st.number_input("身高（公尺）", 0.5, 2.5, step=0.01)
    weight = st.number_input("體重（公斤）", 20.0, 200.0, step=0.1)
    if st.button("計算 BMI"):
        bmi = weight / (height ** 2)
        st.success(f"你的 BMI 為 {bmi:.2f}")

# 功能 2
elif page == "2. 攝氏 / 華氏轉換":
    st.header("溫度轉換")
    temp = st.number_input("請輸入溫度：")
    unit = st.radio("轉換單位：", ("攝氏轉華氏", "華氏轉攝氏"))
    if st.button("開始轉換"):
        if unit == "攝氏轉華氏":
            result = temp * 9 / 5 + 32
            st.success(f"{temp}°C = {result:.2f}°F")
        else:
            result = (temp - 32) * 5 / 9
            st.success(f"{temp}°F = {result:.2f}°C")

# 功能 3
elif page == "3. 圓面積計算":
    st.header("圓面積計算")
    radius = st.number_input("輸入半徑：", 0.0)
    if st.button("計算面積"):
        area = math.pi * radius ** 2
        st.success(f"面積為 {area:.2f}")

# 功能 4
elif page == "4. 三角形面積計算":
    st.header("三角形面積計算")
    base = st.number_input("底：")
    height = st.number_input("高：")
    if st.button("計算三角形面積"):
        area = 0.5 * base * height
        st.success(f"三角形面積為 {area:.2f}")

# 功能 5
elif page == "5. 判斷奇數或偶數":
    st.header("奇偶判斷器")
    num = st.number_input("輸入一個整數：", step=1)
    if st.button("判斷"):
        if int(num) % 2 == 0:
            st.success(f"{int(num)} 是偶數")
        else:
            st.success(f"{int(num)} 是奇數")

# 功能 6
elif page == "6. 判斷是否為閏年":
    st.header("閏年判斷器")
    year = st.number_input("輸入年份：", step=1)
    if st.button("判斷"):
        year = int(year)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            st.success(f"{year} 是閏年")
        else:
            st.success(f"{year} 不是閏年")

# 功能 7
elif page == "7. 成績等級判斷":
    st.header("成績評分系統")
    score = st.number_input("輸入成績（0-100）：", 0, 100)
    if st.button("評分"):
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        st.success(f"你的等級是：{grade}")

# 功能 8
elif page == "8. 數字加總器":
    st.header("數字加總器")
    numbers = st.text_input("輸入數字（用逗號隔開，例如：1,2,3）：")
    if st.button("加總"):
        try:
            num_list = list(map(float, numbers.split(",")))
            total = sum(num_list)
            st.success(f"總和為 {total}")
        except:
            st.error("請輸入正確格式，例如 1,2,3")

# 功能 9
elif page == "9. 登入驗證模擬":
    st.header("登入模擬")
    user = st.text_input("帳號")
    pwd = st.text_input("密碼", type="password")
    if st.button("登入"):
        if user == "admin" and pwd == "1234":
            st.success("登入成功！歡迎 admin")
        else:
            st.error("帳號或密碼錯誤")

# 功能 10
elif page == "10. 簡單計算機":
    st.header("四則運算")
    a = st.number_input("輸入第一個數字")
    op = st.selectbox("選擇運算", ["+", "-", "*", "/"])
    b = st.number_input("輸入第二個數字")
    if st.button("計算"):
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b != 0:
                result = a / b
            else:
                result = "除數不能為 0"
        st.success(f"結果：{result}")