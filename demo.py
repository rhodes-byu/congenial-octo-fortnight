import streamlit as st
from fortnight import fight

st.title('Demo: Streamlit')

num = st.text_input('Enter an integer', key='number')

if num is not None:
    num = int(num)
    st.write(fight.sum_count(range(num)))