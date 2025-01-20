import streamlit as st
import random
import urllib.parse

# Set page title
st.set_page_config(
    page_title="Sistem Cinta Abadi",
    page_icon="❤️"
)

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


def main():
    st.markdown(
        "<h1 style='text-align: center; color: #ff5e6c;'>💖 Sistem Cinta Abadi 💖</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center; font-size: 1.2rem; color: #444;'>Selamat datang di aplikasi <b>Bucin Abadi</b>, tempat di mana cinta tidak pernah ada akhirnya.</p>",
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
    else:
        nama = st.session_state.hati.nama
        # Menu Cinta
        st.header(f"Cinta untuk {nama}")
        menu = st.radio("Pilih menu:", ["Ungkapkan Cinta", "Kirim Pesan Cinta", "Lihat Rindu", "Reset Cinta", "Happy Birthday", "Happy Anniversary", "Bagikan"])

        # Musik latar belakang
        if st.session_state.musik_aktif:
            play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/backsound.mp3", volume=0.2, loop=True)

        if menu == "Ungkapkan Cinta":
            if st.button("Ungkapkan"):
                hasil = st.session_state.hati.ungkapkan_cinta()
                play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/love.mp3", volume=1.0, loop=False)
                st.success(hasil)

        elif menu == "Kirim Pesan Cinta":
            pesan = st.text_input("Tulis pesanmu:")
            if st.button("Kirim Pesan"):
                if pesan:
                    hasil = st.session_state.hati.kirim_pesan_cinta(pesan)
                    play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/pesan.mp3", volume=0.7)
                    st.success(hasil)
                else:
                    st.warning("Pesan tidak boleh kosong.")

        elif menu == "Lihat Rindu":
            st.info(f"Rindu untuk {nama}: {st.session_state.hati.rindu} kali.")

        elif menu == "Reset Cinta":
            if st.button("Reset"):
                st.session_state.hati = None
                st.session_state.musik_aktif = False
                play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/reset.mp3", volume=1.0)
                st.warning("Hati telah di-reset. Musik romantis telah berhenti.")
                # Tidak perlu menggunakan `st.experimental_rerun()`
                # Kita cukup membiarkan aplikasi tetap berjalan dan state akan direset

        elif menu == "Bagikan":
            st.markdown(
                "<h3 style='text-align: center;'>Bagikan Halaman Ini</h3>",
                unsafe_allow_html=True,
            )

            share_url = f"https://bucinabadi.streamlit.app/"

            # Facebook Share
            fb_url = f"https://www.facebook.com/sharer/sharer.php?u={share_url}"

            # Twitter Share
            twitter_text = urllib.parse.quote("Cek aplikasi ini, Sistem Cinta Abadi! ❤️")
            twitter_url = f"https://twitter.com/intent/tweet?text={twitter_text}&url={share_url}"

            # Instagram (Redirect ke URL)
            insta_url = f"https://www.instagram.com/?url={share_url}"

            # LinkedIn
            linkedin_url = f"https://www.linkedin.com/shareArticle?mini=true&url={share_url}&title=Sistem+Cinta+Abadi"

            # Tombol Bagikan
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <a href="{fb_url}" target="_blank">
                        <button style="background-color: #1877F2; color: white; padding: 10px 20px; border-radius: 5px; margin: 5px;">
                            Bagikan ke Facebook
                        </button>
                    </a>
                    <a href="{twitter_url}" target="_blank">
                        <button style="background-color: #1DA1F2; color: white; padding: 10px 20px; border-radius: 5px; margin: 5px;">
                            Bagikan ke Twitter
                        </button>
                    </a>
                    <a href="{insta_url}" target="_blank">
                        <button style="background-color: #E1306C; color: white; padding: 10px 20px; border-radius: 5px; margin: 5px;">
                            Bagikan ke Instagram
                        </button>
                    </a>
                    <a href="{linkedin_url}" target="_blank">
                        <button style="background-color: #0077B5; color: white; padding: 10px 20px; border-radius: 5px; margin: 5px;">
                            Bagikan ke LinkedIn
                        </button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Footer
    st.markdown(
        """
        <div style="text-align: center; font-size: 12px; color: #666; padding: 10px;">
        Dibuat dengan ❤️ oleh <b>Ashari Rasyid</b>.
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
