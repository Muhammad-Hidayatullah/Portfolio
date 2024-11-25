import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



st.title("Kirim Pesan Anda")
col1, col2= st.columns(2)



form_kontak = """
    <form action="https://formsubmit.co/muhmammdhidytllh@gmail.com" method="POST">
        <input type="text" name="name" required placeholder="Nama anda">
        <input type="email" name="email" required placeholder="Email anda">
        <textarea name="message" placeholder="Tulis pesan anda"></textarea>
        <button type="submit">Kirim</button>
</form>
"""

with col2:
    st.markdown(
    """
        
        📧 muhmammdhidytllh@gmail.com
        

    """
    )


with col1:
    st.markdown("Silahkan tinggalkan pesan pada kolom yang tersedia")
    st.markdown(form_kontak, unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            
    local_css("./style/style.css")
