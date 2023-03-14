import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

dataset = pd.read_csv('../template_data.csv')
st.title('Data Visualization')
st.dataframe(dataset)

st.title('Số lượng giao dịch tổng')
fig1 = plt.figure(figsize=(15, 5))
sns.countplot(x=dataset["Số lượng giao dịch tổng"])
st.pyplot(fig1)

st.title('Số lần quá hạn <11 ngày')
fig2 = plt.figure(figsize=(15, 5))
sns.countplot(x=dataset["Số lần quá hạn <11 ngày"])
st.pyplot(fig2)

st.title('Trạng thái nợ')
fig3 = plt.figure(figsize=(15, 5))
sns.countplot(x=dataset["Trạng thái nợ"])
st.pyplot(fig3)
