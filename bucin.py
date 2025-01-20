import streamlit as st

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


def play_audio(url, volume=1.0):
    """
    Fungsi untuk memutar audio di latar belakang menggunakan HTML dengan kontrol volume.
    """
    audio_html = f"""
    <audio autoplay style="display: none;" volume="{volume}">
        <source src="{url}" type="audio/mpeg">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)


def main():
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background: transparent;
        }
        .video-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            overflow: hidden;
        }
        .video-container video {
            min-width: 100%;
            min-height: 100%;
            object-fit: cover;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            color: #fff;
            text-align: center;
            text-decoration: none;
            background: linear-gradient(90deg, #ff758c, #ff7eb3);
            border-radius: 30px;
            transition: all 0.3s ease-in-out;
            box-shadow: 0px 4px 15px rgba(255, 94, 136, 0.5);
            cursor: pointer;
            margin: 10px 0;
        }
        .btn:hover {
            background: linear-gradient(90deg, #ff5e6c, #ff738f);
            box-shadow: 0px 6px 20px rgba(255, 94, 136, 0.7);
        }
        .title {
            font-family: 'Caveat', cursive;
            font-size: 3rem;
            color: #ff5e6c;
            text-align: center;
            margin-bottom: 20px;
        }
        </style>
        <div class="video-container">
            <video autoplay muted loop>
                <source src="https://raw.githubusercontent.com/ardcreator/bucinabadi/main/video/background.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="title">💖 Sistem Cinta Abadi 💖</div>', unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; font-size: 1.2rem; color: #444;'>Selamat datang di aplikasi <b>Bucin Abadi</b>, tempat di mana cinta tidak pernah ada akhirnya.</p>",
        unsafe_allow_html=True,
    )

    # Memasukkan nama orang tersayang
    if st.session_state.hati is None:
        nama = st.text_input("Masukkan nama orang tersayang kamu:")
        if st.button("Mulai", key="mulai_btn", help="Klik untuk memulai"):
            if nama:
                st.session_state.hati = Hati(nama)
                st.session_state.musik_aktif = True
                play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/backsound.mp3", volume=0.5)
                st.experimental_rerun()
            else:
                st.warning("Nama tidak boleh kosong.")
    else:
        nama = st.session_state.hati.nama
        # Menu Cinta
        st.header(f"Cinta untuk {nama}")
        menu = st.radio("Pilih menu:", ["Ungkapkan Cinta", "Kirim Pesan Cinta", "Lihat Rindu", "Reset Cinta"])

        # Musik latar belakang
        if st.session_state.musik_aktif:
            play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/backsound.mp3", volume=0.2)

        if menu == "Ungkapkan Cinta":
            if st.button("Ungkapkan"):
                hasil = st.session_state.hati.ungkapkan_cinta()
                play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/love.mp3", volume=1.0)
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
                st.experimental_rerun()

    # Footer
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            background-color: rgba(255, 255, 255, 0.8);
            padding: 10px 0;
            font-size: 12px;
            color: #666;
        }
        </style>
        <div class="footer">
        Dibuat dengan ❤️ oleh <b>Ashari Rasyid</b>.
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
