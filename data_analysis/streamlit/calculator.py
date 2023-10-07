import streamlit as st

st.title("calculator")
st.markdown("welcome to my first app")


c1 , c2=st.columns(2)
fnum=c1.number_input("enter first number")
snum=c2.number_input("enter secod number")


options =["add","sub","mul","div"]
choice =st.radio("select an operation",options,horizontal=True)


button = st.button("calculate")

if button:
    if choice=="add":
     result=fnum+snum
    if choice=="sub":
     result=fnum-snum
    if choice=="mul":
     result=fnum*snum
    if choice=="div":  
     result=fnum/snum
st.warning(f"result is {result}")    