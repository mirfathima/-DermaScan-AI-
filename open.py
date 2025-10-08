import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'YOUR OPEN AI API KEY'

# Function to generate output using OpenAI API
def generate_output(answers):
    prompt = f"""
        Act as a doctor advisor, I am having a skin disease, i will give you answers of set of questions. The Question and Answers are 
        "How long have you been experiencing symptoms? (in weeks):" {answers['duration']}
        "How would you rate the pain?" {answers['pain_rating']}
        "How severe is the itchiness?" {answers['itchiness_severity']}
        "Has the affected area increased in size over time?" {answers['area_increase']}
        "How much discomfort does it cause in your daily activities?" {answers['daily_discomfort']}
        "Have you noticed any changes in appearance?" {answers['appearance_changes']}
        "How much does it affect your overall quality of life?" {answers['quality_of_life']}
        "Have you tried any treatments?" {answers['treatments_tried']}
        "Do you have any known allergies to medications or topical treatments?" {answers['allergies']}
        "Are there any other medical conditions you have that may be related to your skin condition?" {answers['related_medical_conditions']}"
        Now based on this, tell me how much sereve my disease is.
    """

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=300  # Adjust as needed
    )

    return response['choices'][0]['text']

# Streamlit app
def main1():
    st.title("Skin Assessment Tool")

    # Collect user responses
    answers = {
        'duration': st.number_input("How long have you been experiencing symptoms? (in weeks):", min_value=0),
        'pain_rating': st.slider("How would you rate the pain?", min_value=0, max_value=10),
        'itchiness_severity': st.slider("How severe is the itchiness?", min_value=0, max_value=10),
        'area_increase': st.radio("Has the affected area increased in size over time?", ["Yes", "No"]),
        'daily_discomfort': st.slider("How much discomfort does it cause in your daily activities?", min_value=0, max_value=10),
        'appearance_changes': st.radio("Have you noticed any changes in appearance?", ["Yes", "No"]),
        'quality_of_life': st.slider("How much does it affect your overall quality of life?", min_value=0, max_value=10),
        'treatments_tried': st.text_area("Have you tried any treatments?", ""),
        'allergies': st.text_area("Do you have any known allergies to medications or topical treatments?", ""),
        'related_medical_conditions': st.text_area("Are there any other medical conditions you have that may be related to your skin condition?", "")
    }

    if st.button("Generate"):
        # Generate output using OpenAI API
        output = generate_output(answers)
        st.write(f"Generated Output:\n{output}")

if __name__ == "__main__":
    main1()