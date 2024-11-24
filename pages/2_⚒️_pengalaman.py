import streamlit as st


    
    
st.html(
    '''
    <style>
    hr {
        border-color: darkblue;
        width: "500px";
    }
    </style>
    '''
)
st.title("Pengalaman")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.header("Pengalaman & Pencapaian")
    st.write(
    """
        - Magang MSIB MBKM di PT BNI sebagai Analis Data
        - Mentor STRING Mata Kuliah Pemrograman Web
    """
    )
    
    st.write("")
    
    st.header("Sertifikasi")
    st.write(
    """
        - TOEFL ITP sebesar 590
        - Memulai Pemrograman dengan C oleh dicoding
        - Introduction to Excel oleh Coursera Project Network
        - Python Fundamental for Data Science oleh DQLab
        - R Fundamental for Data Science oleh DQLab
        - Fundamental SQL Using SELECT Statement oleh DQLab
    """
    )

with col2:
    st.header("Projects")
    st.write("[Cek pada link Github berikut](https://github.com/Muhammad-Hidayatullah)")
    