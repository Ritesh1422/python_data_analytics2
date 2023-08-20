import streamlit as st
# run in terminal
#cd data_analysis
# streamlit run dapp.py

import pandas as pd 
import numpy as np
import plotly.express as px
import seaborn as sns

#title app
st.title('data analysis app')

st.cache_data()
def load_data():
    df=sns.load_dataset('titanic')
    return df
with st.spinner('loading data'):
    df=load_data()
    st.write("@@@")


if st.checkbox("view all data"):
   st.dataframe(df)

if st.checkbox("show some stats"):
    cat_col=df.select_dtypes(exclude=np.number).columns.tolist()
    num_col=df.select_dtypes(include=np.number).columns.tolist()
    st.text(num_col)

st.metric(label="average age of passangers",
          value=df['age'].mean().astype(int))

st.metric(label="averaeg fare",
          value=df['fare'].mean().astype(int),
          delta=round(df['fare'].std(),1))

c1,c2=st.columns(2)
c1.text("number of survivors")
survivors=df['survived'].value_counts()
c1.dataframe(survivors)
fig=px.pie(survivors,survivors.index,survivors.values)
c1.plotly_chart(fig,use_container_width=True)
c2.text("number of passengers inn each class")
classes=df['pclass'].value_counts()
c2.dataframe(classes)
fig=px.bar(classes,classes.index,classes.values)
c2.plotly_chart(fig,use_container_width=True)



# if st.checkbox("visualize data"):
#     st.subheader("catagorical data visualition")
#     sel_col=st.selectbox("select column",cat_cols,)                          #horizontal=True)
#     #sel_col_count=df[sel_col]_count,sel_col_count.index,sel_col_count.values]
#     sel_col_count=df[sel_col],sel_col_count.index,sel_col_count.values,title=f"Distribution of {sel_col}"
#                      st.plotly_chart(fig,use_container_width=True)

if st.