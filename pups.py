import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# 🎨 Styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #cd6090;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎮 Titel
st.title("🔥 Zocker Modus aktiviert 🔥")
st.write("Willkommen zurück, GOTY 😎")

# Modell laden
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

# 📸 Upload
uploaded_file = st.file_uploader("Lade ein Bild hoch, GOTY", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
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

# 🧨 Button
st.markdown("---")

if st.button("Drück mich, GOTY"):
    st.success("Wuff Wuff 🐶")
    st.write("Signal empfangen, GOTY! 🔥")
