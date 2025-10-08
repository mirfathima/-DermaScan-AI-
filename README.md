# DERMATECH: Skin Disease Assessment and Prediction

DERMATECH is a Streamlit web application that provides two main functionalities for users concerned about a potential skin condition:
1.  **Assessment:** A questionnaire that uses the OpenAI API to provide a severity assessment based on the user's symptoms.
2.  **Prediction:** An image classifier that predicts the type of skin disease from an uploaded image using a pre-trained Keras model.

## 📁 Project Structure

The application is composed of three Python files:

* `hi.py`: The main entry point for the Streamlit application, setting up the navigation sidebar.
* `open.py`: Contains the **Assessment** tool, which collects user input via a form and uses the OpenAI API for severity analysis.
* `open2.py`: Contains the **Prediction** tool, which loads a Keras model (`skin_disease_modelllll.h5`) to classify an uploaded image.

## 🚀 Getting Started

### Prerequisites

You will need Python 3.x and a set of required libraries.

* **OpenAI API Key**: To use the `Assessment` feature, you must have an OpenAI API key.
* **Model File**: The image prediction feature requires a pre-trained Keras model named `skin_disease_modelllll.h5` to be present in the project's root directory.

### Installation

1.  **Clone the repository (if applicable) or save the files.**

2.  **Install the required Python packages:**
    ```bash
    pip install streamlit openai numpy tensorflow pillow
    ```

3.  **Set up your OpenAI API Key:**
    The API key is currently hardcoded in `open.py`. For security, it's highly recommended to use environment variables instead.

    *Current implementation in `open.py`:*
    ```python
    openai.api_key = '' # **NOTE: REPLACE THIS WITH A SECURE METHOD**
    ```

    *Recommended secure method (using Streamlit Secrets):*
    You would change the line in `open.py` to:
    ```python
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    ```
    And then add your key to a `.streamlit/secrets.toml` file.

4.  **Place the Model File:**
    Ensure the trained model file is in the project directory:
    ```
    skin_disease_modelllll.h5
    ```

### Running the Application

Execute the main file `hi.py` using Streamlit:

```bash
streamlit run hi.py
