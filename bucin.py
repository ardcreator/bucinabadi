import streamlit as st
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
if 'page_state' not in st.session_state:
    st.session_state.page_state = "main"
if 'ucapan' not in st.session_state:
    st.session_state.ucapan = ""
if 'ucapan_type' not in st.session_state:
    st.session_state.ucapan_type = ""


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
    # Halaman utama
    if st.session_state.page_state == "main":
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
            nama = st.session_state.hati.nama
            # Menu Cinta
            st.header(f"Cinta untuk {nama}")
            menu = st.radio("Pilih menu:", ["Ungkapkan Cinta", "Happy Birthday", "Happy Anniversary", "Bagikan Sistem"])

            if menu == "Ungkapkan Cinta":
                if st.button("Ungkapkan"):
                    hasil = st.session_state.hati.ungkapkan_cinta()
                    play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/love.mp3", volume=1.0, loop=False)
                    st.success(hasil)

            elif menu == "Happy Birthday":
                pesan = st.text_area("Masukkan ucapan ulang tahun:", height=100)
                if st.button("Kirim Ucapan"):
                    if pesan:
                        st.session_state.page_state = "ucapan"
                        st.session_state.ucapan = pesan
                        st.session_state.ucapan_type = "birthday"

            elif menu == "Happy Anniversary":
                pesan = st.text_area("Masukkan ucapan anniversary:", height=100)
                if st.button("Kirim Ucapan"):
                    if pesan:
                        st.session_state.page_state = "ucapan"
                        st.session_state.ucapan = pesan
                        st.session_state.ucapan_type = "anniversary"

            elif menu == "Bagikan Sistem":
                share_url = f"https://bucinabadi.streamlit.app/"
                fb_url = f"https://www.facebook.com/sharer/sharer.php?u={share_url}"
                twitter_text = urllib.parse.quote("Cek aplikasi ini, Sistem Cinta Abadi! ❤️")
                twitter_url = f"https://twitter.com/intent/tweet?text={twitter_text}&url={share_url}"
                linkedin_url = f"https://www.linkedin.com/shareArticle?mini=true&url={share_url}&title=Sistem+Cinta+Abadi"

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
                        <a href="{linkedin_url}" target="_blank">
                            <button style="background-color: #0077B5; color: white; padding: 10px 20px; border-radius: 5px; margin: 5px;">
                                Bagikan ke LinkedIn
                            </button>
                        </a>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    # Halaman ucapan
    elif st.session_state.page_state == "ucapan":
        ucapan_type = st.session_state.ucapan_type
        title = "Happy Birthday 🎂" if ucapan_type == "birthday" else "Happy Anniversary 🎉"
        st.markdown(f"<h1 style='text-align: center; color: #ff5e6c;'>{title}</h1>", unsafe_allow_html=True)
        st.markdown(
            f"<div style='text-align: center; font-size: 1.5rem; margin: 20px; color: #333;'>{st.session_state.ucapan}</div>",
            unsafe_allow_html=True,
        )

        # Tombol bagikan ke Twitter
        twitter_text = urllib.parse.quote(st.session_state.ucapan)
        twitter_url = f"https://twitter.com/intent/tweet?text={twitter_text}"
        st.markdown(
            f"""
            <div style="text-align: center;">
                <a href="{twitter_url}" target="_blank">
                    <button style="background-color: #1DA1F2; color: white; padding: 10px 20px; border-radius: 5px;">
                        Bagikan ke Twitter
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Tombol kembali
        if st.button("Kembali"):
            st.session_state.page_state = "main"


if __name__ == "__main__":
    main()
