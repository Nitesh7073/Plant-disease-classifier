# 🌿 Plant Disease Classifier

A deep learning-based web application that detects and classifies diseases in plant leaves using image recognition, powered by a FastAPI backend.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Model Details](#model-details)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## 🔍 Overview

Plant diseases cause significant crop losses worldwide. This project provides a fast and accurate tool to identify plant diseases from leaf images using a trained deep learning model. Users can upload an image of a plant leaf and instantly receive a diagnosis along with the disease name and confidence score.

---

## ✨ Features

- 📸 Upload plant leaf images for disease detection
- 🤖 Deep learning model for accurate classification
- ⚡ Fast and lightweight REST API using FastAPI
- 📊 Returns predicted disease name with confidence score
- 🌐 Interactive API docs via Swagger UI (`/docs`)
- 🔄 Supports multiple plant species and disease types

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend API | FastAPI |
| Deep Learning | TensorFlow / PyTorch |
| Image Processing | OpenCV / PIL |
| Server | Uvicorn |
| Language | Python 3.x |

> *(Update the Deep Learning framework based on what you actually used)*

---

## 📁 Project Structure

```
plant-disease-classifier/
│
├── main.py                  # FastAPI app entry point
├── model/
│   └── plant_model.h5       # Trained model file
├── utils/
│   └── preprocess.py        # Image preprocessing functions
├── routes/
│   └── predict.py           # Prediction API route
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/plant-disease-classifier.git
cd plant-disease-classifier
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

Interactive API docs: `http://127.0.0.1:8000/docs`

---

## 📡 API Endpoints

### `POST /predict`

Upload a plant leaf image to get the disease prediction.

**Request:**
- Content-Type: `multipart/form-data`
- Body: `file` — image file (`.jpg`, `.png`)

**Response:**
```json
{
  "disease": "Tomato Early Blight",
  "confidence": 0.97,
  "status": "success"
}
```

---

## 🧠 Model Details

- **Architecture:** CNN (e.g., ResNet50 / MobileNetV2 / custom CNN)
- **Dataset:** PlantVillage Dataset
- **Classes:** *(mention number, e.g., 38 disease categories)*
- **Input Size:** 224x224 pixels
- **Accuracy:** *(mention your model accuracy, e.g., ~95% on test set)*

---

## 🚀 Future Improvements

- [ ] Add frontend UI (React / HTML)
- [ ] Deploy on cloud (AWS / GCP / Render)
- [ ] Support real-time webcam detection
- [ ] Add treatment suggestions for detected diseases
- [ ] Dockerize the application

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

```bash
# Fork the repo, then:
git checkout -b feature/your-feature
git commit -m "Add your feature"
git push origin feature/your-feature
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-profile)

---

> ⭐ If you found this project useful, please give it a star!
