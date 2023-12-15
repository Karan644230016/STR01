import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.header("การวิเคราะห์ความรู้สึกภาษาไทย")
st.subheader("Kairung Hengpraprohm")

col1, col2 = st.columns(2)
with col1:
    st.image('./pic/kairung.jpg')
    lot3="https://app.lottiefiles.com/share/b48d28ba-de1f-4f6b-a3ef-004121fc987d"
    lottie3 = load_lottieurl(lot3)
    st_lottie(lottie3)
with col2:
    st.image('./pic/DS1.jpg')
st.balloons()



st.header('Karan Khanthong')

st.title('การทดสอบเขียนเว็บด้วย Python')
st.header('นาย กรัณฑ์  ขันทอง')
st.subheader('สาขาวิชาเทคโนโลยีสารสนเทศ')
st.markdown("----")

col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
    st.image('./pic/myImg01.jpg')
with col2:
    st.image('./pic/myIris01.jpg')

html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd

dt=pd.read_csv('./data/iris.csv')
st.write(dt.head(10))

dt1 = dt['petal.length'].sum()
dt2 = dt['petal.width'].sum()
dt3 = dt['sepal.length'].sum()
dt4 = dt['sepal.width'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])

if st.button("show bar chart"):
    st.bar_chart(dx2)
    st.button("Not show bar chart")
else :
    st.button("Not show bar chart") 

html_2 = """
<div style="background-color:#B99470;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายคลาสดอกไม้</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")   


ptlen = st.slider("กรุณาเลือกข้อมูล petal.length",0,10)
ptwd = st.slider("กรุณาเลือกข้อมูล petal.width",0,10)

splen = st.number_input("กรุณาเลือกข้อมูล sepal.length")
spwd = st.number_input("กรุณาเลือกข้อมูล sepal.width")

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

if st.button("ทำนายผล"):
   # ทำนาย
   #dt = pd.read_csv("./data/iris.csv") 

   X = dt.drop('variety', axis=1)
   y = dt.variety   

   Knn_model = KNeighborsClassifier(n_neighbors=3)
   Knn_model.fit(X, y)

    #ข้อมูล input สำหรับทดลองจำแนกข้อมูล
   x_input = np.array([[ptlen, ptwd, splen, spwd]])
    # เอา input ไปทดสอบ
   st.write(Knn_model.predict(x_input))
   out=Knn_model.predict(x_input)

   if out[0]=="Setosa":
      st.image("./pic/setosa.jpg")
      st.header("Setosa")
   elif out[0]=="Versicolor":
      st.image("./pic/Versicolor.jpg")
      st.header("Versicolor")
   else:
      st.image("./pic/Verginiga.jpg")  
      st.header("Verginiga")
   st.button("ไม่ทำนายผล")
else :
    st.button("ไม่ทำนายผล")








