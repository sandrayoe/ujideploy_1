from jsonschema import draft4_format_checker
import streamlit as st
import lorem
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 

st.title("Judul Belum Tau")
st.subheader("blm tau juga")
st.write(lorem.paragraph())

#Korelasi rokok, pendidikan, dan tingkat pendidikan
st.subheader("Kenapa ya, banyak yang merokok?")
st.write(lorem.paragraph())

df3 = pd.read_excel("Pendidikan_pertahun.xlsx")

fig1, ax1 = plt.subplots(figsize=(10,10))
graph1 = sns.regplot (
    data=df3,
    x='Perokok2_3',
    y='Kombinasi_3',
    ax = ax1 
)
#graph.set_xlim(left=0, right=500000)
#graph.set_ylim(bottom=0, top=500000000000)
st.pyplot(fig1)

fig2, ax2 = plt.subplots(figsize=(10,10))
graph2 = sns.regplot (
    data=df3,
    x='Perokok2_3',
    y='SMA2_3',
    ax = ax2 
)
#graph.set_xlim(left=0, right=500000)
#graph.set_ylim(bottom=0, top=500000000000)
st.pyplot(fig2)

fig3, ax3 = plt.subplots(figsize=(10,10))
graph3 = sns.regplot (
    data=df3,
    x='Perokok2_3',
    y='Miskin2_3',
    ax = ax3 
)
#graph.set_xlim(left=0, right=500000)
#graph.set_ylim(bottom=0, top=500000000000)
st.pyplot(fig3)

correlation1 = df3['Kombinasi_3'].corr(df3['Perokok2_3'])
st.write(correlation1)
correlation2 = df3['SMA2_3'].corr(df3['Perokok2_3'])
st.write(correlation2)
correlation3 = df3['Miskin2_3'].corr(df3['Perokok2_3'])
st.write(correlation3)

df5 = pd.read_excel("Pengeluaran_2.xlsx")
st.write(df5)

bar_fig1 = plt.figure(figsize=(20,20))
bar_ax1 = bar_fig1.add_subplot(111)

data_df2 = df5[["pengeluaran_total", "pengeluaran_makanan", "rokok_2"]]
data_df2.plot.bar(alpha=0.8, ax=bar_ax1, title="Average Measurements per Tumor Type")
st.pyplot(bar_fig1)

bar_fig2 = plt.figure(figsize=(20,20))
bar_ax2 = bar_fig2.add_subplot(111)

data_df3 = df5[["pengeluaran_sebulan", "makanan", "rokok_sebulan"]]
data_df3.plot.bar(alpha=0.8, ax=bar_ax2, title="Average Measurements per Tumor Type")
st.pyplot(bar_fig2)


df6 = pd.read_excel("Persentase Merokok Pada Penduduk Umur ≥ 15 Tahun Menurut Kelompok Umur.xlsx")
fig6, ax6 = plt.subplots(figsize=(20,20))
graph4 = sns.barplot (
    data=df6, 
    x='Umur',
    y='2021',
    ax = ax6
)
st.pyplot(fig6)