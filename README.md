📧 Spam Email Classifier

A Machine Learning project that classifies text messages as Spam or Not Spam using Natural Language Processing (NLP).

🚀 Project Overview

This project uses TF-IDF to convert text into numerical features and Multinomial Naive Bayes to classify messages.

A Streamlit web application is created so users can enter a message and get an instant prediction.

🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Multinomial Naive Bayes
- Joblib
- Streamlit
- Google Colab
- GitHub

⚙️ How It Works

1. Dataset is collected and prepared.
2. Text data is cleaned and processed.
3. TF-IDF converts text into numerical features.
4. Multinomial Naive Bayes is trained on the data.
5. The trained model is saved using Joblib.
6. Streamlit loads the model.
7. User enters a message.
8. The model predicts Spam or Not Spam.

💻 How to Run

Install the required libraries:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

📊 Example

Input:

«Congratulations! You have won a free prize. Click now!»

Prediction:

«🚨 Spam»

Input:

«Hi, are you coming to college tomorrow?»

Prediction:

«✅ Not Spam»

📁 Project Files

- "app.py" — Streamlit application
- "spam_classifier.pkl" — Trained Machine Learning model
- "requirements.txt" — Required Python libraries

🎯 Future Improvements

- Improve the model with a larger dataset.
- Add prediction confidence.
- Improve text preprocessing.
- Try advanced Machine Learning and Deep Learning models.
  
- Name: Shraddha Singh
- BCA/DS/AI
