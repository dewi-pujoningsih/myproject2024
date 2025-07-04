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
    st.header("**Aplikasi Aneka Fungsi**")
    st.markdown('''
    Aplikasi ini dibuat untuk memenuhi tugas Praktik Logika dan Pemrograman Komputer.
    Tugas disusun oleh 5 orang''')

