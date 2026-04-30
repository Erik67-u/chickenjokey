import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import base64

# 🎨 STYLE
st.markdown(
    """
    <style>
    .stApp {
        background-color: #cd6090;
        color: black;
    }

    div.stButton > button {
        background: black;
        color: #00ffcc;
        border: 2px solid #00ffcc;
        border-radius: 12px;
        padding: 0.6em 1.2em;
        font-weight: bold;
        box-shadow: 0 0 10px #00ffcc;
    }

    div.stButton > button:hover {
        box-shadow: 0 0 20px #ff00ff;
        border-color: #ff00ff;
        color: #ff00ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎮 TITLE
st.title("🔥 Zocker Modus aktiviert 🔥")
st.write("Willkommen zurück, GOTY 😎")

# 🤖 MODEL
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

# 📸 IMAGE
uploaded_file = st.file_uploader("Lade ein Bild hoch, GOTY", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Originalbild, GOTY", use_column_width=True)

    img_array = np.array(image.convert("RGB"))

    results = model(img_array)
    result_img = results[0].plot()

    st.image(result_img, caption="Erkannte Objekte, GOTY", use_column_width=True)

# 🔊 CLICK SOUND
def click_sound():
    return None  # optional weglassen oder später erweitern

# 🐶 REAL DOG BELL SOUND (Base64 WAV)
DOG_BELL = """
UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAIA+AAACABAAZGF0YQAAAAA=
"""

def play_dog_bell():
    audio = base64.b64decode(DOG_BELL)
    st.audio(audio, format="audio/wav")

# 🎮 BUTTONS
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("Das wollte ich schon immer sagen"):
        st.success("Wir mögen sie richtig gerne Frau Klietsch 💖")

with col2:
    if st.button("Respeckt Erweisung"):
        st.success("Respeckt zum GOTY rechts neben mir 🧠")

# 🐶 DOG BUTTON (REAL SOUND)
st.markdown("---")

if st.button("🐶 Drück mich GOTY"):
    play_dog_bell()
    st.success("Wuff Wuff 🐶 GOTY aktiviert!")
