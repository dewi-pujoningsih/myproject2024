import streamlit as st
import pandas as pd
import math
from pathlib import Path

def faktorial(n):
    hasil=1
    for i in range(1,n+1):
        hasil*=i
    print(f"Hasil {n}! adalah {hasil}")
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
elif add_selectbox=="Kalkulator Faktorial":
    angka=st.input("Masukkan n:")
    faktorial(angka)
    

