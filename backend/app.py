# Part 2: API Development and Testing

from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app) 

fine_tuned_pipeline = pipeline('sentiment-analysis', model='usmangill123/fine_tuned_sentiment_model')

label_mapping = {
    "LABEL_0": "NEGATIVE",
    "LABEL_1": "POSITIVE"
}

# Initialize Groq client
groq_client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def analyze_with_llama(text):
    try:
        # Use Groq's Llama 3 model to classify sentiment
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Classify the sentiment of this text as positive or negative: '{text}'",
                }
            ],
            model="llama3-70b-8192",
        )
        # Extract the response from Llama 3
        response = chat_completion.choices[0].message.content
        # Parse the response to extract sentiment
        if "positive" in response.lower():
            return {"sentiment": "POSITIVE", "confidence": 1.0}  # Confidence is not provided by Llama 3
        elif "negative" in response.lower():
            return {"sentiment": "NEGATIVE", "confidence": 1.0}
        else:
            return {"error": "Unable to determine sentiment"}
    except Exception as e:
        return {"error": str(e)}

@app.route('/analyze/', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text')
    model_choice = data.get('model')

    if not text or not model_choice:
        return jsonify({'error': 'Missing text or model parameter'}), 400

    if model_choice == 'custom':
        result = fine_tuned_pipeline(text)[0]
        sentiment = label_mapping.get(result['label'], result['label'])
        return jsonify({'sentiment': sentiment, 'confidence': result['score']})
    elif model_choice == 'llama':
        llama_result = analyze_with_llama(text)
        if 'error' in llama_result:
            return jsonify({'error': llama_result['error']}), 500
        return jsonify(llama_result)
    else:
        return jsonify({'error': 'Invalid model specified'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
