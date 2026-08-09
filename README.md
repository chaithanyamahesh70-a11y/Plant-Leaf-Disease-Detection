# 🌱 Plant Leaf Disease Detection

A web-based Plant Leaf Disease Detection system that uses Deep Learning to identify diseases from plant leaf images. The application is developed using Python, Flask, PyTorch, HTML, CSS and JavaScript.

## 📌 Project Overview

Plant diseases can significantly affect crop production and quality. This project provides an easy-to-use web application where users can upload an image of a plant leaf and receive a predicted disease along with relevant disease information.

The system uses a trained CNN-based deep learning model to classify plant leaf images.

## ✨ Features

- 🌿 Plant leaf disease detection
- 📷 Upload plant leaf images
- 🤖 CNN-based disease classification
- 🔍 Automated disease prediction
- 📋 Disease information display
- 💊 Supplement/treatment information
- 🌱 Supports multiple plant and crop categories
- 🖥️ User-friendly Flask web interface
- 🧪 Includes sample test images

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