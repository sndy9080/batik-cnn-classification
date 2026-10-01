# Batik Keraton Classification

*An image classification project that uses Convolutional Neural Networks and Xception transfer learning to automatically recognize four Indonesian Batik Keraton motifs.*

## 📌 The Problem

Batik is an important part of Indonesian cultural heritage, but the large variety of motifs can make identification and documentation challenging.

Traditional motif identification may require specific knowledge and experience, while the growing need for digital preservation creates opportunities to automate the recognition process using image-based artificial intelligence.

This project focuses on the automatic classification of four Batik Keraton motifs:

* **Kawung**
* **Mega Mendung**
* **Parang**
* **Truntum**

## 💡 The Solution

Developed an image classification system using two deep learning approaches:

1. **CNN from Scratch**
2. **Xception Transfer Learning**

The workflow begins with collecting and organizing Batik Keraton images according to their respective classes. Images are then resized to **224 × 224 pixels** and normalized by scaling pixel values to the range of 0–1.

The dataset is divided into training, validation, and testing sets before being used to train the classification models.

The CNN model uses a simple architecture consisting of:

* Conv2D
* MaxPooling2D
* Dropout
* Flatten
* Dense with Softmax output

The Xception approach uses a pre-trained **ImageNet** backbone with its main layers frozen, followed by additional layers for classifying the four Batik Keraton categories.

The trained models are then evaluated using accuracy, loss curves, confusion matrices, classification reports, prediction errors, and external images that are outside the training, validation, and test datasets.

## 🚀 The Impact / Results

* The dataset contains approximately **1,800 Batik Keraton images** distributed across four classes: **Kawung (507)**, **Mega Mendung (472)**, **Parang (426)**, and **Truntum (395)**.
* Images are standardized to **224 × 224 pixels** and normalized before model training.
* The CNN-from-scratch experiment uses approximately **90% training, 5% validation, and 5% testing** data.
* The Xception experiment uses approximately **80% training, 10% validation, and 10% testing** data.
* Both models successfully learn to classify the four Batik Keraton motifs and are evaluated through training curves, confusion matrices, classification reports, and prediction error analysis.
* During external image testing, the **CNN from scratch** produced more varied confidence levels and some classification errors, particularly for complex motifs, unusual viewpoints, clothing images, and less ideal lighting conditions.
* The **Xception transfer learning model** produced more stable and consistent predictions on the same external images, with many predictions reaching high confidence levels.
* The project demonstrates how deep learning can support the **digital identification, preservation, education, and promotion of Batik Keraton**.

## 📂 Repository Structure

The repository contains the trained deep learning models, Jupyter notebooks for experimentation, dataset references, and a web application for image classification.

```text
batik-cnn-classification/
├── README.md
│
├── datasets/
│   └── link_kaggle.txt
│
├── models/
│   ├── scratch_model/
│   │   └── scratchCNN.keras
│   │
│   └── xception_model/
│       └── Xception.keras
│
├── notebooks/
│   ├── scratch/
│   │   └── Percobaan CNN - Batik.ipynb
│   │
│   └── xception/
│       └── Percobaan CNN add Models Xception.ipynb
│
└── website/
    ├── app.py
    │
    ├── external_test/
    │   ├── download.jpg
    │   ├── download (1).jpg
    │   ├── ...
    │   ├── images.jpg
    │   ├── images (1).jpg
    │   └── ...
    │
    ├── static/
    │   └── uploads/
    │       ├── 140926-104434.png
    │       ├── 140926-104503.png
    │       ├── 140926-104620.png
    │       ├── 140926-104635.png
    │       └── 140926-104647.png
    │
    └── templates/
        ├── classifications-simple.html
        ├── classifications.html
        └── cnn.html
```

## 🛠️ Tech Stack

* **Python**
* **TensorFlow / Keras**
* **Convolutional Neural Network (CNN)**
* **Xception**
* **Transfer Learning**
* **ImageDataGenerator**
* **NumPy**
* **Pandas**
* **Scikit-learn**
* **Matplotlib**
* **Seaborn**
* **Jupyter Notebook**
* **HTML / CSS**
* **Keras `.keras` Models**

## 📸 Project Gallery

### External Test Images

The project includes external Batik images that were not part of the training, validation, or test datasets. These images are used to evaluate how the trained models perform under different real-world conditions.

### Model Prediction

The classification system produces:

* Predicted Batik motif
* Prediction confidence
* Classification results for external images

### Model Evaluation

The project includes evaluation outputs such as:

* Training and validation loss
* Training and validation accuracy
* Confusion matrix
* Classification report
* Prediction error analysis

### Classification Web Application

The `website/` directory contains the web application and HTML templates used to present and perform Batik motif classification.

* [Classification Interface](website/templates/classifications.html)
* [Simple Classification Interface](website/templates/classifications-simple.html)
* [CNN Interface](website/templates/cnn.html)
