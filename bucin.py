import streamlit as st
import random

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
        ungkapan = [
            f"{self.nama}, kamu adalah alasanku bangun setiap pagi. Aku rindu {self.rindu} kali lebih banyak setiap hari.",
            f"Setiap detik bersamamu adalah momen yang tak ternilai. Aku rindu {self.rindu} kali lebih dalam.",
            f"Di setiap sudut dunia, aku selalu memikirkanmu, {self.nama}. Rindu ini tak pernah berhenti.",
            f"{self.nama}, kamu adalah mimpi indah yang menjadi kenyataan. Aku rindu {self.rindu} kali lebih lama.",
            f"Setiap kali aku melihat matahari, aku ingat kamu, {self.nama}. Rindu ini semakin dalam.",
            f"Tak ada yang lebih indah dari cinta kita, {self.nama}. Aku rindu {self.rindu} kali lebih besar.",
            f"Kamu adalah kebahagiaan yang datang setiap hari. Aku rindu {self.rindu} kali lebih banyak.",
            f"Rindu ini datang dengan tak terhitung banyaknya, {self.nama}. Setiap hari aku semakin mencintaimu.",
            f"Di setiap langkahku, kamu ada di pikiranku, {self.nama}. Rindu ini semakin menguat.",
            f"Kamu adalah segalanya untukku, {self.nama}. Rindu ini tak akan pernah cukup terungkap.",
            f"Setiap detik aku menunggu kamu, {self.nama}. Rindu ini mengalir begitu dalam.",
            f"{self.nama}, kamu adalah cahaya dalam hidupku, {self.nama}. Rindu ini tak terhitung banyaknya.",
            f"Tak ada kata yang cukup untuk menggambarkan betapa aku merindukanmu, {self.nama}. Setiap detik semakin kuat.",
            f"Aku hanya bisa tersenyum setiap kali memikirkanmu, {self.nama}. Rindu ini semakin membesar.",
            f"{self.nama}, kamu adalah cintaku yang tak terhingga. Rindu ini selalu hadir di setiap langkahku.",
            f"Aku selalu mencintaimu, {self.nama}, lebih dari yang bisa aku ungkapkan. Rindu ini semakin terasa.",
            f"Setiap hari aku ingin selalu bersamamu, {self.nama}. Rindu ini semakin kuat dengan waktu.",
            f"Kamu adalah segalanya bagiku, {self.nama}. Rindu ini datang tanpa henti.",
            f"{self.nama}, aku ingin kamu tahu bahwa setiap detik aku merindukanmu. Rindu ini semakin mendalam.",
            f"Aku tidak bisa berhenti memikirkanmu, {self.nama}. Rindu ini semakin menggila.",
            f"{self.nama}, kamu adalah cinta yang tak akan pernah tergantikan. Rindu ini semakin kuat setiap hari.",
            f"Di setiap tempat, di setiap waktu, kamu selalu ada di pikiranku, {self.nama}. Rindu ini tak pernah hilang.",
            f"Setiap kata yang terucap hanyalah untukmu, {self.nama}. Rindu ini tak terhingga.",
            f"{self.nama}, cintaku padamu lebih besar dari apa pun. Rindu ini semakin menguat.",
            f"Tak ada yang bisa menggantikanmu, {self.nama}. Rindu ini datang tanpa henti.",
            f"{self.nama}, setiap detik tanpamu terasa kosong. Rindu ini semakin terasa.",
            f"Kamu adalah kebahagiaan yang selalu aku tunggu, {self.nama}. Rindu ini tidak pernah berakhir.",
            f"Setiap kali aku menatap langit, aku ingat kamu, {self.nama}. Rindu ini tidak pernah berhenti.",
            f"{self.nama}, aku mencintaimu lebih dari yang bisa aku ungkapkan. Rindu ini semakin terasa.",
            f"Rindu ini seperti ombak yang tak berhenti datang, {self.nama}. Semakin besar dan kuat.",
            f"{self.nama}, hanya ada kamu dalam hatiku. Rindu ini semakin membara.",
            f"Aku ingin selalu ada di sisimu, {self.nama}. Rindu ini tidak ada habisnya.",
            f"Setiap hari tanpamu terasa berat, {self.nama}. Rindu ini datang setiap waktu.",
            f"Aku mencintaimu lebih dari apapun, {self.nama}. Rindu ini semakin dalam dan kuat.",
            f"{self.nama}, kamu adalah bagian dari hidupku yang tak tergantikan. Rindu ini semakin besar.",
            f"Tak ada yang lebih indah dari cintamu, {self.nama}. Rindu ini semakin dalam setiap hari.",
            f"Aku tak bisa hidup tanpa kamu, {self.nama}. Rindu ini datang dengan tak terhitung banyaknya.",
            f"Setiap detik aku mengingatmu, {self.nama}. Rindu ini semakin terasa.",
            f"Rindu ini tak akan pernah cukup terungkapkan, {self.nama}. Semakin besar setiap harinya.",
            f"{self.nama}, kamu adalah alasan aku tersenyum setiap hari. Rindu ini semakin membesar.",
            f"Semakin aku mencintaimu, semakin besar rasa rinduku, {self.nama}. Setiap detik terasa panjang.",
            f"Setiap hari aku menantikan kamu, {self.nama}. Rindu ini semakin kuat dengan waktu.",
            f"{self.nama}, kamu adalah cinta yang sempurna. Rindu ini semakin mendalam.",
            f"Rindu ini selalu hadir setiap kali aku memikirkanmu, {self.nama}. Semakin besar setiap hari."
        ]
        # Pilih ungkapan acak
        self.rindu += 1
        return random.choice(ungkapan)


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
    # Set background image
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background: url('https://images.wallpapersden.com/image/download/sunset-heart-hd-romantic-valentine-s-day_bmdma2mUmZqaraWkpJRmbmdlrWZlbmw.jpg');
            background-size: cover;
            background-position: center;
        }
        </style>
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
                play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/backsound.mp3", volume=0.2, loop=True)
            else:
                st.warning("Nama tidak boleh kosong.")
    else:
        nama = st.session_state.hati.nama
        # Menu Cinta
        st.header(f"Cinta untuk {nama}")
        menu = st.radio("Pilih menu:", ["Ungkapkan Cinta", "Kirim Pesan Cinta", "Lihat Rindu", "Reset Cinta"])

        # Musik latar belakang
        if st.session_state.musik_aktif:
            play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/backsound.mp3", volume=0.2, loop=True)

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
