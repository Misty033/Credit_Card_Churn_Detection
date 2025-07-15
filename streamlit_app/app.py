import streamlit as st
import requests
import pandas as pd
import io

st.set_page_config(page_title="Credit Card Churn Predictor", layout="centered")
st.title("Credit Card Churn Prediction")
st.markdown("Upload your CSV file below to receive predictions.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    st.success("File uploaded successfully.")
    
    if st.button("Predict and Download CSV"):
        try:

            with st.spinner("Sending file to API and waiting for response..."):
                response = requests.post(
                    "http://fastapi:8000/api/predict_csv",
                    files={"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}
                )

            if response.status_code == 200:
                result_df = pd.read_csv(io.StringIO(response.text))
                st.success("Prediction successful!")

                st.dataframe(result_df.head())

                csv = result_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download Predictions CSV",
                    data=csv,
                    file_name="predictions.csv",
                    mime="text/csv"
                )
            else:
                st.error(f"API Error {response.status_code}: {response.text}")

        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")






