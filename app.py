import streamlit as st

st.title("🚗 Sistem Pengambil Keputusan Kerusakan Mobil")
st.write("Masukkan gejala yang dialami mobil Anda, lalu sistem akan memberikan kemungkinan kerusakan.")

mesin_hidup = st.selectbox("Apakah mesin bisa dihidupkan?", ["Ya", "Tidak"])
bunyi_aneh = st.selectbox("Apakah terdengar bunyi aneh?", ["Ya", "Tidak"])
keluar_asap = st.selectbox("Apakah keluar asap dari knalpot/mesin?", ["Ya", "Tidak"])
oli_bocor = st.selectbox("Apakah ada kebocoran oli di bawah mobil?", ["Ya", "Tidak"])
lampu_check = st.selectbox("Apakah lampu 'Check Engine' menyala?", ["Ya", "Tidak"])

if st.button("Cek Kerusakan"):
    if mesin_hidup == "Tidak":
        if lampu_check == "Ya":
            st.error("⚠️ Kemungkinan masalah pada sistem injeksi atau sensor.")
        else:
            st.error("⚠️ Periksa aki atau starter.")
    elif bunyi_aneh == "Ya":
        st.warning("🔧 Kemungkinan ada masalah pada timing belt atau bagian mesin lain.")
    elif keluar_asap == "Ya":
        st.error("🔥 Kemungkinan overheat atau masalah pada gasket silinder.")
    elif oli_bocor == "Ya":
        st.warning("🛢️ Ada kebocoran oli, segera periksa seal/gasket.")
    else:
        st.success("✅ Tidak terdeteksi masalah serius. Tapi tetap lakukan servis rutin.")
