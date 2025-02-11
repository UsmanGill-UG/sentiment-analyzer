# Sentiment Analysis System with Custom Fine-Tuned Model and Llama 3

## Overview
This project is a sentiment analysis system that uses a custom fine-tuned model and the Llama 3 model. It includes a backend API built with Flask, a frontend UI developed in React, and a detailed workflow for fine-tuning and testing the models.

## Features
- **Custom Fine-Tuned Model**: A DistilBERT model fine-tuned on the IMDB dataset for sentiment analysis.
- **Llama 3 Integration**: Utilizes the Llama 3 model via the Groq Cloud API for sentiment analysis.
- **Backend API**: A Flask-based API with an `/analyze` endpoint that accepts text and returns sentiment (positive/negative) and confidence scores.
- **Frontend UI**: A React-based user interface with a text input field, model selection dropdown, and results display.
- **Testing**: The system is tested locally with both the custom fine-tuned model and the Llama 3 model.

## Workflow

### 1. **Dataset Preparation and Fine-Tuning**
- **Dataset**: The IMDB dataset was downloaded and preprocessed. The sentiment column was encoded (positive -> 1, negative -> 0), and only the review and label columns were retained.
- **Model Selection**: The `distilbert-base-uncased` model from Hugging Face was selected for fine-tuning.
- **Tokenization**: The dataset was tokenized with truncation, padding, and a maximum sequence length of 256.
- **Fine-Tuning**: The model was fine-tuned on the IMDB dataset for 2 epochs using the Hugging Face Trainer. Training parameters included a learning rate of 5e-5 and a batch size of 16. Metrics like accuracy, precision, recall, and F1-score were logged during training.
- **Model Upload**: The fine-tuned model and tokenizer were saved locally and uploaded to Hugging Face Hub.

### 2. **API Development and Testing**
- **Backend API**: A Flask backend was created with a POST endpoint `/analyze` that accepts:
  - `text`: The input text for sentiment analysis.
  - `model`: A parameter specifying the model to use (custom or Llama 3).
  The endpoint returns the sentiment (positive or negative) and a confidence score.
- **Model Loading**: The fine-tuned model was loaded from Hugging Face, and the Llama 3 model was accessed using the Groq Cloud API.
- **API Testing**: The `/analyze` endpoint was tested locally using Postman, curl, and Python requests.
- **Llama 3 Prompt**: A clear and reusable prompt was defined for the Llama 3 model in Groq Cloud. Example prompt: "Classify the sentiment of this text as positive or negative: 'This movie was fantastic'."
- **Testing with Both Models**: The API was verified to work with both the fine-tuned model and the Llama 3 model, ensuring the results return the sentiment and confidence score.

### 3. **UI Design and Explanation**
- **React UI**: A React frontend was designed with:
  - A text input field for user input.
  - A dropdown menu for model selection (Custom Model or Llama 3).
  - A button labeled "Analyze Sentiment" to send input and selected model to the backend API.
  - A result display section showing the sentiment (positive or negative) and confidence score.
