import React, { useState } from 'react';
import './SentimentAnalyzer.css';

export default function SentimentAnalyzer() {
  const [text, setText] = useState('');
  const [model, setModel] = useState('custom');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeSentiment = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:8000/analyze/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text, model })
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error analyzing sentiment:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h1 className="title">Sentiment Analysis</h1>

        <div className="input-group">
          <label htmlFor="text-input">Enter Text</label>
          <input
            id="text-input"
            type="text"
            placeholder="Type your sentence here..."
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
        </div>

        <div className="input-group">
          <label htmlFor="model-select">Select Model</label>
          <select
            id="model-select"
            value={model}
            onChange={(e) => setModel(e.target.value)}
          >
            <option value="custom">Custom Model</option>
            <option value="llama">Llama 3</option>
          </select>
        </div>

        <button
          onClick={analyzeSentiment}
          disabled={loading}
          className="analyze-button"
        >
          {loading ? 'Analyzing...' : 'Analyze Sentiment'}
        </button>

        {result && (
          <div className="result">
            <h2>Result</h2>
            <p>Sentiment: <span className={result.sentiment === 'positive' ? 'positive' : 'negative'}>{result.sentiment}</span></p>
            {result.confidence && (
              <p>Confidence: {result.confidence.toFixed(2)}%</p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
