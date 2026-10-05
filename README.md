# 🌍 AI Travel Guide — Interactive Multilingual Audio Companion

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Gemini API](https://img.shields.io/badge/Google%20Gemini-3.1%20Flash--Lite-8E75B2?style=for-the-badge&logo=googlecloud&logoColor=white)](https://ai.google.dev/)
[![Murf AI](https://img.shields.io/badge/Murf%20AI-Falcon%20TTS-FF8A1F?style=for-the-badge&logo=soundwave&logoColor=white)](https://murf.ai/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)

> An AI-powered, interactive audio tour guide app that generates rich historical commentary and natural multilingual speech synthesis for iconic world destinations in real time.

---

## 📸 Overview & Key Features

**AI Travel Guide** transforms traditional tourist exploration into a dynamic, personalized audio tour experience. Select any iconic landmark or search for custom destinations to receive real-time AI-generated historical insights paired with high-fidelity speech streaming.

### 🌟 Core Highlights

- 🎙️ **Multilingual Audio Generation**: Native voice commentary in **English**, **Hindi**, **Tamil**, and **Telugu**.
- 👤 **Custom Voice Personas**: Choose between **Male** and **Female** natural-sounding voice models powered by Murf AI Falcon TTS.
- ⏱️ **Flexible Depth Options**:
  - **Summarized (~1 min)**: Concise overview highlighting historical significance, key architecture, and cultural relevance.
  - **Detailed (~3 min)**: Immersive storytelling experience detailing timelines, architectural marvels, and visitor insights.
- 📜 **Live Transcript Synchronicity**: Read the complete AI-crafted narrative script with an inline collapsible transcript panel.
- 🎨 **Glassmorphism UI**: Beautiful responsive layout crafted with Tailwind CSS, custom web fonts (*Playfair Display* & *Inter*), and smooth micro-animations.

---

## 🏗️ Architecture Flow

```
┌─────────────────────────┐               ┌─────────────────────────┐
│     Client (Browser)    │  HTTP POST      │     Flask Backend       │
│  index.html / index.js  │ ──────────────> │      (Backend/app.py)   │
└────────────┬────────────┘                 └────────────┬────────────┘
             │                                           │
             │                               ┌───────────┴───────────┐
             │                               │  Google Gemini API    │
             │                               │ (gemini-3.1-flash-lite)
             │                               └───────────┬───────────┘
             │                                           │ (Text Script)
             │                               ┌───────────┴───────────┐
             │                               │   Murf AI TTS Engine  │
             │                               │   (v1/speech/stream)  │
             │                               └───────────┬───────────┘
             │                                           │ (MP3 Stream)
             │   Base64 Audio & Script Text              │
             └───────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack & Dependencies

### **Backend Framework & Services**
| Technology | Role / Purpose |
| :--- | :--- |
| **Python 3.9+** | Core server runtime environment |
| **Flask & Flask-CORS** | Lightweight REST API gateway with cross-origin request support |
| **Google GenAI SDK** | Generates narrative scripts via `gemini-3.1-flash-lite` model |
| **Murf AI Falcon Engine** | High-fidelity, real-time Text-to-Speech (TTS) audio streaming |
| **python-dotenv** | Secure environment variable configuration |

### **Frontend & UI Libraries**
| Technology | Role / Purpose |
| :--- | :--- |
| **HTML5 & Vanilla JS (ES6+)** | Modern single-page web app architecture |
| **Tailwind CSS (CDN)** | Utility-first styling with sleek dark/light aesthetics |
| **Google Fonts** | Premium typography (`Inter` & `Playfair Display`) |

---

## 🌐 Voice & Locale Matrix

| Language | Locale Code | Male Voice Persona | Female Voice Persona |
| :--- | :--- | :--- | :--- |
| **English** | `en-US` | `Matthew` | `Alicia` |
| **Hindi** | `hi-IN` | `Aman` | `Namrita` |
| **Tamil** | `ta-IN` | `Murali` | `Iniya` |
| **Telugu** | `te-IN` | `Zion` | `Josie` |

---

## 📁 Repository Structure

```
travel-guide/
├── Backend/
│   ├── app.py              # Flask server routes & API integrations
│   ├── requirements.txt    # Python dependency manifest
│   └── .env                # Environment secrets (API Keys - gitignored)
├── Frontend/
│   ├── index.html          # Responsive single-page interface layout
│   └── index.js            # UI state, event listeners & API fetch logic
├── .gitignore              # Ignored patterns (.env, __pycache__)
└── README.md               # Project documentation
```

---

## 🚀 Quickstart & Setup Guide

### 1. Prerequisites
Ensure you have the following installed on your machine:
- **Python 3.9** or higher
- A modern web browser (Chrome, Edge, Firefox, Safari)

### 2. Clone & Environment Setup
```bash
git clone https://github.com/your-username/travel-guide.git
cd travel-guide
```

### 3. Backend Setup
Navigate to the `Backend/` directory, create a virtual environment, and install dependencies:

```bash
# Navigate to Backend
cd Backend

# Create virtual environment (Optional but recommended)
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate

# Install required Python packages
pip install -r requirements.txt
```

### 4. Configure Environment Variables (`.env`)
Create a `.env` file inside the `Backend/` directory with your API keys:

```env
MURF_API_KEY=your_murf_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Launch the Backend Server
Run the Flask server:

```bash
python app.py
```
*The server will start at `http://127.0.0.1:5000`*

### 6. Launch the Frontend
Simply open `Frontend/index.html` in your browser, or serve it using a local static server:

```bash
# Example using Python http.server
cd ../Frontend
python -m http.server 8000
```
Open `http://localhost:8000` in your web browser.

---

## 📡 API Reference

### `POST /generate-audio-guide`

Generates custom tourist guide description text and returns base64 encoded MP3 audio stream.

#### Request Body
```json
{
  "place": "Taj Mahal",
  "answerType": "Summary",
  "language": "English",
  "voiceId": "Matthew",
  "locale": "en-US"
}
```

#### Response (200 OK)
```json
{
  "description": "The Taj Mahal is an immense mausoleum of white marble in Agra...",
  "audioBase64": "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4Ljc2LjEwMAAAAAAAAAAAAAAA..."
}
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the project repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.
