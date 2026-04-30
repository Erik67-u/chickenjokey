import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# 🎨 Styling (schwarze Schrift + Hintergrund bleibt wie vorher)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #cd6090;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎮 Titel
st.title("🔥 Zocker Modus aktiviert 🔥")
st.write("Willkommen zurück, GOTY")

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

# 🧠 Buttons
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("Das wollte ich schon immer sagen"):
        st.success("Wir mögen sie richtig gerne Frau Klietsch")

with col2:
    if st.button("Respeckt Erweisung"):
        st.success("Respeckt zum GOTY rechts neben mir")
