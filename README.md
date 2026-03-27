# 🌍🤖 Smart Arabic–English Translator

An AI-powered web application that translates text between **Arabic and English** using Hugging Face Transformers and Streamlit.

---

## ✨ Features

- 🔁 Arabic ↔ English translation
- 🤖 Powered by Hugging Face MarianMT models
- 🎨 Beautiful UI with random background images
- ⚡ Fast and lightweight Streamlit web app
- 📥 Download translated text
- 🧹 Clear input option
- 🧠 Clean modular architecture (translator separated from UI)

---
## 📁 Project Structure
project:

│── app.py    # Streamlit UI  
│── translator.py   # Translation logic  
│── requirements.txt   # Dependencies  
│── README.md        # Project documentation  

---
## Create Virtual Environments

python -m venv venv

source venv/bin/activate # Mac/Linux

venv\Scripts\activate      # Windows

---
## Install dependencies
pip install -r requirements.txt

---

## Run the App
 streamlit run app.py
 
---

## 🤖 Models Used

- Arabic → English  
  Helsinki-NLP/opus-mt-ar-en  

- English → Arabic  
  Helsinki-NLP/opus-mt-en-ar  
