import streamlit as st
import pandas as pd
import os

# Konfigurasi Halaman
st.set_page_config(page_title="Toko Anggrek", layout="wide")

# 1. Tampilkan Banner Canva
if os.path.exists("anggrekku.png"):
    st.image("anggrekku.png", use_container_width=True)

st.title("🌸Koleksi Anggrek Berdasarkan Kategori")
st.write("Tempat untuk membeli bunga anggrek dengan kualitas segar alami.")
st.divider()

try:
    if os.path.exists("data_anggrek1.csv"):
        df = pd.read_csv("data_anggrek1.csv")
        df = df.dropna(subset=["foto"])

        daftar_kategori = df["kategori"].unique()

        for kat in daftar_kategori:
            st.header(f"Anggrek Jenis {kat.capitalize()}")
            data_per_kat = df[df["kategori"] == kat]

            cols = st.columns(4)

            for index, row in data_per_kat.reset_index().iterrows():
                nama_foto = str(row["foto"]).strip()

                with cols[index % 4]:
                    if os.path.exists(nama_foto):
                        st.image(nama_foto, use_container_width=True)
                        st.subheader(row["nama"])
                        st.markdown(f"### **Rp {row['harga']:,}**")
                        status = row["status"]
                        st.number_input("Jumlah", value=0, key=f"number_{kat}_{index}")
                        if status == "Tersedia":
                            if st.button("Beli", key=f"beli_{kat}_{index}", type="primary"):
                                st.info("Terimakasih sudah membeli")
                            st.markdown(f"**Stok:** :green[{row['status']}]")
                        else :
                            st.button("Habis", disabled=True, key=f"habis_{kat}_{index}")
                            st.markdown(f"**Stok:** :red[{row['status']}]")
                    else:
                        st.warning(f"Foto {nama_foto} tidak ditemukan")
            st.divider()
    else:
        st.error("File 'data_anggrek1.csv' tidak ditemukan!")

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")

# --- Bagian Kotak Saran ---
st.subheader("Kritik & Saran")
st.text_area("Berikan saran anda")
tombol = st.button("Kirim")
if tombol:
    st.success("Makasih Masukkannya 😉")
st.divider()
kepuasan = st.slider("Tingkat kepuasan anda")
tombol_puas = st.button("Nilai")
if tombol_puas:
    if kepuasan <=50:
        st.success("Mohon maaf atas kekurangan kami 😣")
    else:
        st.success("Semoga bahagia selalu 😆")


# --- BAGIAN KONTAK & ALAMAT (FOOTER) ---
st.write("")  # Memberi ruang kosong
st.write("")

st.subheader("Hubungi Kami")
col_info1, col_info2, col_info3 = st.columns(3)

with col_info1:
    st.markdown("**Alamat Galeri:**")
    st.markdown(" Jl. Simanjuntak no.60, Gondokusuman, Terban, Kota Yogyakarta, Daerah Istimewa Yogyakarta ")

with col_info2:
    # Ganti nomor HP di bawah ini dengan nomor Anda (format 62)
    no_hp = "6282138120493"
    pesan_wa = "Halo, saya tertarik memesan anggrek di katalog Anda."
    link_wa = f"https://wa.me/{no_hp}?text={pesan_wa.replace(' ', '%20')}"

    st.markdown("**WhatsApp:**")
    st.markdown(f"[Pesan Sekarang via WhatsApp]({link_wa})")

with col_info3:
    #Sosmed Kita
    link_ig = f"https://instagram.com/izt.ivn"
    st.markdown("**Akun Sosial Media:**")
    st.markdown(f"[@izt.ivn]({link_ig})")

st.write('')
st.write('')   
st.caption("© 2026 Toko Anggrek Digital Kelompok Satu- Semua Hak Dilindungi")
