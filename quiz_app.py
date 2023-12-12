import streamlit as st
import qrcode
from PIL import Image
import io
import sys
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

print(sys.executable)

def generate_qr_code(linkedin_url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=0,
    )
    qr.add_data(linkedin_url)
    qr.make(fit=True)
    
    img_byte_array = io.BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(img_byte_array)
    return img_byte_array.getvalue()

def predict_next_six_months_revenue(revenue_data):
    # Assuming a basic linear regression model for demonstration
    X = np.arange(1, len(revenue_data) + 1).reshape(-1, 1)
    y = revenue_data.values.reshape(-1, 1)

    model = LinearRegression()
    model.fit(X, y)

    # Predict the next 6 months
    next_six_months = np.arange(len(revenue_data) + 1, len(revenue_data) + 7).reshape(-1, 1)
    predicted_revenue = model.predict(next_six_months)

    return predicted_revenue.flatten()

def main():
    st.title("Data Analyst Resume and Revenue Prediction")

    # User Input: LinkedIn URL
    linkedin_url = st.text_input("Enter your LinkedIn URL:")
    
    if linkedin_url:
        # Display the entered LinkedIn URL
        st.write(f"LinkedIn URL: {linkedin_url}")

        # Generate and display the QR code
        qr_code_image = generate_qr_code(linkedin_url)
        st.image(Image.open(io.BytesIO(qr_code_image)), caption="Scan QR Code to visit LinkedIn profile", width=100)

    # Personal Information
    st.header("Personal Information")
    st.write("Name: John Doe")
    st.write("Email: john.doe@example.com")
    st.write("Phone: +1234567890")

    # Revenue Prediction
    st.header("Revenue Prediction")

    # User Input: Enter 6 months' revenue
    revenue_data = st.text_area("Enter 6 months' revenue (comma-separated):")
    
    if revenue_data:
        revenue_list = [float(val.strip()) for val in revenue_data.split(',')]
        if len(revenue_list) == 6:
            # Predict the coming 6 months' revenue
            predicted_revenue = predict_next_six_months_revenue(pd.Series(revenue_list))

            st.write("Predicted Revenue for the Coming 6 Months:")
            st.write(predicted_revenue)

if __name__ == "__main__":
    main()
