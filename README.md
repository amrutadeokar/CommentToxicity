# 🛡️ Toxic Comment Detection System

A web-based application that detects toxic comments in real-time using Natural Language Processing (NLP) and deep learning. It prevents users from submitting toxic remarks by displaying a warning pop-up and blocking the message. When a user submits a non-toxic comment, a pop-up appears saying "Comment submitted successfully," and the comment is displayed under the respective post. If the comment is toxic, a pop-up appears saying "You cannot enter a toxic comment."

## 🔍 Features

- 🔐 User login interface  
- 💬 Comment input section  
- ⚠️ Real-time toxicity detection with a popup warning  
- ✅ Only non-toxic comments are submitted and displayed  
- 🤖 LSTM model trained on labelled comment data  

## 🛠️ Tech Stack

- Frontend: HTML, CSS, JavaScript  
- Backend: Python (Flask API)  
- Machine Learning: TensorFlow/Keras, LSTM, Word Embeddings  
- Dataset: [Toxic Comment Classification Challenge - Kaggle](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)

## 🖼️ Screenshots

https://github.com/amrutadeokar/CommentToxicity/tree/e8fb6aff69dab7a7d55e23857948bedaafb1a278/Project%20Photos

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/commenttoxicity.git
   cd commenttoxicity

2. Set up the Python environment:
   ```bash
   pip install -r requirements.txt
   
3. Start the backend server:
   ```bash
   python model_server.py

4. Open myweb.html in a browser to interact with the frontend.

## 🚀 Usage
- Log in with any credentials.
- Type a comment in the textbox.
       - If the comment is non-toxic, it will be posted below.
       - If the comment is toxic, a warning pop-up will appear, and the comment will be blocked.

## 📚 Learnings
- Applied deep learning for toxic text classification
- Trained and deployed an LSTM model using real-world data
- Integrated an ML model with a frontend interface
- Learned full-stack development and API communication

 🙋‍♀️ Author
Amruta Deokar
🔗 GitHub: [@amrutadeokar](https://github.com/amrutadeokar)

## 📝 License

This project is licensed under the [MIT License](./LICENSE).  
You are free to use, modify, and distribute this software with proper credit to the author.

