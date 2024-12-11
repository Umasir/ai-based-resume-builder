from flask import Blueprint, render_template, request, jsonify
import requests

# Create a Blueprint called 'main'
main = Blueprint('main', __name__)

# Example route for the homepage
@main.route('/')
def index():
    return render_template('index.html')

# Example route for preview page
@main.route('/preview', methods=['POST'])
def preview():
    name = request.form['name']
    contact = request.form['contact']
    summary = request.form['summary']
    skills = request.form['skills'].split(',')
    experience = request.form['experience']
    education = request.form['education']
    
    return render_template('preview.html', name=name, contact=contact, summary=summary, skills=skills, experience=experience, education=education)

# Route for generating AI-powered summary
@main.route('/generate-summary', methods=['POST'])
def generate_summary():
    user_input = request.json.get('user_input')
    
    # Call the Gemini or other API here (modify based on your API service)
    url = "https://your-api-endpoint.com/summarize"  # Replace with your AI model endpoint
    headers = {
        "Authorization": "Bearer your-api-key",  # Replace with actual API key
        "Content-Type": "application/json"
    }

    payload = {
        "text": user_input  # Modify according to the API specification
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        summary = response.json().get('summary', '')
        return jsonify({'summary': summary})
    else:
        return jsonify({'error': "Unable to generate summary. Try again later."}), 500
