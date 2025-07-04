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
    st.write(
        '''Aplikasi ini dibuat untuk memenuhi tugas kelompok Praktik LPK 2025. Semoga dapat bermanfaat untuk 
        orang banyak'''
    )

