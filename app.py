import pickle
import streamlit as st
import numpy as np

# Membaca model
model = pickle.load(open('model.sav', 'rb'))

# Judul web
st.title('Prediksi Penyakit Jantung')

# Input data
age = st.text_input('Usia')
trtbps = st.text_input('Tekanan Darah')
chol = st.text_input('Kolesterol')
thalachh = st.text_input('Detak Jantung Maksimal')
exng = st.text_input('Angina yang Diinduksi oleh Latihan (0 = Tidak, 1 = Ya)')
oldpeak = st.text_input('Depresi ST Induced')

prediksi = ''

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Konversi input menjadi numerik
        inputs = np.array([[float(age), float(trtbps), float(chol), float(thalachh),
                            float(exng), float(oldpeak)]])
        # Lakukan prediksi
        hasil_prediksi = model.predict(inputs)
        
        if hasil_prediksi[0] == 1:
            prediksi = 'Terkena Penyakit Hati'
            st.success(prediksi)
        else:
            prediksi = 'Tidak Terkena Penyakit Hati'
            st.markdown(f'<span style="color:red">{prediksi}</span>', unsafe_allow_html=True)
    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
