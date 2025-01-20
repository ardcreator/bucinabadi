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


def main():
    st.title("💖 Sistem Cinta Abadi 💖")
    st.markdown("Selamat datang di aplikasi **Bucin Abadi**, tempat di mana cinta tidak pernah ada akhirnya.")

    # Memasukkan nama orang tersayang
    if st.session_state.hati is None:
        nama = st.text_input("Masukkan nama orang tersayang kamu:", key="nama_input")
        if st.button("Mulai", key="mulai_btn"):
            if nama:
                st.session_state.hati = Hati(nama)
                st.session_state.musik_aktif = True
                st.experimental_set_query_params(refresh="true")
            else:
                st.warning("Nama tidak boleh kosong.")
    else:
        nama = st.session_state.hati.nama
        # Menu Cinta
        st.header(f"Cinta untuk {nama}")
        menu = st.radio("Pilih menu:", ["Ungkapkan Cinta", "Kirim Pesan Cinta", "Lihat Rindu", "Reset Cinta"])

        # Musik latar belakang
        if st.session_state.musik_aktif:
            musik_html = """
            <audio autoplay loop style="display: none;">
                <source src="https://www.bensound.com/bensound-music/bensound-romantic.mp3" type="audio/mp3">
            </audio>
            """
            st.markdown(musik_html, unsafe_allow_html=True)

        if menu == "Ungkapkan Cinta":
            if st.button("Ungkapkan"):
                hasil = st.session_state.hati.ungkapkan_cinta()
                st.audio("https://www.soundjay.com/button/beep-07.wav", format="audio/wav")
                st.success(hasil)

        elif menu == "Kirim Pesan Cinta":
            pesan = st.text_input("Tulis pesanmu:", key="pesan_input")
            if st.button("Kirim Pesan"):
                if pesan:
                    hasil = st.session_state.hati.kirim_pesan_cinta(pesan)
                    st.audio("https://www.soundjay.com/button/button-09.wav", format="audio/wav")
                    st.success(hasil)
                else:
                    st.warning("Pesan tidak boleh kosong.")

        elif menu == "Lihat Rindu":
            st.info(f"Rindu untuk {nama}: {st.session_state.hati.rindu} kali.")

        elif menu == "Reset Cinta":
            if st.button("Reset"):
                st.session_state.hati = None
                st.session_state.musik_aktif = False
                st.audio("https://www.soundjay.com/button/beep-10.wav", format="audio/wav")
                st.warning("Hati telah di-reset. Musik romantis telah berhenti.")
                st.experimental_set_query_params(refresh="true")

    # Footer dengan credit
    st.markdown("---")
    st.markdown(
        """
        <style>
        footer {visibility: hidden;}
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            background-color: #f9f9f9;
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
