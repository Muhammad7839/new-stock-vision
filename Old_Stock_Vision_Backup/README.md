# 📈 Stock Vision

**Stock Vision** is a beginner-friendly AI project that predicts stock and cryptocurrency prices using real-time sentiment analysis from news and social media.

## 📂 Project Structure

Stock-Vision/
├── backend/          # Flask backend with ML + sentiment models
│   ├── app.py
│   ├── requirements.txt
│   └── model/
│       ├── price_predictor.py
│       └── sentiment_model.py
├── frontend/         # HTML/CSS/JS frontend UI
│   ├── index.html
│   ├── script.js
│   └── style.css
├── .gitignore
└── README.md

---

## 🚀 How to Run Locally

### 📌 Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py

🌐 Frontend Setup
	1.	Open frontend/index.html in VS Code
	2.	Right-click → “Open with Live Server”

Live page will load in your browser.

---

### 📄 `.gitignore`

```txt
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.env
.venv/
env/
venv/

# Mac OS
.DS_Store

# Node (if frontend uses any npm in future)
node_modules/

# VS Code
.vscode/
