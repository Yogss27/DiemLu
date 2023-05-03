import streamlit as st

st.header(':violet[Ini Aplikasi kalkulator penjumlahan]')
st.subheader('silakan input angka numerik yang ingin dihitung')

number1 = st.number_input('Masukkan bilangan pertama')
st.write(f'Bilangan pertama adalah {number1}')

number2 = st.number_input('Masukkan bilangan kedua')
st.write(f'Bilangan kedua adalah {number2}')

if st.button('hitung'):
	hasil = number1+number2
	st.success(f'hasil penjumlahan dari {number1}+{number2}={hasil}', icon="✅")
	st.snow()
else:
    st.write('tekan tombol"hitung"')