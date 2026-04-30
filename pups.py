import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import base64
import wave
import io

# 🎨 NEON GAMING STYLE
st.markdown(
    """
    <style>
    .stApp {
        background-color: #cd6090;
        color: black;
        font-family: Arial;
    }

    /* 🔥 Neon Buttons */
    div.stButton > button {
        background: black;
        color: #00ffcc;
        border: 2px solid #00ffcc;
        border-radius: 12px;
        padding: 0.6em 1.2em;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        transform: scale(1.08);
        box-shadow: 0 0 20px #ff00ff, 0 0 40px #ff00ff;
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

# 🤖 YOLO MODEL
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

# 🔊 SIMPLE SOUND GENERATOR (click sound)
def click_sound(freq=700, duration=0.15):
    framerate = 44100
    t = np.linspace(0, duration, int(framerate * duration))
    audio = (np.sin(2 * np.pi * freq * t) * 32767).astype(np.int16)

    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(framerate)
        f.writeframes(audio.tobytes())

    buffer.seek(0)
    return buffer

# 🐶 BELL SOUND (echter kurzer Bark Sound)
def bark_sound():
    framerate = 44100
    duration = 0.35
    t = np.linspace(0, duration, int(framerate * duration))

    # Fake "Wuff" (tiefe + noise mix)
    signal = (
        np.sin(2 * np.pi * 120 * t) * 0.6 +
        np.random.uniform(-0.4, 0.4, len(t))
    )

    audio = (signal * 32767).astype(np.int16)

    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(framerate)
        f.writeframes(audio.tobytes())

    buffer.seek(0)
    return buffer

# 📸 IMAGE UPLOAD
uploaded_file = st.file_uploader("Lade ein Bild hoch, GOTY", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Originalbild, GOTY", use_column_width=True)

    img_array = np.array(image.convert("RGB"))

    results = model(img_array)
    result_img = results[0].plot()

    st.image(result_img, caption="Erkannte Objekte, GOTY", use_column_width=True)

    st.subheader("Erkannte Klassen, GOTY:")
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls_id]
        st.write(f"{label} ({conf:.2f})")

# 🎮 BUTTON AREA
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("Das wollte ich schon immer sagen"):
        st.audio(click_sound(660))
        st.success("Wir mögen sie richtig gerne Frau Klietsch 💖")

with col2:
    if st.button("Respeckt Erweisung"):
        st.audio(click_sound(880))
        st.success("Respeckt zum GOTY rechts neben mir 🧠")

# 🐶 BELL BUTTON
st.markdown("---")

if st.button("🐶 Drück mich GOTY"):
    st.audio(bark_sound())
    st.success("Wuff Wuff 🐶 GOTY detected!")
