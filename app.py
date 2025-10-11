# Imported Flask and helper functions
from flask import Flask, render_template, request
import os

# Import alt text generator function
from alt_text_generator import generate_alt_text

# Create Flask app instance
app = Flask(__name__)

# Define home page route
@app.route('/')
def home():
    #Render the home page template
    return render_template('index.html')

# Define form submission route with POST method
@app.route('/generate', methods=['POST'])
def generate():
    # Get the image URL submitted by the user 
    image_url = request.form['image_url']
  
    # Generate alt text using your function
   #alt_text = generate_alt-text() 
    alt_text = generate_alt_text(image_url)

    #  Show result page with image and alt text
    return render_template('result.html', image_url=image_url, alt_text=alt_text)

from flask import request, jsonify

@app.route('/generate-alt', methods=['POST'])
def generate_alt():
    data = request.get_json()
    image_url = data.get('image_url')
    alt_text = generate_alt_text(image_url)
    return jsonify({'alt_text': alt_text})


if __name__ == '__main__':
    app.run(debug=True)
