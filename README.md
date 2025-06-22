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
- Opens a file dialogue to select an image

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

Add a custom message and date

See live preview

Download the final image

---

## ⚙️ Installation
### 🧰 Dependencies
Install with:

```bash
pip install -r requirements.txt
```
---
## Ui Snap
<img src="https://github.com/user-attachments/assets/38757047-c5e3-427d-8d0d-f068794d0c16" alt="UI" width="400" height="300">

## 🧑‍🎨 How to Customise
### ✍️ Caption Font
- Drop your .ttf font in the font/ folder


- Edit the font path in app.py and vintagephoto.py

### 🎨 Style the Web UI
- Modify static/css/styles.css and static/js/script.js

- Optional: Add a dark/light mode toggle

### ⚠️ Known Issues
- Image processing may take a few seconds for large files

- Caption cutoff if too long — keep text short

- Flask version only applies effects after submitting (not live preview)
 
