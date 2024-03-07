import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Read data from CSV file
days_df = pd.read_csv('daysdata.csv')
days_df['season'] = days_df.season.astype('category')
season_df = days_df.season.replace((1,2,3,4), ('Spring', 'Summer', 'Fall', 'Winter'))
year_df = days_df.yr.replace((0,1), (2011,2012))
days_df['windspeed'] = days_df['windspeed'].apply(lambda x: x * 67)
days_df['temp'] = days_df['temp'].apply(lambda x: x * 41)
Counts_df = days_df.groupby(by="season")['cnt'].sum().sort_values(ascending=False)
Wind_speed_df = days_df.groupby(by="season")['windspeed'].mean().sort_values(ascending=False)
Temperature_df = days_df.groupby(by="season")['temp'].mean().sort_values(ascending=False)

# Set sidebar
with st.sidebar:
    st.subheader('Halo, Selamat Datang di Website Kami.')
    st.subheader('Dalam website ini, kami akan menyajikan hasil data penyewaan sepeda di tahun 2011 dan 2012')
    st.image('https://raw.githubusercontent.com/zimsky29/Zimuth-Project/main/bike.jpg')
    name = st.text_input(label='Siapa nama mu?', value='')
    st.write('Halo: ', name, 'Semoga website ini membantu')

# Set Visualization
"""
Muhammad Azimuthal Hikam
Bangkit Academy Cohort 2024
"""
st.image('https://raw.githubusercontent.com/zimsky29/Zimuth-Project/main/logo.png', width=700)

with st.expander("Apa itu Bike-Sharing"):
    st.write(
        """Bike sharing, juga dikenal sebagai bike rental, adalah konsep transportasi
        yang memungkinkan individu untuk menyewa sepeda untuk digunakan dalam perjalanan
        singkat. Biasanya, sistem bike sharing melibatkan stasiun pengambilan dan pengembalian
        sepeda yang tersebar di seluruh area perkotaan. Pengguna dapat menyewa sepeda dari
        stasiun yang ada, menggunakan sepeda tersebut untuk melakukan perjalanan, dan kemudian
        mengembalikannya ke stasiun lain yang terletak di tempat tujuan mereka."""
    )

st.subheader('Tingkat penyewaan sepeda pada tahun 2011 dan 2012')
fig, ax = plt.subplots(figsize=(10,5))
custom_palette = sns.color_palette(["#FFBF00", "#6495ED"])
sns.barplot(x=season_df , y='cnt', data=days_df, hue=year_df, errorbar=None, palette=custom_palette, ax=ax)
plt.xlabel("Musim")
plt.ylabel("Jumlah tingkat penyewaan")
plt.title("Jumlah Penyewaan Sepeda pada Tahun 2011 dan 2012 di tiap musim")
st.pyplot(fig)

st.markdown("\n")

st.subheader('Nilai rata-rata kecepatan angin pada tiap musim di tahun 2011 dan 2012')
data = Wind_speed_df
keys = ['Spring', 'Summer', 'Fall', 'Winter'] 
palette_color = sns.color_palette('bright') 
fig, ax = plt.subplots()
plt.pie(data, labels=keys, colors=palette_color, autopct='%.1f%%')   
st.pyplot(fig)

st.markdown("\n")

st.subheader('Nilai rata-rata temperatur pada tiap musim di tahun 2011 dan 2012')
data = Temperature_df
keys = ['Spring', 'Summer', 'Fall', 'Winter'] 
palette_color = sns.color_palette('bright') 
fig, ax = plt.subplots()
plt.pie(data, labels=keys, colors=palette_color, autopct='%.1f%%') 
st.pyplot(fig)

st.markdown("\n")

st.subheader("Conclusion")

"""
1 Conclusion Pertanyaan 1: Pada musim apa tingkat penyewaan sepeda tertinggi dan terendah?
- Pada tahun 2011 dan 2012, jumlah penyewaan sepeda tertinggi terjadi pada musim gugur (Fall) dan jumlah penyewaan sepeda terendah terjadi pada musim semi (Spring).

2 Conclusion Pertanyaan 2: Pada musim apa nilai rata-rata kecepataan angin tertinggi dan terendah?
- Berdasarkan nilai rata-rata kecepatan angin di tahun 2011 dan 2012, nilai tertinggi pada musim semi (Spring). Sedangkan nilai terendahnya pada musim salju (Winter) dan musim gugur (Fall).

3 Conclusion Pertanyaan 3: Pada musim apa nilai rata-rata temperatur tertinggi dan terendah?
- Berdasarkan nilai rata-rata temperatur di tahun 2011 dan 2012, nilai tertinggi pada musim semi (Spring). Sedangkan nilai terendahnya pada musim salju (Winter).

4 Conclusion Tambahan:
- Hasil nilai jumlah penyewaan sepeda tertinggi dan terendah dari tiap musim, dipengaruhi oleh nilai rata-rata dari kecepatan angin dan temeperatur.
"""
