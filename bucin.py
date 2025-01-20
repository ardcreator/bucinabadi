import streamlit as st
import random
import urllib.parse
from fpdf import FPDF
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

# Set page title
st.set_page_config(page_title="Sistem Cinta Abadi")

class Hati:
    def __init__(self, nama):
        self.nama = nama
        self.rindu = 0

    def ungkapkan_cinta(self):
        self.rindu += 1
        return f"{self.nama}, kamu adalah alasanku bangun setiap pagi. Aku rindu {self.rindu} kali lebih banyak setiap hari."

    def kirim_pesan_cinta(self, pesan):
        return f"Pesan untuk {self.nama}: {pesan}"

# Inisialisasi state Streamlit
if 'hati' not in st.session_state:
    st.session_state.hati = None
if 'musik_aktif' not in st.session_state:
    st.session_state.musik_aktif = False

def play_audio(url, volume=1.0, loop=False):
    """
    Fungsi untuk memutar audio di latar belakang menggunakan HTML dengan kontrol volume.
    """
    loop_attr = "loop" if loop else ""
    audio_html = f"""
    <audio autoplay {loop_attr} style="display: none;" volume="{volume}">
        <source src="{url}" type="audio/mpeg">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

def generate_image(message, filename="output.png"):
    """
    Membuat gambar ucapan.
    """
    img = Image.new('RGB', (800, 400), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Menggunakan font default jika custom font tidak ada
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    text_width, text_height = draw.textsize(message, font=font)
    x = (800 - text_width) // 2
    y = (400 - text_height) // 2

    draw.text((x, y), message, fill="black", font=font)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

def generate_pdf(message, filename="output.pdf"):
    """
    Membuat file PDF ucapan.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, message)
    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer

def main():
    st.markdown(
        "<h1 style='text-align: center; color: #ff5e6c;'>💖 Sistem Cinta Abadi 💖</h1>",
        unsafe_allow_html=True,
    )

    # Memasukkan nama orang tersayang
    if st.session_state.hati is None:
        nama = st.text_input("Masukkan nama orang tersayang kamu:")
        if nama:
            if st.button("Mulai", key="mulai_btn", help="Klik untuk memulai"):
                st.session_state.hati = Hati(nama)
                st.session_state.musik_aktif = True
                play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/backsound.mp3", volume=0.2, loop=True)
        else:
            st.warning("Nama tidak boleh kosong.")
    else:
        nama = st.session_state.hati.nama
        st.header(f"Cinta untuk {nama}")
        menu = st.radio("Pilih menu:", ["Happy Birthday", "Happy Anniversary", "Bagikan"])

        if menu == "Happy Birthday":
            birthday_message = st.text_area(f"Masukkan pesan untuk {nama} di ulang tahunnya:")
            if st.button("Kirim Ucapan Ulang Tahun"):
                if birthday_message:
                    play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/birthday.mp3", volume=1.0)
                    st.markdown(f"<h2 style='text-align: center;'>🎉 Selamat Ulang Tahun, {nama}! 🎉</h2>", unsafe_allow_html=True)
                    st.markdown(f"<p style='text-align: center; font-size: 1.5rem;'>{birthday_message}</p>", unsafe_allow_html=True)

                    st.session_state.share_message = f"🎉 Selamat Ulang Tahun, {nama}! 🎉 {birthday_message}"

                    img_buffer = generate_image(st.session_state.share_message)
                    st.download_button("Unduh sebagai Gambar", img_buffer, file_name="birthday_message.png", mime="image/png")

                    pdf_buffer = generate_pdf(st.session_state.share_message)
                    st.download_button("Unduh sebagai PDF", pdf_buffer, file_name="birthday_message.pdf", mime="application/pdf")
                else:
                    st.warning("Pesan tidak boleh kosong.")

        elif menu == "Happy Anniversary":
            anniversary_message = st.text_area(f"Masukkan pesan untuk {nama} di anniversary pernikahannya:")
            if st.button("Kirim Ucapan Anniversary"):
                if anniversary_message:
                    play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/anniversary.mp3", volume=1.0)
                    st.markdown(f"<h2 style='text-align: center;'>💍 Selamat Anniversary, {nama}! 💍</h2>", unsafe_allow_html=True)
                    st.markdown(f"<p style='text-align: center; font-size: 1.5rem;'>{anniversary_message}</p>", unsafe_allow_html=True)

                    st.session_state.share_message = f"💍 Selamat Anniversary, {nama}! 💍 {anniversary_message}"

                    img_buffer = generate_image(st.session_state.share_message)
                    st.download_button("Unduh sebagai Gambar", img_buffer, file_name="anniversary_message.png", mime="image/png")

                    pdf_buffer = generate_pdf(st.session_state.share_message)
                    st.download_button("Unduh sebagai PDF", pdf_buffer, file_name="anniversary_message.pdf", mime="application/pdf")
                else:
                    st.warning("Pesan tidak boleh kosong.")

        elif menu == "Bagikan":
            if "share_message" in st.session_state:
                share_message = urllib.parse.quote(st.session_state.share_message)
                twitter_url = f"https://twitter.com/intent/tweet?text={share_message}"

                st.markdown(f"""
                    <div style="text-align: center;">
                        <a href="{twitter_url}" target="_blank">
                            <button style="background-color: #1DA1F2; color: white; padding: 10px 20px; border-radius: 5px;">
                                Share on Twitter
                            </button>
                        </a>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("Belum ada pesan yang bisa dibagikan.")

if __name__ == "__main__":
    main()
