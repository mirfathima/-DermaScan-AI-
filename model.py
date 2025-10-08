
import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load the trained model from the .h5 file
model = tf.keras.models.load_model('/content/skin_disease_modelllll.h5')

# Define the classes (if you haven't already)
class_names = ['Acne and Rosacea Photos', 'Eczema Photos', 'Melanoma Skin Cancer Nevi and Moles',
                   'Light Diseases and Disorders of Pigmentation', 'Systemic Disease',
                   'Nail Fungus and other Nail Disease', 'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions',
                   'Atopic Dermatitis Photos', 'Bullous Disease Photos', 'Cellulitis Impetigo and other Bacterial Infections',
                   'Eczema Photos', 'Exanthems and Drug Eruptions', 'Hair Loss Photos Alopecia and other Hair Diseases',
                   'Herpes HPV and other STDs Photos', 'Psoriasis pictures Lichen Planus and related diseases',
                   'Scabies Lyme Disease and other Infestations and Bites', 'Seborrheic Keratoses and other Benign Tumors',
                   'Systemic Disease', 'Tinea Ringworm Candidiasis and other Fungal Infections', 'Urticaria Hives',
                   'Vascular Tumors', 'Vasculitis Photos', 'Warts Molluscum and other Viral Infections']    # Define your class names here

# Function to preprocess the image
def preprocess_image(image):
    # Preprocess the image (e.g., normalize pixel values)
    image = image / 255.0  # Assuming your original model was trained with pixel values normalized to [0, 1]
    return image

# Function to make predictions
def predict(image):
    # Preprocess the image
    image = preprocess_image(image)
    # Expand dimensions to match model's expected shape
    image = np.expand_dims(image, axis=0)
    # Make predictions
    predictions = model.predict(image)
    # Find the class with the highest probability
    predicted_class = np.argmax(predictions)
    confidence = np.max(predictions)
    return predicted_class, confidence

# Streamlit app
def main():
    st.title('Skin Disease Classifier')
    st.write('Upload an image for classification')

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image_data = Image.open(uploaded_file)
        st.image(image_data, caption='Uploaded Image', use_column_width=True)

        # Convert the PIL image to numpy array
        image_array = np.array(image_data)

        # Make prediction
        predicted_class, confidence = predict(image_array)
        st.write(f'Prediction: {class_names[predicted_class]}')
        st.write(f'Confidence: {confidence}')

if __name__ == '__main__':
    main()
