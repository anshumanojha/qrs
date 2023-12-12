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

def predict_next_month_revenue(monthly_data):
    # Prepare the input data
    X = pd.DataFrame({'Month': np.arange(1, len(monthly_data) + 1)})
    y = monthly_data.values.reshape(-1, 1)

    # Assuming a basic linear regression model for demonstration
    model = LinearRegression()
    model.fit(X, y)

    # Predict the next month
    next_month_data = pd.DataFrame({'Month': [len(monthly_data) + 1]})
    predicted_revenue = model.predict(next_month_data)[0][0]

    return predicted_revenue

def main():
    st.title("Data Analyst Resume and Future Revenue Prediction")

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

    # User Input: Enter monthly revenue for different months
    monthly_data = []
    for i in range(1, 13):  # Assuming predictions for 12 months
        revenue = st.number_input(f"Enter Revenue for Month {i}", value=0.0, step=0.01)
        monthly_data.append(revenue)

    if len(monthly_data) >= 2:
        # Predict the next month's revenue
        predicted_revenue = predict_next_month_revenue(pd.Series(monthly_data))

        st.write("Predicted Revenue for the Next Month:")
        st.write(predicted_revenue)

if __name__ == "__main__":
    main()
