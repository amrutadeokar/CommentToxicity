import tensorflow as tf
import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.layers import TextVectorization
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model('toxic_comment_model.h5')

# Define your text vectorizer (same as in your notebook)
MAX_FEATURES = 200000
MAX_SEQUENCE_LENGTH = 1800
vectorizer = TextVectorization(max_tokens=MAX_FEATURES,
                               output_sequence_length=MAX_SEQUENCE_LENGTH,
                               output_mode='int')

# Assuming you have some sample data for fitting the vectorizer
# In your case, this would be your full training dataset (df['comment_text'])
# We will use df['comment_text'] to fit the vectorizer as done in the notebook
df = pd.read_csv('Toxicity/train.csv')
x = df['comment_text']
vectorizer.adapt(x.values)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get input data from frontend (JSON format)
    text_input = data['text']  # Get the text input from the frontend request
    
    # Preprocess the input (same as you did with vectorizer in the notebook)
    input_text = vectorizer(text_input)
    
    # Use the model to make a prediction
    prediction = model.predict(np.expand_dims(input_text, 0))
    
    # Return the prediction as a JSON response
    result = (prediction > 0.5).astype(int).tolist()  # Threshold to classify
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
