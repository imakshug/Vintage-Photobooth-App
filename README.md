# 📸 Vintage Polaroid Photobooth App

A full-featured **vintage photo editor** that transforms modern photos into nostalgic Polaroid-style images. Includes a **Python desktop app** and a **web version built with Flask + HTML/CSS/JS**.

---

## 🔀 Features

- 🎨 Vintage filters (color correction, grain, frame)
- 📝 Add handwritten-style caption & date
- 🖼️ Export Polaroid image automatically to `exports/` folder
- 💻 Python GUI (Tkinter) + Web UI (Flask)
- 🔢 Auto-numbered export filenames
- 🎚️ Clean and aesthetic font (handwritten style)
- 🌗 Dark/Light mode toggle for web version (optional)

---

## 📁 Folder Structure
```bash 
Vintage-Photobooth-App/
│
├── app/ ← Flask app
│ ├── static/
│ │ ├── css/
│ │ │ └── styles.css
│ │ └── js/
│ │ └── script.js
│ ├── templates/
│ │ └── index.html
│ ├── uploads/ ← Uploaded original images
│ ├── processed/ ← Output images with effects
│ ├── font/ ← Custom TTF font for captions
│ └── app.py ← Flask server
│
├── desktop_version/
│ ├── vintagephoto.py ← Main Python script
│ ├── Kapakana-VariableFont_wght.ttf
│ └── exports/ ← Saved images
│
├── README.md
└── requirements.txt
```
---

## 💻 1. Desktop App (Tkinter)

### ▶️ Run It

```bash
python vintagephoto.py
```

✅ What It Does
- Opens a file dialog to select an image

- Prompts for caption + date

- Applies vintage effects, adds frame & text

- Saves final result as photo_001.jpg, photo_002.jpg... in exports/

## 🌐 2. Web App (Flask + HTML/CSS/JS)
### ▶️ Run the Web Version

```bash
cd app/
python app.py
```
Then open:
http://127.0.0.1:5000

✅ What It Offers
Upload image via browser

Add custom message and date

See live preview

Download final image

---

## ⚙️ Installation
### 🧰 Dependencies
Install with:

```bash
pip install -r requirements.txt
```
