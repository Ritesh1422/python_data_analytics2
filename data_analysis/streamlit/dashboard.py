import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("stock prediction dashboard")
st.markdown(" the dashboard will help a researchers to get to know more abt the given dataset and its output  ")

st.sidebar.title("select visual charts")
st.sidebar.markdown("select the charts/plots accordingly:")

#reading the dataset
data=pd.read_csv(r"C:\Users\rites\OneDrive\Documents\python_data_analytics2\data_analysis\streamlit\demo_data_set.csv")

chart_visual=st.sidebar.selectbox("select the charts/plots",('line chart','bar chart','bubble chart'))
st.sidebar.checkbox("show analysis by smoking status",True,key=1)
selected_status=st.sidebar.selectbox("select smoking status",options=['formerly_smocked'])

fig=go.Figure()

if chart_visual=='line chart':
    if selected_status=='formerly_smoked':
        fig.add_trace(go.scatter(x=data.country,y=data.formerly_smoked,mode="lines",name="formerly_smoked"))
    if selected_status=='smokes':
        fig.add_trace(go.scatter(x=data.country, y=data.smokes,mode='lines',name="smokes"))
    if selected_status=='never_smokes':
        fig.add_trace(go.scatter(x=data.country, y=data.never_smokes,mode='lines',name="never_smokes"))
    if selected_status=='unknown':
        fig.add_trace(go.scatter(x=data.country, y=data.unknown,mode='lines',name="unknown")) 

elif chart_visual=='bar_chart' :
    if selected_status=='formerly_smoked':
        fig.add_trace(go.bar(x=data.country,y=data.formerly_smoked,name='formerly_smoked'))  





st.plotly_chart(fig,use_container_width=True)         



