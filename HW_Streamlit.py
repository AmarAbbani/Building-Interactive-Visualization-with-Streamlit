# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
st.title("Hello")

import pandas as pd
import plotly.express as px
df= pd.read_csv("Activity.csv")


if st.checkbox("show Activity Dataset"):
    st.subheader("Activity Dataset")
    st.write(df)


fig=px.line(df,x="Id",y="Calories",title="Activity_Calories_Line")
st.plotly_chart(fig)

fig2=px.bar(df,x="ActivityDate",y="TotalDistance",color="Id",title="Activity_Distance_by_Id_Bar")
st.plotly_chart(fig2)


fig3=px.scatter_3d(df,x="Id",y="TotalDistance",z="TotalSteps",title="Distance_and_Calories_Scatter",color="Calories")
st.plotly_chart(fig3)

fig4=px.box(df,y="Calories",hover_data=["TotalDistance"],title="Calories_and_Distance_Box")
st.plotly_chart(fig4)

fig5=px.pie(df,values="Calories",names="Id",title="Calories_Pie")
st.plotly_chart(fig5)

st.text("Image below")



st.balloons()

st.snow()

from PIL import Image
image = Image.open('image.png')

st.image(image, caption='Exercise activity')















