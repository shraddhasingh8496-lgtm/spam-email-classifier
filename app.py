import streamlit as st
import joblib

# Load the trained model
model = joblib.load("spam_classifier.pkl")

# App title
st.title("📧 Spam Email Classifier")

st.write("Enter a message below to check whether it is spam or genuine.")

# Message input
message = st.text_area("Enter your message:")

# Check button
if st.button("Check Message"):

    if message.strip() == "":
        st.warning("Please enter a message.")

    else:
        prediction = model.predict([message])[0]

        if prediction == "spam":
            st.error("⚠️ This message is SPAM")
        else:
            st.success("✅ This message is NOT SPAM")
