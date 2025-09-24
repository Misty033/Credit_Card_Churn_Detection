import streamlit as st
import requests
import pandas as pd
import io
import os

# --- Page Configuration ---
st.set_page_config(page_title="Credit Card Churn Predictor", layout="centered")
st.title("Credit Card Churn Prediction")
st.markdown("Upload your CSV file below to receive predictions.")

# --- Backend URL Configuration ---
BACKEND_URL = os.environ.get("BACKEND_URL", "YOUR_PRIVATE_FASTAPI_BACKEND_URL/api/predict_csv")

# --- UI for File Upload ---
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    st.success("File uploaded successfully.")
    
    if st.button("Predict and Download CSV"):
        try:
            with st.spinner("Sending file to the prediction API and awaiting results..."):
                # Define the files payload for the POST request
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}
                # response = requests.post(BACKEND_URL, files=files)
                
                response = requests.post(
                    "http://fastapi:8000/api/predict_csv", 
                    files=files
                )


            # --- Process the Response ---
            if response.status_code == 200:
                st.success("Prediction successful!")
                
                # Read the returned CSV data into a pandas DataFrame
                result_df = pd.read_csv(io.StringIO(response.text))
                
                st.markdown("### Prediction Results Preview")
                st.dataframe(result_df.head())

                # Prepare the data for download
                csv_output = result_df.to_csv(index=False).encode('utf-8')
                
                st.download_button(
                    label="Download Predictions as CSV",
                    data=csv_output,
                    file_name="predictions.csv",
                    mime="text/csv"
                )
            else:
                # Display a detailed error if the API returns a non-200 status
                st.error(f"API Error (Status {response.status_code}): {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"Network error: Could not connect to the backend service. Please ensure the URL is correct. Details: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

