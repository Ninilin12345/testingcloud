import streamlit as st

st.header ('Weight Calculation !')

weight = st.number_input('Enter your weight (pound)')
height = st.number_input('Enter your height (cm)')
st.radio('Choose',('Male','Female'))


weight_result = weight* 0.45
height_result= height * 0.01

result = st.button('Calculate')
if result:
    body_weight = weight_result/height_result ** 2 
    values = st.slider('Your Weight Range :',0.0, 100.0, (0.0, body_weight))  
    st.write('Your BMI is :',body_weight)
    if body_weight < 19:
        st.write ('You are underweight')
    elif body_weight < 25:
        st.write ('You are Normal')
    elif body_weight < 30:
        st.write ('You are Overweight')
    else:
        st.write ('You are obesity')
        
        






