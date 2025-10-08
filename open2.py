import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load the pre-trained model
model = load_model('skin_disease_modelllll.h5')

# Define the class names (you may need to adjust this based on your model's classes)
class_names = ['Acne and Rosacea ',
               'Actinic Keratosis Basal Cell Carcinoma and Malignant Lesions ','Atopic Dermatitis ',
               'Basal Cell Carcinoma','Benign Keratosis-like Lesions',
               'Cellulitis Impetigo and Bacterial Infections ','Chickenpox ',
               'Eczema ','Exanthems and Drug Eruptions ','Hairloss ',
               'Herpes HPV and STDs ','Impetigo ',
               'Infectious erythema ','Light Diseases and Disorders of Pigmentation ',
               'Lupus and Connective Tissue ','Melanocytic Nevi (NV) ',
               'Melanoma Skin Cancer Nevi and Moles ','Nail Fungus ',
               'Normal ','Poison Ivy Photos and Contact Dermatitis ',
               'Psoriasis pictures Lichen Planus and related disease_21','Scabies ',
               'Seborrheic Keratoses and Benign Tumors ','Skin Allergy ',
               'Skin warts ','Systemic Disease ',
               'Tinea Ringworm Candidiasis and Fungal Infections ',
               'Urticaria Hives ','Vascular Tumors ',
               'Vasculitis ','Warts Molluscum and Viral Infections ']    # Define your class names here] # Replace with your actual class names
def main2():
    st.title('Skin Disease Classifier')

    # Function to make predictions
    def predict(image_path):
        # Load and preprocess the image
        img = Image.open(image_path)
        img = img.resize((192, 192))  # Resize the image to match the model's input size
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0  # Normalize pixel values

        # Make prediction
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction)
        
        return class_names[predicted_class], prediction[0][predicted_class]

    # Main Streamlit app
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

        # Make prediction when the user uploads an image
        prediction, confidence = predict(uploaded_file)
        

        if prediction == 'Acne and Rosacea ':
            st.write('Acne and Rosacea Photos, Caused by: excess oil, clogged pores, and bacteria, and also factors include genetics, blood vessel abnormalities, and inflammation.Symptoms:Pimples, blackheads, whiteheads,Facial redness, visible blood vessels, swollen bumps,Treatment:Topical or oral antibiotics, retinoids, laser therapy, Measure to be taken to avoid spreading : Avoid picking or squeezing pimples, keep hands and face clean,Use gentle skincare products')
        elif prediction == 'Actinic Keratosis Basal Cell Carcinoma and Malignant Lesions ':
            st.write('Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions,Caused by:Prolonged sun exposure leading to skin damage,including genetic predisposition. Symptoms:Rough, scaly patches on the skin,Pearly or waxy bump. Treatment:cryotherapy, laser therapy, or surgical removal,radiation therapy, chemotherapy.Measure to be taken to avoid spreading :Use sunscreen, wear protective clothing, and limit sun exposure')
        elif prediction == 'Atopic Dermatitis ':
            st.write('Atopic Dermatitis ,Caused by:including a compromised skin barrier and immune system, as well as exposure to allergens or irritants. Symptoms:Itchy and inflamed skin, redness, dryness. Treatment:Moisturizers to hydrate the skin, topical corticosteroids or immunomodulators for inflammation, antihistamines for itching. Measure to be taken to avoid spreading :Regularly moisturize to maintain skin integrity,practice good personal hygiene')
        else:
            st.write('Prediction disease is', prediction)
        # st.write('Prediction disease is', prediction)
            
if __name__ == "__main__":
    main2()