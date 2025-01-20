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


# Inisialisasi objek Hati
if 'hati' not in st.session_state:
    st.session_state.hati = None


def main():
    st.title("❤️ Sistem Cinta Abadi ❤️")
    st.markdown("Selamat datang di aplikasi **Bucin Abadi**, tempat di mana cinta tidak pernah ada akhirnya.")

    if st.session_state.hati is None:
        nama = st.text_input("Masukkan nama orang tersayang kamu:", key="nama_input")
        if st.button("Mulai", key="mulai_btn"):
            if nama:
                st.session_state.hati = Hati(nama)
                st.success(f"Hati telah dibuat untuk {nama}!")
            else:
                st.warning("Nama tidak boleh kosong.")
    else:
        nama = st.session_state.hati.nama
        st.header(f"Cinta untuk {nama}")
        menu = st.radio("Pilih menu:", ["Ungkapkan Cinta", "Kirim Pesan Cinta", "Lihat Rindu", "Reset"])

        if menu == "Ungkapkan Cinta":
            if st.button("Ungkapkan"):
                hasil = st.session_state.hati.ungkapkan_cinta()
                st.success(hasil)

        elif menu == "Kirim Pesan Cinta":
            pesan = st.text_input("Tulis pesanmu:", key="pesan_input")
            if st.button("Kirim Pesan"):
                if pesan:
                    hasil = st.session_state.hati.kirim_pesan_cinta(pesan)
                    st.success(hasil)
                else:
                    st.warning("Pesan tidak boleh kosong.")

        elif menu == "Lihat Rindu":
            st.info(f"Rindu untuk {nama}: {st.session_state.hati.rindu} kali.")

        elif menu == "Reset":
            if st.button("Reset Semua"):
                st.session_state.hati = None
                st.warning("Hati telah di-reset.")

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
