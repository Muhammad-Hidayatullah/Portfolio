import streamlit as st


with st.sidebar:
    st.success("Pilh Salah Satu di Atas")
    
    
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
st.title("Tentang Saya")
st.divider()
col1, col2 = st.columns(2, gap="large")
with col1:
    st.write(
        """
            - Nama : Muhammad Hidayatullah
            - Universitas : UPN Veteran Jakarta
            - Jurusan       : Fakulitas Ilmu Komputer 
            - Prodi         : S1 Sistem Informasi
            - Semester      : 7
            - Angkatan      : 2021
        """
    )
    st.markdown(
        """
            Hi,
            Perkenalkan nama saya Muhammad Hidayatullah
            mahasiswa UPN Veteran Jakarta Fakultas Ilmu Komputer Jurusan S1 Sistem Informasi Semester 7.
            Saya sangat bersemangat dan memiliki hasrat yang kuat dalam menggali potensi teknologi dan sistem informasi.
            Dengan dedikasi tinggi terhadap pembelajaran, saya telah mengembangkan keterampilan dalam analisis sistem, pengembangan perangkat lunak, manajemen data, pengembangan website, dan lain-lainnya.
            Kreativitas saya terbukti dalam berkontribusi pada proyek-proyek kelompok serta kemampuan saya dalam memecahkan masalah dengan pendekatan inovatif. 
            Saya sangat antusias untuk terus berkembang dan belajar, serta berkontribusi pada tim yang dinamis dalam lingkungan profesional yang memungkinkan saya memanfaatkan pengetahuan 
            dan keterampilan saya untuk mencapai tujuan bersama.
        """
    )
    
EMAIL = "muhmammdhidytllh@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/muhammad-hidayatullah-0788b41bb/"
with col2:
    st.image("images/Muhammad Hidayatullah_foto.png")
    st.write("📩", EMAIL)
    st.write("💼 [Profil Linkedin](https://www.linkedin.com/in/muhammad-hidayatullah-0788b41bb/)")
    
