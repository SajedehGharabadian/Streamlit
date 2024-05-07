import streamlit as st

x = 0

col1, col2, col3 = st.columns(3)


with col1:
    minus_btn = st.button("➖", type='primary')

with col2:
    header = st.header(str(x))

with col3:
    plus_btn = st.button("➕", type='primary')

if minus_btn:
    header -= 1
    x -= 1

if plus_btn:
    header += 1
    x += 1
