import streamlit as st

st.title("Iris prediction model")
#button_clicked = st.button("Click me")

#if button_clicked:
#    st.write("It worked")
#    st.balloons()

with st.form(key="Iris_new_flower"):
    st.write("Choose features values of your new flower")
    sepal_length = st.slider("Sepal length")
    sepal_width = st.slider("Sepal width")
    petal_length = st.slider("Petal length")
    petal_width = st.slider("Petal width")
    submitted = st.form_submit_button("Submit")
    if submitted:
       st.write("Sepal length", sepal_length, "Sepal width", sepal_width,"Petal length",petal_length,"Petal width",petal_width)
       entry = {
                    "Sepal length":sepal_length,
                    "Sepal width" :sepal_width,
                    "Petal length":petal_length,
                    "Petal width":petal_width
                }