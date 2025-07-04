import streamlit as st
import pandas as pd
import math
from pathlib import Path


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Pilih menu berikut:",
    ("Beranda", "Kalkulator Faktorial", "Cek Ganjil Genap", "Tentang kami")
)
if add_selectbox=="Beranda":
    st.markdown("*Aplikasi* **Gado** ***Gado***.")
    st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

