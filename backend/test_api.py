import requests

response = requests.post('http://127.0.0.1:8000/analyze/', json={'text': 'This movie was fantastic!', 'model': 'custom'})
print(response.json())

response = requests.post('http://127.0.0.1:8000/analyze/', json={'text': 'This movie was terrible.', 'model': 'llama'})
print(response.json())
