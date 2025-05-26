import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyAsg8dJwRe32SEglWL-R7pGhl8CWS38MBo")

# Initialize the Gemini model (flash version for faster responses)
model = genai.GenerativeModel("gemini-1.5-flash")

# Send a message similar to chat completions
response = model.generate_content([
    {"role": "user", "parts": ["what is coding"]}
])

# Print the response
print(response.text)
