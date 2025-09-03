
import streamlit as st

st.set_page_config(page_title="Honda Car Diagnostic", page_icon="🚗", layout="centered")

# === HEADER ===
st.title("🚗 Sistem Diagnosis Kerusakan Mobil Honda")
st.write("Aplikasi ini membantu menganalisa kerusakan umum pada mobil Honda berdasarkan gejala yang kamu alami.")

# === IDENTITAS MOBIL ===
st.header("📌 Data Kendaraan")

tipe = st.selectbox("Pilih tipe mobil Honda:", [
    "Brio", "Jazz", "Civic", "Accord", "HR-V", "CR-V", "BR-V", "Mobilio", "City", "Odyssey"
])
tahun = st.number_input("Masukkan tahun produksi:", min_value=1990, max_value=2025, value=2015)
transmisi = st.radio("Jenis transmisi:", ["Manual", "Automatic / CVT"])

st.markdown("---")

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
        "Suspensi & Kemudi",
        "Sistem AC"
    ]
)

diagnosa = ""

# === MESIN ===
if kategori == "Mesin":
    mesin_hidup = st.selectbox("Apakah mesin sulit dihidupkan?", ["Tidak", "Ya"])
    mesin_mati = st.selectbox("Apakah mesin sering mati mendadak?", ["Tidak", "Ya"])
    bunyi_aneh = st.selectbox("Apakah terdengar bunyi ketukan/aneh?", ["Tidak", "Ya"])
    asap = st.selectbox("Apakah ada asap berlebihan dari knalpot?", ["Tidak", "Ya"])
    getar = st.selectbox("Apakah mesin terasa bergetar berlebihan?", ["Tidak", "Ya"])
    bbm = st.selectbox("Apakah konsumsi bahan bakar boros?", ["Tidak", "Ya"])

    if st.button("🔍 Analisa Mesin"):
        if mesin_hidup == "Ya":
            diagnosa = "⚠️ Cek aki, busi, atau sistem bahan bakar."
        elif mesin_mati == "Ya":
            diagnosa = "⚠️ Sensor CKP, pompa bensin, atau throttle body bermasalah."
        elif bunyi_aneh == "Ya":
            diagnosa = "⚠️ Klep longgar, timing belt aus, atau piston bermasalah."
        elif asap == "Ya":
            diagnosa = "⚠️ Asap putih → gasket silinder bocor. Asap hitam → campuran bahan bakar kaya."
        elif getar == "Ya":
            diagnosa = "⚠️ Engine mounting lemah atau koil pengapian rusak."
        elif bbm == "Ya":
            diagnosa = "⚠️ Injektor kotor atau sensor O2 rusak."
        else:
            diagnosa = "✅ Mesin normal."

# === TRANSMISI ===
elif kategori == "Transmisi":
    susah_gigi = st.selectbox("Apakah perpindahan gigi terasa kasar?", ["Tidak", "Ya"])
    slip = st.selectbox("Apakah terasa slip saat akselerasi?", ["Tidak", "Ya"])
    oli_bocor = st.selectbox("Apakah ada kebocoran oli transmisi?", ["Tidak", "Ya"])
    getar = st.selectbox("Apakah terasa hentakan/getaran saat perpindahan gigi?", ["Tidak", "Ya"])

    if st.button("🔍 Analisa Transmisi"):
        if susah_gigi == "Ya":
            diagnosa = "⚠️ Sinkronisasi transmisi aus atau oli transmisi kurang."
        elif slip == "Ya":
            diagnosa = "⚠️ Kampas kopling (manual) atau torque converter (matic) bermasalah."
        elif oli_bocor == "Ya":
            diagnosa = "⚠️ Seal transmisi/gasket bocor."
        elif getar == "Ya":
            diagnosa = "⚠️ Pressure solenoid (CVT) atau kopling hidrolik bermasalah."
        else:
            diagnosa = "✅ Transmisi normal."

# === SISTEM LISTRIK ===
elif kategori == "Sistem Listrik":
    lampu = st.selectbox("Apakah lampu redup/sering mati?", ["Tidak", "Ya"])
    aki = st.selectbox("Apakah aki sering soak?", ["Tidak", "Ya"])
    indikator = st.selectbox("Apakah lampu indikator error sering muncul?", ["Tidak", "Ya"])
    starter = st.selectbox("Apakah starter mesin lemah?", ["Tidak", "Ya"])

    if st.button("🔍 Analisa Listrik"):
        if lampu == "Ya":
            diagnosa = "⚠️ Alternator lemah atau kabel massa bermasalah."
        elif aki == "Ya":
            diagnosa = "⚠️ Aki soak atau sistem pengisian tidak normal."
        elif indikator == "Ya":
            diagnosa = "⚠️ Sensor/ECU perlu dicek dengan OBD2."
        elif starter == "Ya":
            diagnosa = "⚠️ Dinamo starter lemah atau relay rusak."
        else:
            diagnosa = "✅ Sistem listrik normal."

# === SISTEM PENDINGIN ===
elif kategori == "Sistem Pendingin":
    overheat = st.selectbox("Apakah mesin sering overheat?", ["Tidak", "Ya"])
    coolant_bocor = st.selectbox("Apakah air radiator/coolant sering habis?", ["Tidak", "Ya"])
    kipas = st.selectbox("Apakah kipas radiator tidak berfungsi?", ["Tidak", "Ya"])
    bau = st.selectbox("Apakah ada bau coolant dalam kabin?", ["Tidak", "Ya"])

    if st.button("🔍 Analisa Pendingin"):
        if overheat == "Ya":
            diagnosa = "⚠️ Radiator, thermostat, atau pompa air rusak."
        elif coolant_bocor == "Ya":
            diagnosa = "⚠️ Selang radiator bocor atau gasket kepala silinder rusak."
        elif kipas == "Ya":
            diagnosa = "⚠️ Motor kipas mati atau relay kipas rusak."
        elif bau == "Ya":
            diagnosa = "⚠️ Heater core bocor."
        else:
            diagnosa = "✅ Sistem pendingin normal."

# === SISTEM REM ===
elif kategori == "Sistem Rem":
    rem_bl = st.selectbox("Apakah pedal rem terasa blong?", ["Tidak", "Ya"])
    bunyi_rem = st.selectbox("Apakah terdengar bunyi berdecit saat rem?", ["Tidak", "Ya"])
    getar_rem = st.selectbox("Apakah terasa getaran saat pengereman?", ["Tidak", "Ya"])
    oli_rem = st.selectbox("Apakah minyak rem sering berkurang?", ["Tidak", "Ya"])

    if st.button("🔍 Analisa Rem"):
        if rem_bl == "Ya":
            diagnosa = "⚠️ Master rem atau booster rusak."
        elif bunyi_rem == "Ya":
            diagnosa = "⚠️ Kampas rem aus."
        elif getar_rem == "Ya":
            diagnosa = "⚠️ Disc brake tidak rata."
        elif oli_rem == "Ya":
            diagnosa = "⚠️ Ada kebocoran pada sistem rem."
        else:
            diagnosa = "✅ Sistem rem normal."

# === SUSPENSI & KEMUDI ===
elif kategori == "Suspensi & Kemudi":
    bunyi = st.selectbox("Apakah ada bunyi saat melewati jalan rusak?", ["Tidak", "Ya"])
    setir_berat = st.selectbox("Apakah setir terasa berat?", ["Tidak", "Ya"])
    ban_aus = st.selectbox("Apakah ban aus tidak merata?", ["Tidak", "Ya"])
    olips = st.selectbox("Apakah ada kebocoran oli power steering?", ["Tidak", "Ya"])

    if st.button("🔍 Analisa Suspensi & Kemudi"):
        if bunyi == "Ya":
            diagnosa = "⚠️ Ball joint, bushing, atau shockbreaker rusak."
        elif setir_berat == "Ya":
            diagnosa = "⚠️ Oli power steering kurang atau motor EPS lemah."
        elif ban_aus == "Ya":
            diagnosa = "⚠️ Perlu spooring & balancing."
        elif olips == "Ya":
            diagnosa = "⚠️ Seal rack steering bocor."
        else:
            diagnosa = "✅ Suspensi & kemudi normal."

# === SISTEM AC ===
elif kategori == "Sistem AC":
    dingin = st.selectbox("Apakah AC tidak dingin?", ["Tidak", "Ya"])
    blower = st.selectbox("Apakah hembusan blower lemah?", ["Tidak", "Ya"])
    bau = st.selectbox("Apakah AC mengeluarkan bau tidak sedap?", ["Tidak", "Ya"])
    bunyi = st.selectbox("Apakah terdengar bunyi berisik saat AC hidup?", ["Tidak", "Ya"])
    clutch = st.selectbox("Apakah kompresor tidak aktif (magnetic clutch tidak nyala)?", ["Tidak", "Ya"])
    kipas_ac = st.selectbox("Apakah kipas AC tidak berfungsi?", ["Tidak", "Ya"])

    if st.button("🔍 Analisa AC"):
        if dingin == "Ya":
            diagnosa = "⚠️ Freon habis/bocor, kondensor kotor, atau kompresor lemah."
        elif blower == "Ya":
            diagnosa = "⚠️ Motor blower lemah atau filter kabin kotor."
        elif bau == "Ya":
            diagnosa = "⚠️ Evaporator kotor atau jamur pada saluran AC."
        elif bunyi == "Ya":
            diagnosa = "⚠️ Kompresor aus atau tensioner belt longgar."
        elif clutch == "Ya":
            diagnosa = "⚠️ Magnetic clutch AC rusak atau relay AC mati."
        elif kipas_ac == "Ya":
            diagnosa = "⚠️ Fan AC mati atau relay fan rusak."
        else:
            diagnosa = "✅ Sistem AC normal."

# === HASIL ===
if diagnosa:
    st.subheader("📋 Hasil Analisa")
    st.info(f"**Mobil Honda {tipe} ({tahun}, {transmisi})**\n\n{diagnosa}")
