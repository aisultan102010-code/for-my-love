import streamlit as st
import time

# 1. Настройка страницы (вкладка в браузере)
st.set_page_config(page_title="Нашей годовщине ❤️", page_icon="🌹")

# 2. Стилизация (немного магии CSS внутри Python)
st.markdown("""
    <style>
    .main {
        background-color: #fff5f5;
    }
    h1 {
        color: #d63384;
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Контент
st.title("С годовщиной, любимая! ❤️")

# Секция с фото (замени 'photo.jpg' на свое фото)
# st.image("photo.jpg", use_column_width=True)

st.write("---")

# Таймер (сколько вы вместе)
# В реальности здесь нужно посчитать разницу между датой начала и сейчас
st.subheader("Наши дни вместе:")
st.metric(label="Дней счастья", value="365") 

st.write("---")

# Комплименты в виде красивых блоков
st.subheader("Почему ты — моё всё: ✨")

col1, col2 = st.columns(2)

with col1:
    st.info("🌟 Твоя улыбка меняет мой мир.")
    st.info("🎨 Твоя креативность не знает границ.")

with col2:
    st.info("🧸 С тобой я чувствую себя дома.")
    st.info("👑 Ты самая добрая душа.")

st.write("---")

# Интерактив: Кнопка-сюрприз
if st.button('Нажми, чтобы получить поцелуй 💋'):
    st.balloons()
    st.snow() # Эффект падающего снега/блесток
    st.success("Ты — лучшее, что со мной случилось! Я тебя люблю!")
    time.sleep(2)
    st.write("💌 *Твое маленькое послание здесь*")
