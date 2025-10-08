import streamlit as st
from open import main1
from open2 import main2




# Create a dictionary mapping page names to their respective functions
pages = {
    "Assessment": main1,
    "Prediction": main2,
   
}

# Streamlit App
def main():
    st.sidebar.title("DERMATECH")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    # Run the function corresponding to the selected page name
    pages[selection]()

if __name__ == "__main__":
    main()
