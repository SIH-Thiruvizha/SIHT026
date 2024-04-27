import streamlit as st
import requests
from PIL import Image
import io

# API_URL = "https://api-inference.huggingface.co/models/jy46604790/Fake-News-Bert-Detect"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()

# def get_prediction_label(prediction):
#     score1 = prediction[0][0]['score']
#     score2 = prediction[0][1]['score']
#     st.write('Real%:',score1*100)
#     st.write('Fake%:',score2*100)
# st.title('Fake News Detection')

# user_input = st.text_input('Enter text:')
# try:
#     if st.button('Check'):
#         output = query({
#             "inputs": user_input,
#         })
#         prediction_label, image_url = get_prediction_label(output)
#         st.write(f"Prediction: {prediction_label}")
#         st.image(image_url, caption='Image', use_column_width=True)
# except:
#     st.write('Plz give Input')

API_URL = "https://api-inference.huggingface.co/models/prithivMLmods/Deep-Fake-Detector-Model"
headers = {"Authorization": "Bearer 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"}

def query(image_bytes):
    response = requests.post(API_URL, headers=headers, data=image_bytes)
    return response.json()

st.title('Deep Fake Image Detector')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Convert the image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='JPEG')
    image_bytes = image_bytes.getvalue()

    if st.button('Check for Deep Fake'):
        output = query(image_bytes)
        st.write(output)

#text

