import streamlit as st
import qrcode
from PIL import Image
import io
import sys
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import json  # Add this line

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

def predict_revenue(monthly_data, factors):
    # Prepare the input data
    X = pd.DataFrame({'Month': np.arange(1, len(monthly_data) + 1)})
    for factor, value in factors.items():
        X[factor] = value

    # Assuming a basic linear regression model for demonstration
    y = monthly_data.values.reshape(-1, 1)

    model = LinearRegression()
    model.fit(X, y)

    # Predict the next month
    next_month_data = X.iloc[-1, :].copy()
    next_month_data['Month'] += 1

    for factor, value in factors.items():
        next_month_data[factor] = value

    predicted_revenue = model.predict([next_month_data])[0][0]

    return predicted_revenue

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

    # User Input: Enter monthly revenue and factors affecting revenue
    monthly_data = st.text_area("Enter Monthly Revenue (comma-separated):")
    factors_text = st.text_area("Factors Affecting Revenue (JSON format):")

    if monthly_data and factors_text:
        # Parse entered data
        revenue_list = [float(val.strip()) for val in monthly_data.split(',')]
        factors = json.loads(factors_text)

        if len(revenue_list) >= 2:
            # Predict the next month's revenue
            predicted_revenue = predict_revenue(pd.Series(revenue_list), factors)

            st.write("Predicted Revenue for the Next Month:")
            st.write(predicted_revenue)

if __name__ == "__main__":
    main()
