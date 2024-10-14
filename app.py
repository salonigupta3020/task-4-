from flask import Flask, request, jsonify
from PIL import Image
import openai

app = Flask(__name__)

# Load your Google credentials here (set environment variable or use directly)
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_credentials.json"

@app.route('/chat', methods=['POST'])

def chat():
    user_input = request.json.get('input')
    # Handle text input and respond
    response = handle_text_input(user_input)
    return jsonify({'response': response})

def handle_text_input(text):
    # Use Google Palm and Gemini AI to generate a text response
    # For demonstration, we're just echoing the input
    return f"You said: {text}"

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/chat', methods=['POST'])

def chat():
    user_input = request.json.get('input')
    image_file = request.files.get('image')  # Add support for image upload

    if image_file:
        image_response = handle_image_input(image_file)
        return jsonify({'image_response': image_response})

    response = handle_text_input(user_input)
    return jsonify({'response': response})

def handle_image_input(image_file):
    # Open the image using PIL
    img = Image.open(image_file)
    img.show()  # Display the image (for debugging purposes)

    # Use Google Palm or Gemini AI to analyze the image and generate a response
    # Placeholder: replace with your AI image analysis code
    return "Image processed successfully."

def handle_text_input(text):
    # Replace with actual API call to Google Palm/Gemini
    # Example API call to OpenAI for demonstration
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    )
    return response['choices'][0]['message']['content']


