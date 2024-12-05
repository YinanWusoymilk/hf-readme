from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# OpenAI API Key (replace with your actual API key)
openai.api_key = os.getenv('OPENAI_API_KEY')

# Model ID of your fine-tuned model
FINE_TUNED_MODEL = os.getenv('FINE_TUNE_MODEL_ID')

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/analyze', methods=['POST'])
def analyze():
    # Get user input from the form
    readme_text = request.form.get('readme_text')

    # Define the system prompt and user message
    system_prompt = (
        "You are an intelligent system that analyzes README files from Hugging Face models. "
        "Your task is to extract and classify 8 key components from the README content provided below. "
        "Identify whether each component is present or absent and provide the content of each present component."
    )

    # Call the fine-tuned model using the new API
    response = openai.chat.completions.create(
        model=FINE_TUNED_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"README Content:\n---\n{readme_text}\n---"}
        ]
    )

    # Extract the assistant's reply
    output_text =  response.choices[0].message.content


    return render_template('result.html', output_text=output_text)

    

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
