# Plant Disease Detection Using CNN (Beans Dataset)
This project demonstrates how to build, evaluate, and deploy a plant disease detection system using a Convolutional Neural Network (CNN) trained on the beans dataset. It enables users to classify bean leaf images as "healthy", "angular leaf spot", or "bean rust" through an interactive web application, helping farmers and researchers easily diagnose crop diseases.

## Project Description
This repository features a full end-to-end workflow:
* Data loading with TensorFlow Datasets (no manual downloads)
* Image preprocessing and visualization
* CNN model building, training, and evaluation using TensorFlow/Keras
* Deployment with Gradio—an accessible web UI anyone can use to upload images for automatic plant disease detection

The code and explanations are beginner-friendly, making this notebook a great resource for anyone learning deep learning, agriculture technology, or real-world deployment.

## Folder Structure
File  | Purpose
------- | -------
bean_classifier.py | # Gradio-based web app serving the trained model
bean_classifier.h5 | # Trained Keras model weights (ready for inference)
CNN_concept.md | # Clear, simple conceptual guide to CNNs and how they work
Plant_Disease_Detection_Using_CNN.ipynb | # Step-by-step Jupyter/Colab notebook covering data loading, training, visualization, and more
 images/ | # Folder containing example images/diagrams used in CNN_concept.md
README.md | # Project description and usage guide


## Getting Started
1. Clone the repository

`git clone https://github.com/muhammadfahd/plant-disease-detection-using-cnn- `


1. **Colab Notebook**
You can start by opening Plant_Disease_Detection_Using_CNN.ipynb in Google Colab for detailed, step-by-step walkthrough of the workflow (installation, training, evaluation, and model export).

2. **Dataset**
Beans Disease Dataset: Automatically loaded via TensorFlow Datasets using:

python
```
import tensorflow_datasets as tfds
dataset = tfds.load('beans', as_supervised=True)

```
Contains thousands of labeled images, divided into three classes: healthy, angular leaf spot, and bean rust.


3. **Features**
* Clean Jupyter notebook: fully reproducible and educational
* Gradio web UI: anyone can upload a bean leaf image and receive a prediction
* Deployment-ready: easy to upload to Hugging Face Spaces for public/demo use
* Clear explanation of CNN concepts in CNN_concept.md
* Example visuals and diagrams in the images folder


