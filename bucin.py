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


# Inisialisasi state Streamlit
if 'hati' not in st.session_state:
    st.session_state.hati = None


def main():
    st.markdown(
        "<h1 style='text-align: center; color: #ff5e6c;'>💖 Sistem Cinta Abadi 💖</h1>",
        unsafe_allow_html=True,
    )

    # Masukkan nama orang tersayang
    if st.session_state.hati is None:
        nama = st.text_input("Masukkan nama orang tersayang kamu:")
        if nama:
            if st.button("Mulai"):
                st.session_state.hati = Hati(nama)
    else:
        nama = st.session_state.hati.nama

        # Menu pilihan
        menu = st.radio(
            "Pilih menu:",
            ["Ungkapkan Cinta", "Happy Birthday", "Happy Anniversary"],
            horizontal=True
        )

        if menu == "Ungkapkan Cinta":
            if st.button("Ungkapkan"):
                hasil = st.session_state.hati.ungkapkan_cinta()
                play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/love.mp3", volume=1.0, loop=False)
                st.success(hasil)

        elif menu == "Happy Birthday":
            # Input custom pesan
            birthday_message = st.text_area(f"Masukkan pesan untuk {nama} di ulang tahunnya:")
            if st.button("Kirim Ucapan Ulang Tahun"):
                if birthday_message:
                    play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/birthday.mp3", volume=1.0)
                    st.markdown(f"<h2 style='text-align: center;'>🎉 Selamat Ulang Tahun, {nama}! 🎉</h2>", unsafe_allow_html=True)
                    st.markdown(f"<p style='text-align: center; font-size: 1.5rem;'>{birthday_message}</p>", unsafe_allow_html=True)

                    # Generate link for sharing
                    share_message = urllib.parse.quote(f"🎉 Selamat Ulang Tahun, {nama}! 🎉 {birthday_message}")
                    twitter_url = f"https://twitter.com/intent/tweet?text={share_message}"

                    # Create share button
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
                    st.warning("Pesan tidak boleh kosong.")

        elif menu == "Happy Anniversary":
            # Input custom pesan
            anniversary_message = st.text_area(f"Masukkan pesan untuk {nama} di anniversary pernikahannya:")
            if st.button("Kirim Ucapan Anniversary"):
                if anniversary_message:
                    play_audio("https://raw.githubusercontent.com/ardcreator/bucinabadi/main/audio/anniversary.mp3", volume=1.0)
                    st.markdown(f"<h2 style='text-align: center;'>💍 Selamat Anniversary, {nama}! 💍</h2>", unsafe_allow_html=True)
                    st.markdown(f"<p style='text-align: center; font-size: 1.5rem;'>{anniversary_message}</p>", unsafe_allow_html=True)

                    # Generate link for sharing
                    share_message = urllib.parse.quote(f"💍 Selamat Anniversary, {nama}! 💍 {anniversary_message}")
                    twitter_url = f"https://twitter.com/intent/tweet?text={share_message}"

                    # Create share button
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
                    st.warning("Pesan tidak boleh kosong.")


if __name__ == "__main__":
    main()
