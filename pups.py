import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# 🔴 Hintergrund rot machen (CSS)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ff0000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎮 Titel ändern
st.title("🎮 Zocker Modus aktiviert")

# Modell laden  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Titel
st.title("YOLOv8 Objekterkennung mit Streamlit")

# Modell laden (vortrainiert)
@st.cache_resource
def load_model():
    model = YOLO("yolov8n.pt")  # kleines, schnelles Modell
    return model

model = load_model()

# Bild hochladen
uploaded_file = st.file_uploader("Lade ein Bild hoch", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Originalbild", use_column_width=True)

    # In numpy konvertieren
    img_array = np.array(image)

    # YOLO Vorhersage
    results = model(img_array)

    # Ergebnisbild mit Bounding Boxes
    result_img = results[0].plot()

    st.image(result_img, caption="Erkannte Objekte", use_column_width=True)

    # Optional: Labels anzeigen
    st.subheader("Erkannte Klassen:")
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls_id]
        st.write(f"{label} ({conf:.2f})")

Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

# Bild hochladen
uploaded_file = st.file_uploader("Lade ein Bild hoch", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Originalbild", use_container_width=True)

    img_array = np.array(image)

    results = model(img_array)

    result_img = results[0].plot()

    st.image(result_img, caption="Erkannte Objekte", use_container_width=True)

    st.subheader("Erkannte Klassen:")

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls_id]
        st.write(f"{label} ({conf:.2f})")
