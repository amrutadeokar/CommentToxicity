from flask import Flask, request, jsonify, render_template # type: ignore
import tensorflow as tf # type: ignore
import numpy as np # type: ignore
from flask import Flask, request, jsonify # type: ignore
from tensorflow.keras.layers import TextVectorization # type: ignore
import pandas as pd # type: ignore
from flask_cors import CORS  # type: ignore # Import Flask-CORS to handle cross-origin requests
from flask import session, redirect, url_for # type: ignore


app = Flask(__name__, static_folder='Website/static', template_folder='Website/templates')

app.secret_key = 'your_secret_key'  # Add this near app initialization

# Enable CORS for all domains (you can specify domains if needed)
CORS(app, supports_credentials=True)

# Load the pre-trained model
model = tf.keras.models.load_model('toxic_comment_model.keras')

# Define your text vectorizer (same as in your notebook)
MAX_FEATURES = 200000
MAX_SEQUENCE_LENGTH = 1800
vectorizer = TextVectorization(max_tokens=MAX_FEATURES,
                               output_sequence_length=MAX_SEQUENCE_LENGTH,
                               output_mode='int')

# Assuming you have some sample data for fitting the vectorizer
# In your case, this would be your full training dataset (df['comment_text'])
df = pd.read_csv('Toxicity/train.csv')
x = df['comment_text']
vectorizer.adapt(x.values)

@app.route('/')
def home():
    return render_template('myweb.html')  # Render the HTML file

@app.route('/login', methods=['POST'])
def login():
    Email = request.form.get('email')
    Password = request.form.get('password')

    # Dummy authentication (Replace with actual authentication logic)
    if Email == "abc@123" and Password == "pccoer":
        session['email'] = Email  # Store session data
        return redirect(url_for('dashboard'))  # Redirect to second page
    else:
        return render_template('myweb.html', error="Invalid credentials")

@app.route('/dashboard')
def dashboard():
    if 'email' in session:  # Check if user is logged in
        return render_template('myweb2.html')  # Main Page
    else:
        return redirect(url_for('home'))  # Redirect back to login if not authenticated


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text_input = data['text']

        if isinstance(text_input, str):
            text_input = [text_input]

        input_text = vectorizer(text_input)
        prediction = model.predict(input_text)

        category_labels = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]

        # Check if any category has a value greater than the threshold (0.5)
        result = {category_labels[i]: int(prediction[0][i] > 0.5) for i in range(len(category_labels))}
        
        # Check if any of the categories is toxic
        is_toxic = any(value == 1 for value in result.values())

        if is_toxic:
            return jsonify({'message': "You cannot enter a Toxic comment", 'status': 'error'})
        else:
            return jsonify({'message': "Comment submitted successfully", 'status': 'success'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
