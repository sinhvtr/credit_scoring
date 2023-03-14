import pickle
import streamlit as st

lr_model = pickle.load(open('lr_model.pkl', 'rb'))
svc_model = pickle.load(open('svc_model.pkl', 'rb'))
nb_model = pickle.load(open('nb_model2.pkl', 'rb'))

st.title('Risk Prediction')
genre = st.radio(
    "Giới tính",
    ('Nam', 'Nữ'))
if genre == 'Nam':
    genre_value = 0
else:
    genre_value = 1

num_transactions = st.slider('Số lượng giao dịch tổng', min_value=0, max_value=15)
request_amount = st.slider('Số tiền yêu cầu', min_value=0, max_value=10000000)
salary = st.slider('Mức lương', min_value=0, max_value=10000000)
working_time = st.slider('Thâm niên', min_value=0, max_value=30)
working_status = st.radio(
    "Trạng thái làm việc",
    ('Đang làm việc', 'Đã nghỉ'))
if working_status == 'Đang làm việc':
    working_status_value = 0
else:
    working_status_value = 1

marriage_status = st.radio(
    "Trạng thái hôn nhân",
    ('Đã kết hôn', 'Độc thân'))
if marriage_status == 'Đang làm việc':
    marriage_status_value = 0
else:
    marriage_status_value = 1

num_qua_han = st.slider('Số lần quá hạn <11 ngày', min_value=0, max_value=10)
num_dependants = st.slider('Số người phụ thuộc', min_value=0, max_value=10)

X_new = [genre_value, num_transactions, request_amount, salary, working_time, working_status_value, marriage_status_value, num_qua_han, num_dependants]

st.title('Dự đoán khả năng trả nợ')
result = lr_model.predict([X_new])
st.write(result)
result_proba = lr_model.predict_proba([X_new])
st.write(result_proba)
