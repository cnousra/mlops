import streamlit as st

st.title("My beautiful App")
button_clicked = st.button("Click me")

if button_clicked:
    st.write("It worked")
    st.balloons()