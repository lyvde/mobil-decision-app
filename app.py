import streamlit as st

st.set_page_config(page_title="Honda Car Diagnostic", page_icon="🚗", layout="centered")

st.title("🚗 Sistem Diagnosis Kerusakan Mobil Honda")
st.write("Pilih gejala yang kamu alami, lalu sistem akan mencoba menebak kemungkinan kerusakan berdasarkan pengalaman umum pada mobil Honda.")

# === INPUT GEJALA ===
st.header("🔎 Masukkan Gejala")

kategori = st.selectbox(
    "Pilih kategori gejala:",
    [
        "Mesin",
        "Transmisi",
        "Sistem Listrik",
        "Sistem Pendingin",
        "Sistem Rem",
        "Suspensi & Kemudi"
    ]
)

diagnosa = ""

if kategori == "Mesin":
    mesin_hidup = st.selectbox("Apakah mesin sulit dihidupkan?", ["Tidak", "Ya"])
    mesin_mati = st.selectbox("Apakah mesin sering mati mendadak?", ["Tidak", "Ya"])
    bunyi_aneh = st.selectbox("Apakah terdengar bunyi ketukan/aneh?", ["Tidak", "Ya"])
    asap = st.selectbox("Apakah ada asap berlebihan dari knalpot?", ["Tidak", "Ya"])
    getar = st.selectbox("Apakah mesin terasa bergetar berlebihan?", ["Tidak", "Ya"])

    if st.button("🔍 Analisa Mesin"):
        if mesin_hidup == "Ya":
            diagnosa = "⚠️ Kemungkinan masalah pada **aki, busi, atau sistem bahan bakar**."
        elif mesin_mati == "Ya":
            diagnosa = "⚠️ Cek **sensor CKP, pompa bensin, atau throttle body**."
        elif bunyi_aneh == "Ya":
            diagnosa = "⚠️ Bisa jadi **klep longgar, timing belt aus, atau piston bermasalah**."
        elif asap == "Ya":
            diagnosa = "⚠️ Asap putih → **gasket silinder bocor**, Asap hitam → **campuran bahan bakar terlalu kaya**."
        elif getar == "Ya":
            diagnosa = "⚠️ Periksa **engine mounting atau koil pengapian**."
        else:
            diagnosa = "✅ Tidak ada gejala mesin serius terdeteksi."

elif kategori == "Transmisi":
    susah_gigi = st.selectbox("Apakah perpindahan gigi terasa kasar?", ["Tidak", "Ya"])
    slip = st.selectbox("Apakah terasa slip saat akselerasi?", ["Tidak", "Ya"])
    oli_bocor = st.selectbox("Apakah ada kebocoran oli transmisi?", ["Tidak", "Ya"])

    if st.button("🔍 Analisa Transmisi"):
        if susah_gigi == "Ya":
            diagnosa = "⚠️ Kemungkinan sinkronisasi transmisi aus atau oli transmisi kurang."
        elif slip == "Ya":
            diagnosa = "⚠️ Periksa **kampas kopling (manual)** atau **torque converter (matic)**."
        elif oli_bocor == "Ya":
            diagnosa = "⚠️ Ada kebocoran di **seal transmisi atau gasket**."
        else:
            diagnosa = "✅ Transmisi normal."

elif kategori == "Sistem Listrik":
    lampu = st.selectbox("Apakah lampu redup/sering mati?", ["Tidak", "Ya"])
    aki = st.selectbox("Apakah aki sering soak?", ["Tidak", "Ya"])
    indikator = st.selectbox("Apakah lampu indikator error sering muncul?", ["Tidak", "Ya"])

    if st.button("🔍 Analisa Listrik"):
        if lampu == "Ya":
            diagnosa = "⚠️ Alternator lemah atau kabel massa bermasalah."
        elif aki == "Ya":
            diagnosa = "⚠️ Aki soak, perlu diganti atau sistem pengisian tidak optimal."
        elif indikator == "Ya":
            diagnosa = "⚠️ Kemungkinan masalah sensor/ECU, perlu scanner OBD2."
        else:
            diagnosa = "✅ Sistem listrik normal."

elif kategori == "Sistem Pendingin":
    overheat = st.selectbox("Apakah mesin sering overheat?", ["Tidak", "Ya"])
    coolant_bocor = st.selectbox("Apakah air radiator/coolant sering habis?", ["Tidak", "Ya"])
    kipas = st.selectbox("Apakah kipas radiator tidak berfungsi?", ["Tidak", "Ya"])

    if st.button("🔍 Analisa Pendingin"):
        if overheat == "Ya":
            diagnosa = "⚠️ Cek **radiator, thermostat, atau pompa air**."
        elif coolant_bocor == "Ya":
            diagnosa = "⚠️ Ada kebocoran di selang radiator atau gasket kepala silinder."
        elif kipas == "Ya":
            diagnosa = "⚠️ Kemungkinan motor kipas mati atau relay rusak."
        else:
            diagnosa = "✅ Sistem pendingin normal."

elif kategori == "Sistem Rem":
    rem_bl = st.selectbox("Apakah pedal rem terasa blong?", ["Tidak", "Ya"])
    bunyi_rem = st.selectbox("Apakah terdengar bunyi berdecit saat rem?", ["Tidak", "Ya"])
    getar_rem = st.selectbox("Apakah terasa getaran saat pengereman?", ["Tidak", "Ya"])

    if st.button("🔍 Analisa Rem"):
        if rem_bl == "Ya":
            diagnosa = "⚠️ Kemungkinan **kebocoran minyak rem atau master rem bermasalah**."
        elif bunyi_rem == "Ya":
            diagnosa = "⚠️ Kampas rem aus, perlu diganti."
        elif getar_rem == "Ya":
            diagnosa = "⚠️ Disc brake (piringan) tidak rata atau bengkok."
        else:
            diagnosa = "✅ Sistem rem normal."

elif kategori == "Suspensi & Kemudi":
    bunyi = st.selectbox("Apakah ada bunyi saat melewati jalan rusak?", ["Tidak", "Ya"])
    setir_berat = st.selectbox("Apakah setir terasa berat?", ["Tidak", "Ya"])
    ban_aus = st.selectbox("Apakah ban aus tidak merata?", ["Tidak", "Ya"])

    if st.button("🔍 Analisa Suspensi & Kemudi"):
        if bunyi == "Ya":
            diagnosa = "⚠️ Periksa **ball joint, bushing, atau shockbreaker**."
        elif setir_berat == "Ya":
            diagnosa = "⚠️ Power steering bermasalah (oli kurang atau motor EPS lemah)."
        elif ban_aus == "Ya":
            diagnosa = "⚠️ Spooring/camber tidak presisi, perlu alignment."
        else:
            diagnosa = "✅ Suspensi & kemudi normal."

# === HASIL ===
if diagnosa:
    st.subheader("📋 Hasil Analisa")
    st.info(diagnosa)
