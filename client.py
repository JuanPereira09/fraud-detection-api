import requests

url = "http://127.0.0.1:8000/fraud/analyze"

data = {
    "user_id": 5,
    "amount": 8000,
    "country": "BR"
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Resposta:", response.json())
