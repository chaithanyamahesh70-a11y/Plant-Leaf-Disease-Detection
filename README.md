# 🌱 Plant Leaf Disease Detection

A web-based **Plant Leaf Disease Detection System** that uses Deep Learning to identify diseases from plant leaf images. The application allows users to upload a leaf image and receive a predicted disease along with relevant disease information and treatment/supplement details.

The project is developed using **Python, Flask, PyTorch, HTML, CSS, and JavaScript**.

---

## 📌 Project Overview

Plant diseases can significantly affect crop production and quality. Early identification of plant diseases can help farmers and users take appropriate preventive and treatment measures.

This project provides an easy-to-use web application where users can upload an image of a plant leaf and receive an automatically predicted disease.

The system uses a trained **CNN-based Deep Learning model** to classify plant leaf images into different disease categories.

---

## ✨ Features

- 🌿 Plant leaf disease detection
- 📷 Upload plant leaf images
- 🤖 CNN-based disease classification
- 🔍 Automated disease prediction
- 📊 Confidence score for predictions
- 📋 Disease information display
- 💊 Supplement and treatment information
- 🌱 Supports multiple plant and crop categories
- 🖥️ User-friendly web interface
- 🧪 Includes sample test images
- 📱 Responsive web interface

---

## 🛠️ Technologies Used

### Programming Languages

- Python
- HTML
- CSS
- JavaScript

### Frameworks & Libraries

- Flask
- PyTorch
- Torchvision
- NumPy
- Pandas
- Pillow

### Tools

- Visual Studio Code
- Git
- GitHub
- Git LFS

---

## 📂 Project Structure

```text
Plant-Leaf-Disease-Detection/
│
├── app.py
├── CNN.py
├── disease_info.csv
├── supplement_info.csv
├── plant_disease_model_1_latest.pt
├── requirements.txt
├── README.md
├── .gitignore
├── .gitattributes
│
├── screenshots/
│   ├── home.png
│   ├── detection.png
│   └── result.png
│
├── static/
│   ├── css/
│   ├── images/
│   ├── js/
│   └── test_images/
│
└── templates/
    ├── base.html
    ├── home.html
    ├── about.html
    ├── contact.html
    ├── detect.html
    └── result.html