import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Загрузка модели
model = LinearRegression()
# model.fit(X_train, y_train)
# joblib.dump(model, 'your_model.pkl')
loaded_model = joblib.load('/Users/test/Desktop/проект2/работает/your_model.pkl')

# Интерфейс для загрузки файла
st.title("Оценка стоимости недвижимости")
st.write("Загрузите файл с фичами для получения оценки стоимости")

uploaded_file = st.file_uploader("Выберите файл", type=["csv"])

if uploaded_file is not None:
    # Чтение загруженного файла
    input_data = pd.read_csv(uploaded_file)
    
    # Отображение загруженных данных
    st.write("Загруженные данные:")
    st.write(input_data)
    
     # Предсказание
    predictions = loaded_model.predict(input_data)
    
    # Отображение предсказаний
    st.write("Предсказания стоимости:")
    st.write(predictions)

