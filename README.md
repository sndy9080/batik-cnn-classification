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

The trained models are evaluated using training and validation curves, confusion matrices, classification reports, prediction error analysis, and external images that are outside the training, validation, and test datasets.

## 🚀 The Impact / Results

* The dataset contains approximately **1,800 Batik Keraton images** distributed across four classes: **Kawung (507)**, **Mega Mendung (472)**, **Parang (426)**, and **Truntum (395)**.
* Images are standardized to **224 × 224 pixels** and normalized before model training.
* The CNN-from-scratch experiment uses approximately **90% training, 5% validation, and 5% testing** data.
* The Xception experiment uses approximately **80% training, 10% validation, and 10% testing** data.
* Both models successfully learn to classify the four Batik Keraton motifs and are evaluated using accuracy, loss, confusion matrix, classification report, and prediction error analysis.
* During external image testing, the **CNN from scratch** produced more varied confidence levels and some classification errors, particularly on complex motifs, unusual viewpoints, clothing images, and less ideal lighting conditions.
* The **Xception transfer learning model** produced more stable and consistent predictions on the same external images, with many predictions reaching high confidence levels.
* The project demonstrates how deep learning can support the **digital identification, preservation, education, and promotion of Batik Keraton**.

## 📂 Repository Structure

The repository contains trained deep learning models, Jupyter notebooks, dataset references, evaluation outputs, and a web application for Batik motif classification.

```text
batik-cnn-classification/
├── README.md
│
├── datasets/
│   └── link_kaggle.txt
│
├── images/
│   ├── System Workflow.png
│   ├── Loss and Accuracy Charts for the CNN Model from Scratch.png
│   ├── Loss and Accuracy Plots for the Xception Transfer Learning Model.png
│   ├── Evaluation of the confusion matrix, classification report, and prediction error for the CNN Model from Scratch.png
│   ├── Evaluasi confusion matrix, classification report, dan prediksi error pada Model Transfer Learning Xception.png
│   ├── Prediction results for the external dataset using the CNN model from scratch.png
│   └── Prediction results from the Xception model's external dataset.png
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
├── src/
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

### System Workflow

<p align="center">
  <img src="images/System Workflow.png" alt="Batik Classification System Workflow" width="400">
</p>

### CNN from Scratch — Loss & Accuracy

<p align="center">
  <img src="images/Loss and Accuracy Charts for the CNN Model from Scratch.png" alt="CNN from Scratch Loss and Accuracy" width="400">
</p>

### Xception Transfer Learning — Loss & Accuracy

<p align="center">
  <img src="images/Loss and Accuracy Plots for the Xception Transfer Learning Model.png" alt="Xception Loss and Accuracy" width="400">
</p>

### CNN from Scratch — Evaluation

<p align="center">
  <img src="images/Evaluation of the confusion matrix, classification report, and prediction error for the CNN Model from Scratch.png" alt="CNN from Scratch Evaluation" width="400">
</p>

### Xception — Evaluation

<p align="center">
  <img src="images/Evaluasi confusion matrix, classification report, dan prediksi error pada Model Transfer Learning Xception.png" alt="Xception Evaluation" width="400">
</p>

### External Dataset — CNN from Scratch

<p align="center">
  <img src="images/Prediction results for the external dataset using the CNN model from scratch.png" alt="CNN from Scratch External Prediction Results" width="400">
</p>

### External Dataset — Xception

<p align="center">
  <img src="images/Prediction results from the Xception model's external dataset.png" alt="Xception External Prediction Results" width="400">
</p>

### Classification Web Application

The `website/` directory contains the web application and HTML templates used to perform Batik motif classification.

* [Classification Interface](website/templates/classifications.html)
* [Simple Classification Interface](website/templates/classifications-simple.html)
* [CNN Interface](website/templates/cnn.html)
