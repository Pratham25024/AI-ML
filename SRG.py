import json

response = """{
  "benefits": [
    "Easy to learn",
    "Strong libraries",
    "Great community support"
  ]
}"""

try:
    data = json.loads(response)
except json.JSONDecodeError:
    data = {"error": "Invalid JSON response"}

print(data)
