import streamlit as st
from translator import Translator
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Translator",
    page_icon="🤖",
    layout="centered"
)

# ---------------- BACKGROUND IMAGES ----------------
BACKGROUND_IMAGES = [
    "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5",
    "https://images.unsplash.com/photo-1503264116251-35a269479413",
    "https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17",
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085",
]

def set_bg(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Dark overlay */
        .stApp::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.55);
            z-index: 0;
        }}

        .block-container {{
            position: relative;
            z-index: 1;
        }}

        h1, h2, h3, p, label {{
            color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply random background
set_bg(random.choice(BACKGROUND_IMAGES))

# ---------------- HEADER (ROBOT STYLE) ----------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
        width=140
    )

st.markdown(
    "<h2 style='text-align:center;'>Smart Arabic–English Translator</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>AI-powered translation using Hugging Face 🤖</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Settings")

direction = st.sidebar.selectbox(
    "Translation Direction",
    ["Arabic → English", "English → Arabic"]
)

# ---------------- MODEL SELECTION ----------------
if direction == "Arabic → English":
    model_name = "Helsinki-NLP/opus-mt-ar-en"
else:
    model_name = "Helsinki-NLP/opus-mt-en-ar"

# ---------------- LOAD TRANSLATOR ----------------
@st.cache_resource
def load_translator(model_name):
    return Translator(model_name)

translator = load_translator(model_name)

# ---------------- INPUT ----------------
text = st.text_area(
    "Enter text",
    placeholder="Type or paste your text here...",
    height=150
)

# ---------------- BUTTONS ----------------
col1, col2 = st.columns(2)

with col1:
    translate_btn = st.button("🚀 Translate")

with col2:
    clear_btn = st.button("🧹 Clear")

if clear_btn:
    st.rerun()

# ---------------- TRANSLATION ----------------
if translate_btn:
    if text.strip():
        with st.spinner("Translating... ⏳"):
            output = translator.translate(text)

        st.success("✅ Translation complete!")

        st.markdown("### 🔤 Result")
        st.write(output)

        st.code(output)

        st.download_button(
            "📥 Download Translation",
            output,
            file_name="translation.txt",
            mime="text/plain"
        )

    else:
        st.warning("⚠️ Please enter text!")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit + Hugging Face 🤖")