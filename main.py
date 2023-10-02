import joblib
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Judul aplikasi
st.title('Prediksi Kelulusan Mahasiswa TI UNTIRTA')

# Masukkin gambar
st.subheader('Keterangan Nilai Bobot Mata Kuliah')
img = Image.open('Nilai Bobot Mata Kuliah.jpg')
st.image(img, use_column_width = True)

# Masukkan Nama
Nama_Lengkap = st.text_input("Nama Lengkap: ")

# Masukkan NIM
NIM = st.number_input("NIM:", min_value=0, max_value=3333999999, value=0)

# Set st.session_state setelah pengguna memasukkan Nama dan NIM
if Nama_Lengkap:
    st.session_state.name = Nama_Lengkap

if NIM:
    st.session_state.age = NIM

SEMESTER_1 = joblib.load('MODEL_SEMESTER1_SVM.pkl')
SEMESTER_2 = joblib.load('MODEL_SEMESTER2_MLP.pkl')
SEMESTER_3 = joblib.load('MODEL_SEMESTER3_KNN.pkl')

# Sidebar for navigation

with st.sidebar:
    selected = option_menu('Prediksi Kelulusan Mahasiswa Teknik Industri UNTIRTA',
                           ['SEMESTER 1', 'SEMESTER 2', 'SEMESTER 3'], default_index=0)

# Diabetes Prediction Page
if (selected == 'SEMESTER 1'):

    # Page title
    st.title('Prediksi Kelulusan Mahasiswa Semester 1 Teknik Industri UNTIRTA')

    Fisika_Dasar_1 = st.selectbox('Fisika Dasar 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_1 = st.selectbox('Kalkulus 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kimia_Dasar = st.selectbox('Kimia Dasar', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Material_Teknik = st.selectbox('Material Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengantar_Teknik_Industri = st.selectbox('Pengantar Teknik Industri', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Menggambar_Teknik = st.selectbox('Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Menggambar_Teknik = st.selectbox('Praktikum Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Logika_Pemrograman = st.selectbox('Logika Pemrograman', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))

    # Code for prediction
    SEMESTER_1_PREDICTION = ''

    # Creating a button for prediction

    if st.button('PREDIKSI KELULUSAN'):
        if 'name' in st.session_state:
            st.write(f"Halo {st.session_state.name}!")

        if 'age' in st.session_state:
            st.write(f"NIM {st.session_state.age}.")

        Fisika_Dasar_1 = float(Fisika_Dasar_1)
        Kalkulus_1 = float(Kalkulus_1)
        Kimia_Dasar = float(Kimia_Dasar)
        Material_Teknik = float(Material_Teknik)
        Pengantar_Teknik_Industri = float(Pengantar_Teknik_Industri)
        Menggambar_Teknik = float(Menggambar_Teknik)
        Praktikum_Menggambar_Teknik = float(Praktikum_Menggambar_Teknik)
        Logika_Pemrograman = float(Logika_Pemrograman)

        SEMESTER_1_prediction = SEMESTER_1.predict([[Fisika_Dasar_1, Kalkulus_1, Kimia_Dasar, Material_Teknik, Pengantar_Teknik_Industri, Menggambar_Teknik, Praktikum_Menggambar_Teknik, Logika_Pemrograman]])

        if SEMESTER_1_prediction[0] == 1:
            SEMESTER_1_PREDICTION = 'LULUS TIDAK TEPAT WAKTU'
            MOTIVASI = (
                'Jangan patah semangat, terus perbaiki nilaimu. Ini baru semester 1 dan harus cepat beradaptasi.'
                'Jika kamu malas dan hanya membuang-buang waktu, kamu tak akan tahu bagaimana cara merengkuh peluang bahkan ketika peluang itu tepat berada di hadapan kamu.')
        else:
            SEMESTER_1_PREDICTION = 'LULUS TEPAT WAKTU'
            MOTIVASI = (
                'Kamu telah melalui lebih dari 20 sks dengan baik. Pertahankan dan tingkatkan kembali nilai-nilai di semester kedepan.'
                'Kamu bisa mengambil lebih dari 20 sks untuk semester 2. Tidak apa-apa untuk merayakan kesuksesan, tapi lebih penting untuk memperhatikan pelajaran tentang kegagalan.')

        pesan_hasil = f'{SEMESTER_1_PREDICTION}, {MOTIVASI}'

        st.success(pesan_hasil)

if (selected == 'SEMESTER 2'):

    # Page title
    st.title('Prediksi Kelulusan Mahasiswa SEMESTER 2 Teknik Industri UNTIRTA')

    Fisika_Dasar_1 = st.selectbox('Fisika Dasar 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_1 = st.selectbox('Kalkulus 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kimia_Dasar = st.selectbox('Kimia Dasar', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Material_Teknik = st.selectbox('Material Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengantar_Teknik_Industri = st.selectbox('Pengantar Teknik Industri', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Menggambar_Teknik = st.selectbox('Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Menggambar_Teknik = st.selectbox('Praktikum Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Logika_Pemrograman = st.selectbox('Logika Pemrograman', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Aljabar_Linear = st.selectbox('Aljabar Linear', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Fisika_Dasar_2 = st.selectbox('Fisika Dasar 2', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_2 = st.selectbox('Kalkulus 2', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Mekanika_Teknik = st.selectbox('Mekanika Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Fisika_Dasar = st.selectbox('Praktikum Fisika Dasar', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Proses_Manufaktur = st.selectbox('Proses Manufaktur', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ekologi_Industri = st.selectbox('Ekologi Industri', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Proses_Manufaktur = st.selectbox('Praktikum Proses Manufaktur', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))

    # Code for prediction
    SEMESTER_2_PREDICTION = ''

    # Creating a button for prediction

    if st.button('PREDIKSI KELULUSAN'):
        if 'name' in st.session_state:
            st.write(f"Halo {st.session_state.name}!")

        if 'age' in st.session_state:
            st.write(f"NIM {st.session_state.age}.")

        Fisika_Dasar_1 = float(Fisika_Dasar_1)
        Kalkulus_1 = float(Kalkulus_1)
        Kimia_Dasar = float(Kimia_Dasar)
        Material_Teknik = float(Material_Teknik)
        Pengantar_Teknik_Industri = float(Pengantar_Teknik_Industri)
        Menggambar_Teknik = float(Menggambar_Teknik)
        Praktikum_Menggambar_Teknik = float(Praktikum_Menggambar_Teknik)
        Logika_Pemrograman = float(Logika_Pemrograman)
        Aljabar_Linear = float(Aljabar_Linear)
        Fisika_Dasar_2 = float(Fisika_Dasar_2)
        Kalkulus_2 = float(Kalkulus_2)
        Mekanika_Teknik = float(Mekanika_Teknik)
        Praktikum_Fisika_Dasar = float(Praktikum_Fisika_Dasar)
        Proses_Manufaktur = float(Proses_Manufaktur)
        Ekologi_Industri = float(Ekologi_Industri)
        Praktikum_Proses_Manufaktur = float(Praktikum_Proses_Manufaktur)

        SEMESTER_2_prediction = SEMESTER_2.predict([[Fisika_Dasar_1, Kalkulus_1, Kimia_Dasar, Material_Teknik, Pengantar_Teknik_Industri,
                                                     Menggambar_Teknik, Praktikum_Menggambar_Teknik, Logika_Pemrograman,
                                                     Aljabar_Linear, Fisika_Dasar_2, Kalkulus_2, Mekanika_Teknik, Praktikum_Fisika_Dasar,
                                                     Proses_Manufaktur, Ekologi_Industri, Praktikum_Proses_Manufaktur]])

        if SEMESTER_2_prediction[0] == 0:
            SEMESTER_2_PREDICTION = 'LULUS TIDAK TEPAT WAKTU'
            MOTIVASI = (
                'Jangan patah semangat, terus perbaiki nilaimu.'
                'Jika kamu malas dan hanya membuang-buang waktu, kamu tak akan tahu bagaimana cara melihat peluang bahkan '
                'ketika peluang itu tepat berada di hadapan kamu. '
                'Bukan nasib yang menentukan hidupmu, tapi kamu sendirilah yang menentukan masa depanmu. '
                'Rasa malas akan menjadi penghalang rezeki dari yang Tuhan berikan')
        else:
            SEMESTER_2_PREDICTION = 'LULUS TEPAT WAKTU'
            MOTIVASI = (
                'Kamu telah melalui lebih dari 20 sks dengan baik. Pertahankan dan tingkatkan kembali nilai-nilai di semester kedepan.'
                'Kamu bisa mengambil lebih dari 20 sks untuk semester 3. Menjadi mahasiswa tidaklah mudah, namun semua bisa dilalui oleh mereka yang semangatnya yang tak akan goyah')

        pesan_hasil = f'{SEMESTER_2_PREDICTION}, {MOTIVASI}'

        st.success(pesan_hasil)

if (selected == 'SEMESTER 3'):

    # Page title
    st.title('Prediksi Kelulusan Mahasiswa SEMESTER 3 Teknik Industri UNTIRTA')

    Fisika_Dasar_1 = st.selectbox('Fisika Dasar 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_1 = st.selectbox('Kalkulus 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kimia_Dasar = st.selectbox('Kimia Dasar', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Material_Teknik = st.selectbox('Material Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengantar_Teknik_Industri = st.selectbox('Pengantar Teknik Industri', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Menggambar_Teknik = st.selectbox('Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Menggambar_Teknik = st.selectbox('Praktikum Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Logika_Pemrograman = st.selectbox('Logika Pemrograman', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Aljabar_Linear = st.selectbox('Aljabar Linear', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Fisika_Dasar_2 = st.selectbox('Fisika Dasar 2', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_2 = st.selectbox('Kalkulus 2', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Mekanika_Teknik = st.selectbox('Mekanika Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Fisika_Dasar = st.selectbox('Praktikum Fisika Dasar', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Proses_Manufaktur = st.selectbox('Proses Manufaktur', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ekologi_Industri = st.selectbox('Ekologi Industri', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Proses_Manufaktur = st.selectbox('Praktikum Proses Manufaktur', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analisis_Biaya = st.selectbox('Analisis Biaya', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Penelitian_Operasional_1 = st.selectbox('Peneletian Operasional 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perencanaan_dan_Pengendalian_Produksi = st.selectbox('Perencanaan dan Pengendalian Produksi', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Sistem_Rantai_Pasok = st.selectbox('Sistem Rantai Pasok', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ergonomi_1 = st.selectbox('Ergonomi 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_3 = st.selectbox('Kalkulus 3', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Statistika_1 = st.selectbox('Statistika 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))

    # Code for prediction
    SEMESTER_3_PREDICTION = ''

    # Creating a button for prediction

    if st.button('PREDIKSI KELULUSAN'):
        if 'name' in st.session_state:
            st.write(f"Halo {st.session_state.name}!")

        if 'age' in st.session_state:
            st.write(f"NIM {st.session_state.age}.")

        Fisika_Dasar_1 = float(Fisika_Dasar_1)
        Kalkulus_1 = float(Kalkulus_1)
        Kimia_Dasar = float(Kimia_Dasar)
        Material_Teknik = float(Material_Teknik)
        Pengantar_Teknik_Industri = float(Pengantar_Teknik_Industri)
        Menggambar_Teknik = float(Menggambar_Teknik)
        Praktikum_Menggambar_Teknik = float(Praktikum_Menggambar_Teknik)
        Logika_Pemrograman = float(Logika_Pemrograman)
        Aljabar_Linear = float(Aljabar_Linear)
        Fisika_Dasar_2 = float(Fisika_Dasar_2)
        Kalkulus_2 = float(Kalkulus_2)
        Mekanika_Teknik = float(Mekanika_Teknik)
        Praktikum_Fisika_Dasar = float(Praktikum_Fisika_Dasar)
        Proses_Manufaktur = float(Proses_Manufaktur)
        Ekologi_Industri = float(Ekologi_Industri)
        Praktikum_Proses_Manufaktur = float(Praktikum_Proses_Manufaktur)
        Analisis_Biaya = float(Analisis_Biaya)
        Penelitian_Operasional_1 = float(Penelitian_Operasional_1)
        Perencanaan_dan_Pengendalian_Produksi = float(Perencanaan_dan_Pengendalian_Produksi)
        Sistem_Rantai_Pasok = float(Sistem_Rantai_Pasok)
        Ergonomi_1 = float(Ergonomi_1)
        Kalkulus_3 = float(Kalkulus_3)
        Statistika_1 = float(Statistika_1)


        SEMESTER_3_prediction = SEMESTER_3.predict([[Fisika_Dasar_1, Kalkulus_1, Kimia_Dasar, Material_Teknik, Pengantar_Teknik_Industri,
                                                     Menggambar_Teknik, Praktikum_Menggambar_Teknik, Logika_Pemrograman,
                                                     Aljabar_Linear, Fisika_Dasar_2, Kalkulus_2, Mekanika_Teknik, Praktikum_Fisika_Dasar,
                                                     Proses_Manufaktur, Ekologi_Industri, Praktikum_Proses_Manufaktur, Analisis_Biaya,
                                                     Penelitian_Operasional_1, Perencanaan_dan_Pengendalian_Produksi, Sistem_Rantai_Pasok,
                                                     Ergonomi_1, Kalkulus_3, Statistika_1]])

        if SEMESTER_3_prediction[0] == 0:
            SEMESTER_3_PREDICTION = 'LULUS TIDAK TEPAT WAKTU'
            MOTIVASI = (
                'Jangan patah semangat, terus perbaiki nilaimu.'
                'Jika tak ingin tertinggal dengan temanmu hilangkan rasa malas, '
                'jadilah orang yang dikagumi karena kesuksesanmu nantinya bukan orang yang direndahkan')
        else:
            SEMESTER_3_PREDICTION = 'LULUS TEPAT WAKTU'
            MOTIVASI = (
                'Kamu telah melalui lebih dari 20 sks dengan baik. Pertahankan dan tingkatkan kembali nilai-nilai di semester kedepan.'
                'Kamu bisa mengambil lebih dari 20 sks untuk semester 4. "Jika kita terus melakukan apa yang kita lakukan, kita juga terus akan mendapatkan apa yang kita dapatkan"')

        pesan_hasil = f'{SEMESTER_3_PREDICTION}, {MOTIVASI}'

        st.success(pesan_hasil)
