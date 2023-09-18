import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Cavvoh')

st.info('')

icon_size = 20


