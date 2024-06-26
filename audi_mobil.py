import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil_audi.sav', 'rb'))

st.title('Estimasi Harga Mobil Audi Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')


predict = ''

if if st.button('Estimasi Harga'):
	predict = model.predict(
		[[year, mileage, tax, mpg, engineSize]]
		)
	st.write('Estimasi Harga Mobil Audi Bekas dalam Euro : ', predict)
	st.write('Estimasi Harga Mobil Audi dalam IDR (Juta) : ', predict*18000)