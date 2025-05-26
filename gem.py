import requests

# Replace this with your actual Gemini API key
API_KEY = "AIzaSyAsg8dJwRe32SEglWL-R7pGhl8CWS38MBo"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Explain how AI works in a few words"
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

# Print the response
print(response.status_code)
print(response.json())
